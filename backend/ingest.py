# backend/ingest.py
import subprocess
from pathlib import Path

REPO_DIR = "store/repo"

def clone_repo(url):
    subprocess.run(
        ["git", "clone", url, REPO_DIR],
        check=True
    )
    return REPO_DIR

def collect_files(base):
    files = []
    for p in Path(base).rglob("*"):
        if (
            p.suffix in [".py", ".js", ".ts"]
            and "test" not in p.name.lower()
            and "node_modules" not in p.parts
            and "venv" not in p.parts
        ):
            files.append(p)
    return files
