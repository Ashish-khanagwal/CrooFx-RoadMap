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
