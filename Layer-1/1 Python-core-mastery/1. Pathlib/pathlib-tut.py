from pathlib import Path

# Path is a class that represents a file system

repo = Path("/repo")  # <- It makes an object that knows how path works on my OS.
file = repo / "src" / "main.py"

# "/" is operator overloading, it does not mean division here.
# It means join these paths in an OS-safe way.
# Internally it calls something like:
# repo.joinpath("src").joinpath("main.py")
# this doesn't create folders, it only creates a path object in the memory.

print(file)
print(type(file))

project = Path("/project")  # -> This is absolute path, full address from root.
project_file = project / "src" / "core" / "scanner.py"
print(project_file)

fastapp = Path("fastapp")  # -> This is relative path, from current folder.
# fastapp folder inside my current working directory.
project_file2 = fastapp / "src" / "main.py"
print(project_file2)
print(fastapp.resolve())  # -> This is how we will seee the full absolute version.

print(type(project_file))
print(project_file.parts)
# It breaks a path into its componenets
# ('project', 'src', 'core', 'scanner.py')
# A path is structured data — not text.

home = Path.home()
print(home)
# Give me the home directory of the home user.

# Absolute path -> A path that starts from the root of the filesystem.
project1 = Path("/project1")
# Go to the root of the computer -> then find folder project1.

# Relative path -> A path that starts from your current working directory.
project2 = Path("project2")
# Looks for project2 inside the folder where the script is running.

file1 = project1 / "src"
file2 = project2 / "src"

# Joining paths does not change absolute/relative nature.
# If the base path is relative -> result is relative.
# If the base path is absolute -> result is absolute.

print(file1)  # -> Absolute path
print(file2)  # -> Relative path
print(file1.cwd())

p1 = Path("/a") / "b"
p2 = Path("a") / "b"

print(p1)
print(p2)

print(p1.is_absolute())
print(p2.is_absolute())

print(repo.is_absolute())
print(project.is_absolute())
print(fastapp.is_absolute())
print(home.is_absolute())

path = Path("usr/file01.txt")

print(repr(path.name))  # final component of the path 'file01.txt'
print(repr(path.stem))  # file name without extension 'file01'
print(repr(path.suffix))  # the extension, it only returns the last extension '.txt'
print(repr(path.parent))  # Everything except the last part 'usr'

print(path.parts)

new_path = path.parent / (path.stem + "_flashcard.txt")
print(repr(new_path))
# / is used to concatenate the path

p = Path("archive.tar.gz")

print(p.suffix)  # As it only prints the last extension '.gz'
print(p.suffixes)  # It will print all extensions '.tar, .gz'
print(p.stem)  # .stem only removes the last extension.

t = Path("project/src/core/main.py")
print(t.name)  # 'main.py'
print(t.suffix)  # '.py'
print(t.parent)  # 'project/src/core'
print(t.stem)  # 'main'
print(t.parent.parent)  # 'project/src'
print(t.parent.parent.parent)  # 'project'
print(repr(t))
