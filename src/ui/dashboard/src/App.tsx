import React, { useEffect, useState, useRef, useCallback, Suspense, Component, type ReactNode } from 'react';
import axios from 'axios';
import { 
  LayoutDashboard, GitGraph, Terminal, FileText, 
  Search, Plus, X, MessageSquare, 
  FileCode, Info, Map as MapIcon
} from 'lucide-react';
import ReactMarkdown from 'react-markdown';

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

/* ── Error Boundary ─────────────────────────────────────── */
class ErrorBoundary extends Component<
  { fallback: ReactNode; children: ReactNode },
  { hasError: boolean; error: string }
> {
  constructor(props: { fallback: ReactNode; children: ReactNode }) {
    super(props);
    this.state = { hasError: false, error: '' };
  }
  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error: error.message };
  }
  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '2rem', color: '#ef4444' }}>
          <h3>Component Error</h3>
          <p style={{ opacity: 0.7 }}>{this.state.error}</p>
        </div>
      );
    }
    return this.props.children;
  }
}

const ForceGraph = React.lazy(() =>
  import('react-force-graph-2d')
);

/* ── Knowledge Graph (lazy + error-safe) ────────────────── */
interface GraphNode {
  id: string;
  type?: 'dataset' | 'transformation' | 'module';
  x?: number;
  y?: number;
  purpose_statement?: string;
  complexity_score?: number;
  is_dead_candidate?: boolean;
}

const KnowledgeGraph: React.FC<{ project: string; type: 'module' | 'lineage'; onSelect: (node: GraphNode) => void }> = ({ project, type, onSelect }) => {
  const [data, setData] = useState<{ nodes: GraphNode[]; links: any[] }>({ nodes: [], links: [] });
  const fgRef = useRef<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      if (!project) return;
      try {
        const res = await axios.get(`${API_BASE}/graph/${project}?type=${type}`);
        const d = res.data || {};
        setData({
          nodes: Array.isArray(d.nodes) ? d.nodes : [],
          links: Array.isArray(d.links) ? d.links : []
        });
      } catch (err) {
        console.error('Failed to fetch graph data', err);
        setData({ nodes: [], links: [] });
      }
    };
    fetchData();
  }, [project, type]);

  return (
    <div className="graph-container">
      <ErrorBoundary fallback={<p style={{ padding: '2rem' }}>Graph could not be loaded.</p>}>
        <Suspense fallback={<p style={{ padding: '2rem', opacity: 0.5 }}>Loading graph engine…</p>}>
          <ForceGraph
            ref={fgRef}
            graphData={data}
            nodeLabel="id"
            nodeColor={(node: any) =>
              node.type === 'dataset' ? '#10b981' : node.type === 'transformation' ? '#f59e0b' : '#6366f1'
            }
            linkDirectionalArrowLength={3.5}
            linkDirectionalArrowRelPos={1}
            linkColor={() => 'rgba(255, 255, 255, 0.35)'}
            linkWidth={1.5}
            nodeRelSize={6}
            onNodeClick={(node: any) => {
              fgRef.current?.centerAt(node.x, node.y, 1000);
              fgRef.current?.zoom(2, 1000);
              onSelect(node);
            }}
            backgroundColor="#0a0a0c"
          />
        </Suspense>
      </ErrorBoundary>
    </div>
  );
};

/* ── Artifact Viewer ─────────────────────────────────────── */
const ArtifactViewer: React.FC<{ project: string; filename: string }> = ({ project, filename }) => {
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchArtifact = async () => {
      setLoading(true);
      try {
        const res = await axios.get(`${API_BASE}/metadata/${project}?filename=${filename}`);
        setContent(res.data.content);
      } catch {
        setContent('Artifact not found or analysis incomplete.');
      }
      setLoading(false);
    };
    fetchArtifact();
  }, [project, filename]);

  if (loading) return <div className="p-8 opacity-50">Loading artifact...</div>;

  return (
    <div className="artifact-container glass">
      <div className="artifact-body">
        <ReactMarkdown>{content}</ReactMarkdown>
      </div>
    </div>
  );
};

/* ── Build Console ──────────────────────────────────────── */
interface LogEntry {
  step: string;
  details: string | object;
}

const BuildConsole: React.FC<{ logs: LogEntry[] }> = ({ logs }) => {
  const scrollRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
  }, [logs]);

  return (
    <div className="console-container glass">
      <div className="console-header">
        <span className="dot red" />
        <span className="dot yellow" />
        <span className="dot green" />
        <span style={{ marginLeft: 10, fontSize: '0.7rem', color: '#666' }}>AGENT_ACTIVITY.LOG</span>
      </div>
      <div className="console-body" ref={scrollRef}>
        {logs.map((log, i) => (
          <div key={i} className="log-line">
            <span className="log-step">[{log.step?.toUpperCase()}]</span>
            <span className="log-details">
              {typeof log.details === 'string' ? log.details : JSON.stringify(log.details)}
            </span>
          </div>
        ))}
        {logs.length === 0 && <div className="log-line fade">Waiting for agent activity…</div>}
      </div>
    </div>
  );
};

/* ── New Analysis Form ──────────────────────────────────── */
const NewAnalysis: React.FC<{ onStart: (repo: string) => void }> = ({ onStart }) => {
  const [repo, setRepo] = useState('');
  return (
    <div className="glass" style={{ margin: '2rem', padding: '2rem', borderRadius: 12, maxWidth: 800 }}>
      <h3 style={{ marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: 10 }}>
        <Plus size={20} /> Map a New Repository
      </h3>
      <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '1.5rem' }}>
        Enter a local absolute path or a GitHub URL (e.g. https://github.com/user/repo).
      </p>
      <div style={{ display: 'flex', gap: '1rem' }}>
        <input
          type="text"
          className="glass"
          style={{
            flex: 1,
            padding: '12px 16px',
            color: 'white',
            borderRadius: 8,
            border: '1px solid rgba(255,255,255,0.1)',
          }}
          placeholder="https://github.com/dbt-labs/jaffle_shop"
          value={repo}
          onChange={e => setRepo(e.target.value)}
        />
        <button
          className="premium-gradient"
          style={{ border: 'none', padding: '12px 24px', borderRadius: 8, color: 'white', fontWeight: 'bold', cursor: 'pointer' }}
          onClick={() => onStart(repo)}
        >
          Begin Analysis
        </button>
      </div>
    </div>
  );
};

/* ── Dashboard (main) ───────────────────────────────────── */
const Dashboard: React.FC = () => {
  const [project, setProject] = useState<string | null>(null);
  const [projects, setProjects] = useState<string[]>([]);
  const [view, setView] = useState<'module' | 'lineage' | 'console' | 'brief' | 'codebase'>('module');
  const [chatOpen, setChatOpen] = useState(false);
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [chatMessages, setChatMessages] = useState<{ role: 'user' | 'bot'; text: string }[]>([]);
  const [isTyping, setIsTyping] = useState(false);
  const [input, setInput] = useState('');
  const [selectedNode, setSelectedNode] = useState<GraphNode | null>(null);
  const [stats, setStats] = useState({ modules: 0, complexity: 0 });
  const [elapsedTime, setElapsedTime] = useState(0);
  const [isTimerRunning, setIsTimerRunning] = useState(false);
  const timerRef = useRef<number | null>(null);

  const fetchProjects = useCallback(async () => {
    try {
      const res = await axios.get(`${API_BASE}/projects`);
      setProjects(res.data);
    } catch (err) {
      console.error('Failed to fetch projects', err);
    }
  }, []);

  useEffect(() => {
    fetchProjects();

    let ws: WebSocket | null = null;
    try {
      const wsUrl = API_BASE.replace('http', 'ws') + '/ws/analysis';
      ws = new WebSocket(wsUrl);
      ws.onmessage = event => {
        const data = JSON.parse(event.data);
        
        // Handle incoming logs with granular step filtering if needed
        setLogs(prev => [...prev, data]);
        
        if (data.step === 'pipeline_complete') {
          fetchProjects();
          setIsTimerRunning(false);
        }
      };
      ws.onclose = () => console.log('WebSocket closed');
      ws.onerror = () => console.warn('WebSocket connection failed – live logs unavailable');
    } catch {
      console.warn('Could not open WebSocket');
    }

    return () => {
      ws?.close();
    };
  }, [fetchProjects]);

  useEffect(() => {
    if (isTimerRunning) {
      timerRef.current = window.setInterval(() => {
        setElapsedTime(prev => prev + 1);
      }, 1000);
    } else {
      if (timerRef.current) clearInterval(timerRef.current);
    }
    return () => { if (timerRef.current) clearInterval(timerRef.current); };
  }, [isTimerRunning]);

  useEffect(() => {
    if (!project) {
      setStats({ modules: 0, complexity: 0 });
      setSelectedNode(null);
      return;
    }

    const fetchStats = async () => {
      try {
        const res = await axios.get(`${API_BASE}/graph/${project}?type=module`);
        const nodes = res.data.nodes || [];
        const avgComp = nodes.reduce((acc: number, n: any) => acc + (n.complexity_score || 0), 0) / (nodes.length || 1);
        setStats({ modules: nodes.length, complexity: parseFloat(avgComp.toFixed(1)) });
      } catch (err) {
        console.error("Stats fetch failed", err);
        setStats({ modules: 0, complexity: 0 });
      }
    };
    fetchStats();
    setSelectedNode(null); // Reset when project changes
  }, [project]);

  const handleSendMessage = async () => {
    if (!input.trim() || !project) return;
    const userMsg = input;
    setChatMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setInput('');
    setIsTyping(true);
    try {
      const res = await axios.post(`${API_BASE}/query`, { query: userMsg, project });
      setChatMessages(prev => [...prev, { role: 'bot', text: res.data.answer }]);
    } catch {
      setChatMessages(prev => [...prev, { role: 'bot', text: "Navigator is currently offline or project not found." }]);
    }
    setIsTyping(false);
  };

  const handleStartAnalysis = async (repo: string) => {
    setLogs([]);
    setElapsedTime(0);
    setIsTimerRunning(true);
    setView('console');
    try {
      await axios.post(`${API_BASE}/analyze`, { repo_path: repo });
    } catch {
      setLogs(prev => [...prev, { step: 'error', details: 'Failed to trigger analysis' }]);
    }
  };

  const activeAgent = logs.length > 0 ? (() => {
    const lastStep = logs[logs.length - 1].step || '';
    if (lastStep === 'pipeline_complete') return 'idle';
    if (lastStep === 'error') return 'error';
    if (lastStep.includes('_start')) return lastStep.replace('_start', '');
    if (lastStep.includes('_progress')) return lastStep.replace('_progress', '');
    return 'orchestrator';
  })() : 'idle';

  return (
    <div className="dashboard-container">
      <aside className="glass">
        <div className="logo-section" style={{ cursor: 'pointer', padding: '1rem 0' }} onClick={() => setView('module')}>
          <h2 style={{ display: 'flex', alignItems: 'center', gap: 10, margin: 0 }}>
            <MapIcon className="accent" size={24} />
            <span style={{ fontSize: '1.2rem', fontWeight: 800, letterSpacing: '-0.02em' }}>CARTOGRAPHER</span>
          </h2>
        </div>

        <nav style={{ marginTop: '1rem', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          <div className={`nav-item ${view === 'module' ? 'active' : ''}`} onClick={() => setView('module')}>
            <LayoutDashboard size={18} /> System Map
          </div>
          <div className={`nav-item ${view === 'lineage' ? 'active' : ''}`} onClick={() => setView('lineage')}>
            <GitGraph size={18} /> Data Lineage
          </div>

          <div style={{ padding: '0 16px', marginTop: '1.5rem', marginBottom: '0.5rem' }}>
            <p style={{ fontSize: '0.65rem', color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.05em', margin: 0 }}>
              Documentation
            </p>
          </div>

          <div className={`nav-item ${view === 'brief' ? 'active' : ''}`} onClick={() => setView('brief')}>
            <FileText size={18} /> Onboarding Brief
          </div>
          <div className={`nav-item ${view === 'codebase' ? 'active' : ''}`} onClick={() => setView('codebase')}>
            <FileCode size={18} /> CODEBASE.md
          </div>

          <div style={{ borderTop: '1px solid rgba(255,255,255,0.05)', marginTop: '0.5rem', paddingTop: '0.5rem' }}>
            <div className={`nav-item ${view === 'console' ? 'active' : ''}`} onClick={() => setView('console')}>
              <Terminal size={18} /> Build Console
            </div>
          </div>

          <div style={{ marginTop: '1rem' }}>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', padding: '0 16px', marginBottom: 4 }}>
              PROJECTS
            </p>
            <select
              className="glass"
              style={{ width: '100%', padding: 8, color: 'white', borderRadius: 8 }}
              onChange={e => {
                setProject(e.target.value);
                if (view === 'console') setView('module');
              }}
              value={project || ''}
            >
              <option value="">Select Project</option>
              {projects.map((p: string) => (
                <option key={p} value={p}>{p}</option>
              ))}
            </select>
            <button
              className="glass"
              style={{ width: '100%', marginTop: '0.5rem', padding: '8px', border: '1px dashed rgba(255,255,255,0.2)', color: 'white', borderRadius: 8, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8 }}
              onClick={() => { setProject(null); setView('module'); }}
            >
              <Plus size={16} /> New Analysis
            </button>
          </div>
        </nav>

        <div style={{ marginTop: 'auto' }}>
          <div className="nav-item" onClick={() => setChatOpen(!chatOpen)}>
            <MessageSquare size={18} /> Navigator Chat
          </div>
        </div>
      </aside>

      {/* ── Main ── */}
      <main>
        <header className="glass">
          <div style={{ display: 'flex', gap: '2rem' }}>
            <div className="stat">
              <span className="label">Modules / Datasets</span>
              <span className="value">{stats.modules}</span>
            </div>
            <div className="stat">
              <span className="label">Avg Complexity</span>
              <span className="value">{stats.complexity}</span>
            </div>
            <div className="stat">
              <span className="label">Status</span>
              <span className="value" style={{ color: activeAgent === 'error' ? '#ef4444' : '#10b981' }}>
                {activeAgent === 'idle' ? 'Ready' : activeAgent.toUpperCase()}
              </span>
            </div>
            {(isTimerRunning || elapsedTime > 0) && (
              <div className="stat">
                <span className="label">{isTimerRunning ? 'Analyzing...' : 'Duration'}</span>
                <span className="value accent">{elapsedTime}s</span>
              </div>
            )}
            {activeAgent !== 'idle' && (
              <div className="agent-activity-pill">
                <span className="pulse-dot" /> Active Agent: {activeAgent}
              </div>
            )}
          </div>
          <div style={{ flex: 1 }} />
          <button
            className="premium-gradient"
            style={{ border: 'none', color: 'white', cursor: 'pointer', padding: '10px 20px', borderRadius: 8, fontWeight: 600, display: 'flex', alignItems: 'center', gap: 8 }}
            onClick={() => { setProject(null); setStats({ modules: 0, complexity: 0 }); }}
          >
            <Plus size={16} /> New Project
          </button>
        </header>

        {(view === 'console' || isTimerRunning) ? (
          <BuildConsole logs={logs} />
        ) : !project ? (
          <NewAnalysis onStart={handleStartAnalysis} />
        ) : view === 'brief' ? (
          <ArtifactViewer project={project!} filename="onboarding_brief.md" />
        ) : view === 'codebase' ? (
          <ArtifactViewer project={project!} filename="CODEBASE.md" />
        ) : (
          <div style={{ position: 'relative', flex: 1, display: 'flex' }}>
            <KnowledgeGraph project={project} type={view === 'lineage' ? 'lineage' : 'module'} onSelect={setSelectedNode} />
            {selectedNode && (
               <div className="inspector-panel glass">
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem', alignItems: 'center' }}>
                   <h4 style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                     <Info size={18} /> Details
                   </h4>
                   <button onClick={() => setSelectedNode(null)} style={{ background: 'none', border: 'none', color: 'white', cursor: 'pointer' }}>
                     <X size={18} />
                   </button>
                 </div>
                 <div className="inspector-content">
                   <p className="label">ID / PATH</p>
                   <p className="value code">{selectedNode?.id}</p>
                   
                   <p className="label">PURPOSE</p>
                   <p className="value">{selectedNode?.purpose_statement || 'No semantic analysis available yet.'}</p>
                   
                   <p className="label">STATISTICS</p>
                   <div style={{ display: 'flex', gap: '1rem' }}>
                    <div>
                      <p className="label">Complexity</p>
                      <p className="value">{selectedNode?.complexity_score || 0}</p>
                    </div>
                    <div>
                      <p className="label">Status</p>
                      <p className="value" style={{ color: selectedNode?.is_dead_candidate ? '#ef4444' : '#10b981' }}>
                        {selectedNode?.is_dead_candidate ? 'Dead' : 'Active'}
                      </p>
                    </div>
                   </div>
                 </div>
               </div>
            )}
          </div>
        )}

        {chatOpen && (
          <div className="chat-overlay glass">
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem', alignItems: 'center' }}>
              <h3 style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <Search size={20} /> Navigator
              </h3>
              <button onClick={() => setChatOpen(false)} style={{ background: 'none', border: 'none', color: 'white', cursor: 'pointer' }}>
                <X size={20} />
              </button>
            </div>
            <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {chatMessages.map((m: { role: string; text: string }, i: number) => (
                <div key={i} className={`glass message ${m.role}`} style={{ padding: '12px 16px', borderRadius: 12, alignSelf: m.role === 'user' ? 'flex-end' : 'flex-start', maxWidth: '85%' }}>
                  <div className="prose-chat">
                    <ReactMarkdown>{m.text}</ReactMarkdown>
                  </div>
                </div>
              ))}
              {isTyping && <div className="log-line fade">Navigator is searching knowledge base…</div>}
              {chatMessages.length === 0 && <div className="glass" style={{ padding: 12, borderRadius: 8 }}>How can I help you understand this codebase?</div>}
            </div>
            <div style={{ marginTop: '1rem', display: 'flex', gap: 8 }}>
              <input 
                type="text" 
                className="glass" 
                style={{ flex: 1, padding: 12, color: 'white', borderRadius: 8, border: '1px solid rgba(255,255,255,0.1)' }} 
                placeholder="Ask a question…" 
                value={input}
                onChange={e => setInput(e.target.value)}
                onKeyPress={e => e.key === 'Enter' && handleSendMessage()}
              />
              <button 
                className="premium-gradient" 
                style={{ border: 'none', padding: '0 20px', borderRadius: 8, color: 'white', fontWeight: 'bold', cursor: 'pointer' }}
                onClick={handleSendMessage}
              >
                Send
              </button>
            </div>
          </div>
        )}
      </main>

      <style>{`
        .nav-item { display:flex; align-items:center; gap:12px; padding:10px 16px; border-radius:8px; cursor:pointer; transition:all .2s; color:var(--text-secondary); }
        .nav-item:hover,.nav-item.active { background:rgba(255,255,255,.05); color:white; }
        .nav-item.active { border-left:3px solid var(--accent-primary); }
        .stat { display:flex; flex-direction:column; }
        .stat .label { font-size:.7rem; color:var(--text-secondary); text-transform:uppercase; }
        .stat .value { font-weight:bold; font-size:1.1rem; }
        .console-container { flex:1; margin:2rem; border-radius:12px; display:flex; flex-direction:column; overflow:hidden; background:#0d0d0f; border:1px solid rgba(255,255,255,.05); }
        .console-header { padding:10px 16px; background:#1a1a1e; display:flex; align-items:center; gap:6px; }
        .dot { width:12px; height:12px; border-radius:50%; }
        .dot.red { background:#ff5f56; }
        .dot.yellow { background:#ffbd2e; }
        .dot.green { background:#27c93f; }
        .console-body { flex:1; padding:16px; font-family:'JetBrains Mono','Fira Code',monospace; font-size:.85rem; overflow-y:auto; color:#d1d1d1; background:#000; }
        .log-line { margin-bottom:4px; line-height:1.4; border-bottom:1px solid rgba(255,255,255,.03); padding-bottom:2px; }
        .log-step { color:#6366f1; margin-right:12px; font-weight:bold; font-size:.75rem; }
        .log-details { word-break:break-all; }
        .log-line.fade { opacity:.5; font-style:italic; }
        .chat-overlay { position:absolute; bottom:20px; right:20px; width:400px; height:500px; border-radius:16px; display:flex; flex-direction:column; padding:1.5rem; box-shadow:0 10px 30px rgba(0,0,0,.5); z-index:1000; animation:slideUp .3s ease-out; }
        .message.user { background: rgba(99, 102, 241, 0.2); border: 1px solid rgba(99, 102, 241, 0.3); }
        .agent-activity-pill { background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); color: #10b981; padding: 4px 12px; border-radius: 99px; font-size: 0.75rem; display: flex; align-items: center; gap: 8px; }
        .pulse-dot { width: 8px; height: 8px; border-radius: 50%; background: #10b981; animation: pulse 2s infinite; }
        .inspector-panel { position: absolute; right: 20px; top: 20px; width: 320px; max-height: 80%; overflow-y: auto; padding: 1.5rem; border-radius: 12px; z-index: 500; animation: slideIn .3s ease-out; }
        .inspector-panel p.label { font-size: 0.65rem; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 2px; margin-top: 12px; }
        .inspector-panel p.value { font-size: 0.9rem; color: #fff; line-height: 1.4; }
        .inspector-panel p.value.code { font-family: monospace; font-size: 0.75rem; word-break: break-all; background: rgba(0,0,0,0.3); padding: 4px; border-radius: 4px; }
        .prose-chat { font-size: 0.9rem; color: rgba(255,255,255,0.9); }
        .prose-chat p { margin-bottom: 0.5rem; }
        .prose-chat code { background: rgba(0,0,0,0.2); padding: 2px 4px; border-radius: 4px; font-family: monospace; font-size: 0.8rem; }
        
        /* ── Artifact Markdown Styling ──────────────────────────── */
        .artifact-container { flex: 1; margin: 2rem; overflow-y: auto; padding: 3rem; max-width: 900px; line-height: 1.6; }
        .artifact-body h1 { font-size: 2rem; margin-bottom: 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem; }
        .artifact-body h2 { font-size: 1.5rem; margin-top: 2rem; margin-bottom: 1rem; color: var(--accent-primary); }
        .artifact-body h3 { font-size: 1.25rem; margin-top: 1.5rem; margin-bottom: 0.75rem; }
        .artifact-body p { margin-bottom: 1rem; color: rgba(255,255,255,0.8); }
        .artifact-body ul, .artifact-body ol { margin-left: 1.5rem; margin-bottom: 1rem; }
        .artifact-body li { margin-bottom: 0.5rem; }
        .artifact-body code { background: rgba(255,255,255,0.05); padding: 0.2rem 0.4rem; border-radius: 4px; font-family: monospace; font-size: 0.9em; }
        .artifact-body pre { background: #000; padding: 1.5rem; border-radius: 8px; overflow-x: auto; margin-bottom: 1.5rem; border: 1px solid rgba(255,255,255,0.05); }
        .artifact-body table { width: 100%; border-collapse: collapse; margin-bottom: 1.5rem; }
        .artifact-body th, .artifact-body td { padding: 0.75rem; border: 1px solid rgba(255,255,255,0.1); text-align: left; }
        .artifact-body th { background: rgba(255,255,255,0.05); }
        
        @keyframes slideIn { from{transform:translateX(20px);opacity:0;} to{transform:translateX(0);opacity:1;} }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
        @keyframes slideUp { from{transform:translateY(20px);opacity:0;} to{transform:translateY(0);opacity:1;} }
      `}</style>
    </div>
  );
};

export default Dashboard;
