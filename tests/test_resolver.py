import pytest
import os
from src.utils.resolver import PathResolver

def test_resolve_absolute_import(tmp_path):
    # Setup mock repo
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "src").mkdir()
    (repo / "src" / "utils").mkdir()
    (repo / "src" / "utils" / "auth.py").write_text("pass")
    
    resolver = PathResolver(str(repo))
    resolved = resolver.resolve_import("src.utils.auth")
    assert resolved == "src/utils/auth.py"

def test_resolve_relative_import(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "common").mkdir()
    (repo / "common" / "utils.py").write_text("pass")
    
    current_file = str(repo / "models" / "auth.py")
    os.makedirs(os.path.dirname(current_file), exist_ok=True)
    
    resolver = PathResolver(str(repo))
    # ..common.utils from models/auth.py
    resolved = resolver.resolve_import("..common.utils", current_file)
    assert resolved == "common/utils.py"

def test_resolve_not_found():
    resolver = PathResolver("/tmp")
    assert resolver.resolve_import("nonexistent.module") is None
