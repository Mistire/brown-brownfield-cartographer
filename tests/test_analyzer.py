import pytest
import os
from src.analyzers.tree_sitter_analyzer import SurveyorAnalyzer

def test_python_analysis(tmp_path):
    code = """
import os
from datetime import datetime

class MyClass:
    def method(self):
        pass

def my_function(a, b):
    return a + b
"""
    file_path = tmp_path / "test.py"
    file_path.write_text(code)
    
    analyzer = SurveyorAnalyzer()
    results = analyzer.analyze_module(str(file_path))
    
    assert results["language"] == "python"
    assert "os" in results["imports"]
    assert "datetime" in results["imports"]
    assert "MyClass" in results["classes"]
    assert "my_function" in results["functions"]
    assert "method" in results["functions"]
