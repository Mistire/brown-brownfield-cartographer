import os
import shutil
import unittest
import networkx as nx
from agents.hydrologist import Hydrologist

class TestE2ELineage(unittest.TestCase):
    def setUp(self):
        self.test_dir = "/tmp/cartographer_e2e_test"
        os.makedirs(self.test_dir, exist_ok=True)
        
        # 1. Create Python file
        with open(os.path.join(self.test_dir, "ingest.py"), "w") as f:
            f.write("# Ingest from raw_data.csv to stg_users table\n")
            f.write("df = pd.read_csv('raw_data.csv')\n")
            f.write("df.to_sql('stg_users', conn)\n")
            
        # 2. Create SQL file
        with open(os.path.join(self.test_dir, "transform.sql"), "w") as f:
            f.write("INSERT INTO fct_orders SELECT * FROM stg_users JOIN stg_orders ON users.id = orders.user_id")
            
        # 3. Create DBT YAML file
        with open(os.path.join(self.test_dir, "schema.yml"), "w") as f:
            f.write("models:\n  - name: fct_orders\n    config:\n      owner: finance_team\n")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_mixed_language_lineage(self):
        hydrologist = Hydrologist(self.test_dir)
        hydrologist.run()
        
        graph = hydrologist.lineage_graph
        
        # Verify Nodes
        self.assertIn("raw_data.csv", graph.nodes)
        self.assertIn("stg_users", graph.nodes)
        self.assertIn("fct_orders", graph.nodes)
        
        # Verify Edges & Metadata
        # Python: raw_data.csv -> ingest.py -> stg_users
        self.assertTrue(graph.has_edge("raw_data.csv", "ingest.py"))
        self.assertTrue(graph.has_edge("ingest.py", "stg_users"))
        
        # SQL: stg_users -> transform.sql -> fct_orders (or direct edge if SQL analyzer works that way)
        # In our implementation, SQL lineage creates direct source -> target edges
        self.assertTrue(graph.has_edge("stg_users", "fct_orders"))
        
        # Verify Standardized Metadata
        node_data = graph.nodes["raw_data.csv"]
        self.assertEqual(node_data.get("inference_type"), "Static Analysis")
        self.assertEqual(node_data.get("confidence"), 1.0)
        
        edge_data = graph.get_edge_data("stg_users", "fct_orders")
        self.assertEqual(edge_data.get("inference_type"), "Static Analysis")
        self.assertEqual(edge_data.get("confidence"), 1.0)

if __name__ == "__main__":
    unittest.main()
