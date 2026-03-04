from pathlib import Path

repo = Path(".")

# This will recognize the symlinks

for p in repo.iterdir():
    print(p, "symlink: ", p.is_symlink())

# OUTPUT
# src symlink: False
# link1 symlink: True
# link2 symlink: True
# test.py symlink: False

# See Where the Symlink Points
for p in repo.iterdir():
    if p.is_symlink():
        print(p, "points to", p.resolve())

# link2 points to /private/etc
# link1 points to /Users/ashishkhanagwal/Documents/ASHISH/2. TECH/Croovi-org/CrooFx-RoadMap/Layer-1/1 Python-core-mastery/1. Pathlib/repo/src

# Get the repository root
repo_root = repo.resolve()

# Loop through items in repo
for p in repo_root.iterdir():

    # Check if it is a symlink
    if p.is_symlink():
        target = p.resolve()

        # If target is inside the repo -> safe
        if target.is_relative_to(repo_root):
            print(f"FOLLOW {p.name}")

        # If target is outside the repo -> Dangerous
        else:
            print(f"IGNORE {p.name}")
