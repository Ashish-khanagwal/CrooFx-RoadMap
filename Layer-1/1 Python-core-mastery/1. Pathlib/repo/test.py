from pathlib import Path

path = Path(".")

# This will recognize the symlinks

for p in path.iterdir():
    print(p, "symlink: ", p.is_symlink())
