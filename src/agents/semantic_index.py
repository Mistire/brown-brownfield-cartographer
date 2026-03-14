import numpy as np
import json
import os
from typing import List, Dict, Any, Tuple

class SemanticIndex:
    """
    A simple vector store for module purpose statements.
    Stores embeddings in a numpy array and metadata in a JSON file.
    """
    def __init__(self, index_dir: str):
        self.index_dir = index_dir
        self.embeddings_path = os.path.join(index_dir, "embeddings.npy")
        self.metadata_path = os.path.join(index_dir, "metadata.json")
        
        self.embeddings = None
        self.metadata = []
        
        if os.path.exists(self.metadata_path):
            with open(self.metadata_path, "r") as f:
                self.metadata = json.load(f)
        
        if os.path.exists(self.embeddings_path):
            self.embeddings = np.load(self.embeddings_path)

    def add_entry(self, path: str, purpose: str, embedding: List[float]):
        """Adds a new entry to the index."""
        new_embedding = np.array(embedding, dtype=np.float32).reshape(1, -1)
        
        if self.embeddings is None:
            self.embeddings = new_embedding
        else:
            self.embeddings = np.vstack([self.embeddings, new_embedding])
            
        self.metadata.append({
            "path": path,
            "purpose": purpose
        })

    def save(self):
        """Persists the index to disk."""
        os.makedirs(self.index_dir, exist_ok=True)
        if self.embeddings is not None:
            np.save(self.embeddings_path, self.embeddings)
        with open(self.metadata_path, "w") as f:
            json.dump(self.metadata, f, indent=2)

    def search(self, query_embedding: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """Performs cosine similarity search."""
        if self.embeddings is None:
            return []
            
        query_vec = np.array(query_embedding, dtype=np.float32)
        
        # Compute cosine similarity
        # (embeddings . query) / (||embeddings|| * ||query||)
        norm_embeddings = np.linalg.norm(self.embeddings, axis=1)
        norm_query = np.linalg.norm(query_vec)
        
        similarities = np.dot(self.embeddings, query_vec) / (norm_embeddings * norm_query + 1e-10)
        
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            results.append({
                "path": self.metadata[idx]["path"],
                "purpose": self.metadata[idx]["purpose"],
                "score": float(similarities[idx])
            })
            
        return results
