from pathlib import Path

# Path is a class that represents a file system

repo = Path("/repo")  # <- It makes an object that knows how path works on my OS.
file = repo / "src" / "main.py"

for p in repo.rglob("*"):
    print(p)

print(file)
