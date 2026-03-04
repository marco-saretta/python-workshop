---
layout: default
title: src vs Flat Layout
parent: Python Templates
nav_order: 2
---

# src vs Flat Layout

# "src" vs Flat Layout in Python Projects

When organizing Python projects, two common structures are used: **flat layout** and **`src` layout**.

## Flat Layout

All code files are stored at the top level of the project folder.

```
myproject/
│
├── main.py
├── utils.py
└── tests/
    └── test_utils.py
```

**Pros:**
- Simple and easy for small projects.
- No need for additional configuration.

**Cons:**
- Imports can break when the project is installed as a package.
- Code may accidentally import from the wrong place during testing.

## `src` Layout

Your package code lives inside a separate `src/` folder:
```
myproject/
│
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
└── tests/
    └── test_utils.py
```

**Pros:**
- Prevents import confusion (you must install the package before importing).
- Mirrors how projects will look when distributed (via pip, for example).

**Cons:**
- Slightly more setup (e.g., need to run `pip install -e .` for editable installs).

## Which Should You Use?

- Use **flat layout** for short scripts and quick projects.
- Use **`src` layout** for any package meant to be reused or shared — especially if uploaded to PyPI or installed locally.
