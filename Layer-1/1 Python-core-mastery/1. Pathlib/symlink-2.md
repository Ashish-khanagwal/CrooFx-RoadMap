# Hands-On Symlink Demo

---

## 1️⃣ Create the Folder Structure

Open terminal and run:

```bash
mkdir repo
cd repo
mkdir src
touch src/main.py
```

Your repo now looks like:

```
repo/
 └── src/
      └── main.py
```

---

## 2️⃣ Create Symlink # — Internal Symlink

Create a symlink pointing **inside** the repo:

```bash
ln -s src link1
```

Meaning: `link1 -> src`

```
repo/
 ├── src/
 │    └── main.py
 └── link1 -> src
```

Opening `repo/link1/main.py` will show the same file as `repo/src/main.py` - no duplication, just a pointer.

---

## 3️⃣ Create Symlink # 2- External Symlink

Now create a link pointing **outside** the repo:

```bash
ln -s /etc link2
```

```
repo/
 ├── src/
 │    └── main.py
 ├── link1 -> src
 └── link2 -> /etc
```

---

## 4️⃣ Verify the Symlinks

Run:

```bash
ls -l
```

You should see:

```
src/
link1 -> src
link2 -> /etc
```

The `->` means it's a symlink.

---

## 5️⃣ Test in Python

Create a file:

```bash
touch test.py
```

Add this code:

```python
from pathlib import Path

repo = Path(".")

for p in repo.iterdir():
    print(p, "symlink:", p.is_symlink())
```

Run:

```bash
python test.py
```

Output:

```
src symlink: False
link1 symlink: True
link2 symlink: True
test.py symlink: False
```

Python correctly detects them.

---

## 6️⃣ See Where Each Symlink Points

Modify the code:

```python
from pathlib import Path

repo = Path(".")

for p in repo.iterdir():
    if p.is_symlink():
        print(p, "points to", p.resolve())
```

Output:

```
link1 points to /Users/.../repo/src
link2 points to /etc
```

Now you can see exactly why Croofx must control symlinks.

---

## 7️⃣ What This Demonstrates

You now have two cases side by side:

| Symlink         | Target     | Stays inside repo? | Croofx should... |
| --------------- | ---------- | ------------------ | ---------------- |
| `link1 -> src`  | `repo/src` | ✅ Yes             | Follow it        |
| `link2 -> /etc` | `/etc`     | ❌ No              | Ignore it        |

This is the exact problem that a symlink policy solves.

# Python Example - Follow Safe Symlinks, Ignore Dangerous Ones

---

## Repo Structure

```
repo/
 ├── src/
 │    └── main.py
 ├── link1 -> src
 ├── link2 -> /etc
```

**Goal:** print `FOLLOW link1` and `IGNORE link2`.

---

## The Code

```python
from pathlib import Path

# Get the repository root
repo_root = Path(".").resolve()

# Loop through items in repo
for p in repo_root.iterdir():

    # Check if it is a symlink
    if p.is_symlink():

        target = p.resolve()

        # If target is inside repo → safe
        if target.is_relative_to(repo_root):
            print(f"FOLLOW {p.name}")

        # If target is outside repo → ignore
        else:
            print(f"IGNORE {p.name}")
```

---

## Step by Step Explanation

### 1️⃣ Get the Real Repo Root

```python
repo_root = Path(".").resolve()
# → /Users/ashish/repo
```

`.resolve()` makes the path absolute and clean - no ambiguity about where we are.

---

### 2️⃣ Iterate Through Repo Files

```python
for p in repo_root.iterdir():
```

`iterdir()` lists everything directly inside the folder:

```
src
link1
link2
```

---

### 3️⃣ Check If Something Is a Symlink

```python
p.is_symlink()
```

| Item    | Result  |
| ------- | ------- |
| `src`   | `False` |
| `link1` | `True`  |
| `link2` | `True`  |

---

### 4️⃣ Find the Real Target

```python
target = p.resolve()
```

| Symlink | Resolves to              |
| ------- | ------------------------ |
| `link1` | `/Users/ashish/repo/src` |
| `link2` | `/etc`                   |

---

### 5️⃣ Check If th Target Is Inside the Repo

```python
target.is_relative_to(repo_root)
```

| Target                   | Inside repo? | Decision       |
| ------------------------ | ------------ | -------------- |
| `/Users/ashish/repo/src` | ✅ `True`    | `FOLLOW link1` |
| `/etc`                   | ❌ `False`   | `IGNORE link2` |

---

## Expected Output

```
FOLLOW link1
IGNORE link2
```
