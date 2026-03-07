from pathlib import Path

# Current directory
print(Path.cwd())

# Files and dir in current directory
for p in Path().iterdir():
    print(p)

my_dir = Path("repo")
my_file = Path("pathlib-tut.py")

print(my_dir)
print(my_file)

print(my_dir.stem)
print(my_file.stem)

print(my_dir.parent)
print(my_file.parent)

print(my_file.suffix)

p = Path(".").resolve()
print("path: ", p)

# __file__ used for current directory or file
p1 = Path(__file__).resolve().parent
print(p1)


# to access the home folder of the user.
p2 = Path("~/dotfiles").resolve()
print(p2)

# OUTPUT
# /Users/ashishkhanagwal/Documents/ASHISH/2. TECH/Croovi-org/CrooFx-RoadMap/Layer-1/1 Python-core-mastery/1. Pathlib/~/dotfiles
# See it still contains that '~' so .resolve() didn't work the way we anticipated.

# thats why we use expanduser()
p3 = Path("~/dotfiles").expanduser()
print(p3)

# OUTPUT
# /Users/ashishkhanagwal/dotfiles

# ANOTHER METHOD
p4 = Path.home() / "dotfiles"
print(p4)
# OUTPUT is same.
# /Users/ashishkhanagwal/dotfiles

# glob -> in current directory
for q in p.glob("*p*"):  # has p in whole word
    print(q)

print("\n")
# recursive glob rglob -> goes in subdirectories
for q in p.rglob("*.py"):  # ends with .py
    print(q)

print("\n")
# All fies
for q in p.rglob("*"):
    print(q)

# This is how we read a file.
file = p / "repo/test.py"

with open(file) as f:
    print(f.read())

# Creating & Deleting Directories
dir = Path("TempDir")
# dir.mkdir() -> Create
# dir.rmdir() -> Delete

sdir = Path("TempDir/subdir")
# sdir.mkdir(parents=True)  # Creating subdirectories

# Creating Files
fil = Path("temp_file.txt")
# fil.touch() -> Creating files
# fil.rename("tempfile.txt") -> It can overwrite the file
# fil.replace("temp_file.txt")
# fil.unlink() -> Deleting file
