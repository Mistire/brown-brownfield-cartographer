from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import os
import json
import networkx as nx
from typing import Dict, Any, List, Optional
from pydantic import BaseModel
import asyncio
import subprocess
from orchestrator import Orchestrator
from graph.knowledge_graph import KnowledgeGraph

app = FastAPI(title="Brownfield Cartographer API")

# Enable CORS for frontend development
_ALLOWED_ORIGINS = [o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173").split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_ALLOWED_ORIGINS,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

CARTOGRAPHY_DIR = os.getenv("CARTOGRAPHY_DIR", ".cartography")
TARGETS_DIR = os.getenv("TARGETS_DIR", "targets")
os.makedirs(TARGETS_DIR, exist_ok=True)

MAX_WS_MESSAGE_BYTES = int(os.getenv("WS_MAX_MESSAGE_BYTES", 65536))   # 64 KB default
WS_IDLE_TIMEOUT_SECS = int(os.getenv("WS_IDLE_TIMEOUT_SECS", 300))    # 5 min default

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in list(self.active_connections):
            try:
                await connection.send_text(message)
            except Exception:
                self.active_connections.remove(connection)

manager = ConnectionManager()

class AnalysisRequest(BaseModel):
    repo_path: str # Can be a local path or a git URL

class QueryRequest(BaseModel):
    query: str
    project: str

@app.get("/projects")
def list_projects():
    if not os.path.exists(CARTOGRAPHY_DIR):
        return []
    return [d for d in os.listdir(CARTOGRAPHY_DIR) if os.path.isdir(os.path.join(CARTOGRAPHY_DIR, d))]

@app.get("/graph/{project}")
def get_graph(project: str, type: str = "module"):
    path = os.path.join(CARTOGRAPHY_DIR, project, f"{type}_graph.json")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Graph not found")
    
    with open(path, "r") as f:
        data = json.load(f)
    
    # Transform NetworkX format to react-force-graph format
    nodes = data.get("nodes", [])
    links = data.get("links", data.get("edges", []))
    return {"nodes": nodes, "links": links}

@app.get("/metadata/{project}")
def get_metadata(project: str, filename: str = "CODEBASE.md"):
    path = os.path.join(CARTOGRAPHY_DIR, project, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail=f"Artifact '{filename}' not found for project '{project}'")
    
    with open(path, "r") as f:
        return {"content": f.read()}

# In-memory store for navigator instances to persist state per session
navigators: Dict[str, Any] = {}

@app.post("/query")
async def run_query(req: QueryRequest):
    from agents.navigator import Navigator
    from utils.paths import get_cartography_dir
    
    project_path = os.path.join(get_cartography_dir(), req.project)
    if not os.path.exists(project_path):
        raise HTTPException(status_code=404, detail="Project not analyzed yet")
        
    # Lazy load navigator for the project
    nav_key = f"{req.project}"
    if nav_key not in navigators:
        # Use the base cartography dir and project name
        navigators[nav_key] = Navigator(project_path)
    
    try:
        navigator = navigators[nav_key]
        if not navigator.kg.module_graph.nodes:
             # Try reloading if empty
             navigator.kg = KnowledgeGraph.load(project_path)
             
        answer = await navigator.query(req.query)
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"Navigator encountered an error: {str(e)}"}

@app.websocket("/ws/analysis")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            try:
                data = await asyncio.wait_for(
                    websocket.receive_text(),
                    timeout=WS_IDLE_TIMEOUT_SECS
                )
                if len(data.encode()) > MAX_WS_MESSAGE_BYTES:
                    await websocket.close(code=1009)  # Message Too Big
                    manager.disconnect(websocket)
                    return
            except asyncio.TimeoutError:
                await websocket.close(code=1001)  # Going Away (idle)
                manager.disconnect(websocket)
                return
    except WebSocketDisconnect:
        manager.disconnect(websocket)

async def run_analysis_task(repo_path: str):
    actual_path = repo_path
    
    if repo_path.startswith(("http://", "https://", "git@")):
        project_name = repo_path.split("/")[-1].replace(".git", "")
        actual_path = os.path.join(TARGETS_DIR, project_name)
        
        await manager.broadcast(json.dumps({"step": "clone_start", "details": f"Cloning {repo_path} to {actual_path}..."}))
        
        if not os.path.exists(actual_path):
            try:
                subprocess.check_call(["git", "clone", repo_path, actual_path])
                await manager.broadcast(json.dumps({"step": "clone_complete", "details": "Clone successful."}))
            except Exception as e:
                await manager.broadcast(json.dumps({"step": "error", "details": f"Clone failed: {str(e)}"}))
                return
        else:
            await manager.broadcast(json.dumps({"step": "clone_skip", "details": "Repository already exists, using existing files."}))

    main_loop = asyncio.get_running_loop()

    def progress_callback(step: str, details: Any):
        # Called from sync threads; must use threadsafe broadcast
        asyncio.run_coroutine_threadsafe(
            manager.broadcast(json.dumps({"step": step, "details": details})), 
            main_loop
        )

    try:
        orchestrator = Orchestrator(actual_path, on_progress=progress_callback)
        await orchestrator.run_full_pipeline()
        await manager.broadcast(json.dumps({"step": "pipeline_complete", "details": "Analysis finished successfully."}))
    except Exception as e:
        await manager.broadcast(json.dumps({"step": "error", "details": f"Analysis failed: {str(e)}"}))

@app.post("/analyze")
async def trigger_analysis(req: AnalysisRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_analysis_task, req.repo_path)
    return {"message": "Analysis started", "repo_path": req.repo_path}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
