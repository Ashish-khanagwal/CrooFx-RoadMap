# Understanding Symlinks

---

## 1️⃣ Beginner: What Is a Symlink?

A symlink (symbolic link) is like a **shortcut**.

```
repo/
 ├── src/
 │    └── main.py
 ├── shortcut -> src
```

That arrow means: `shortcut points to src`

So if you open:

```
repo/shortcut/main.py
```

You are actually opening:

```
repo/src/main.py
```

The file is not duplicated. It's just a **pointer**.

---

## 2️⃣ Real Computer Example

Your system might look like this:

```
repo/
 ├── venv/
 │    └── numpy -> /usr/lib/python3.11/site-packages/numpy
```

Here, `numpy` points to `/usr/lib/python3.11/site-packages/numpy`.

The real code lives **outside** your repo. The symlink just points there.

---

## 3️⃣ Why Symlinks Exist

1. **Dependency sharing** - virtualenv, node_modules, system libraries
2. **Storage efficiency** - no duplicate files
3. **Flexible directory structures** - tools can reuse files from other locations

---

## 4️⃣ Why Symlinks Are Dangerous for Scanners

Imagine this:

```
repo/
 ├── src/
 ├── evil_link -> /
```

`/` means the **entire filesystem**.

If your scanner follows that link, it suddenly scans:

```
/etc
/home
/usr
```

Which causes:

- Huge, uncontrolled scans
- Performance crashes
- Security issues
- Non-deterministic output

Infrastructure tools **must** prevent this.

---

## 5️⃣ The Three Possible Strategies

When a scanner encounters a symlink, it has three options:

### Strategy 1 - Ignore Them

```
skip symlinks
```

Simple, but loses dependency information.

### Strategy 2 - Always Follow Them

```
resolve every symlink
```

Very dangerous. ❌

### Strategy 3 - Controlled Policy ✅

```
follow only safe symlinks
```

This is what professional tools do. The scanner checks whether the symlink target stays **inside** the repo before following it.

# Symlink Policy & Detection in Python

---

## 6️⃣ What Is a Symlink Policy?

A symlink policy is simply a rule that answers:

> **When should we follow a symlink?**

Example policy:

```
Follow symlink ONLY if:
1. It stays inside the repo
2. It is a known dependency directory
```

Everything else is ignored.

---

## 7️⃣ Detecting a Symlink in Python

Pathlib gives us:

```python
p.is_symlink()
```

Example:

```python
from pathlib import Path

p = Path("link")

if p.is_symlink():
    print("This is a symlink")
```

---

## 8️⃣ Finding Where the Symlink Points

We use `.resolve()` to find the real location:

```python
target = p.resolve()
```

Example:

```
repo/link -> /usr/lib/python
```

`.resolve()` returns:

```
/usr/lib/python
```

Now you know exactly where the symlink is pointing.

---

## 9️⃣ Checking If the Target Is Inside the Repo

We must verify that the symlink stays inside the repo before following it:

```python
target.is_relative_to(repo_root)
```

| Result  | Meaning                                   |
| ------- | ----------------------------------------- |
| `True`  | ✅ Safe - target is inside the repo       |
| `False` | ❌ Dangerous - target is outside the repo |

---

## 🔟 Simple Symlink Policy Example

```python
Follow symlink if:
    target is inside repo
    OR
    target is inside virtualenv dependencies

Otherwise:
    ignore it
```

This keeps the scanner **bounded** - it only ever touches files you intended it to reach.
