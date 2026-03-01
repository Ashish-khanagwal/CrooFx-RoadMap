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

project1 = Path("/project1")
project2 = Path("project2")

file1 = project1 / "src"
file2 = project2 / "src"

print(file1)  # -> Absolute path
print(file2)  # -> Relative path

# Absolute path

print(repo.is_absolute())
print(project.is_absolute())
print(fastapp.is_absolute())
print(home.is_absolute())
