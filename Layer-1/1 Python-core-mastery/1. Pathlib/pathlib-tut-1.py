from pathlib import Path

path = Path("project/src/../core/file.py")

# Attributes
print(repr(path))
print(repr(path.name))
print(repr(path.stem))
print(repr(path.parent))
print(repr(path.suffix))
print(path.is_absolute())

# "project/src/../core/file.py"
# right now this looks messy, there are two ways to clean it.

# .absolute()
# It converts a relative path into an absolute path.
# It prefixes current working directory

print(path.absolute())
# output:
# /Users/ashishkhanagwal/Documents/ASHISH/2. TECH/Croovi-org/CrooFx-RoadMap/Layer-1/1 Python-core-mastery/1. Pathlib/project/src/../core/file.py
# Notice: the .. is still there, it did not normalize structure.

# .resolve()
# This is much stronger
# It converts to absolute
# remove . and ..
# resolves symlinks
# touches filesystem

print(path.resolve())
# output:
# /Users/ashishkhanagwal/Documents/ASHISH/2. TECH/Croovi-org/CrooFx-RoadMap/Layer-1/1 Python-core-mastery/1. Pathlib/project/core/file.py

p = Path("a/b/../c/file.txt")

print("Original:", p)
print("Absolute:", p.absolute())
print("Resolve:", p.resolve())

repo = Path(".")
repo_root = repo.resolve()
print(repo_root)


p1 = Path("a/../b")
print(p1.absolute())
print(p1.resolve())

if repo.is_symlink():
    print("this is a symlink")
else:
    print("Not a symlink")


print(Path.cwd())
