---
layout: default
title: Package Management with uv
parent: Base Setup
nav_order: 2
---

# Package Management with uv

Every Python project needs a way to manage its dependencies: the external libraries your code relies on. This section introduces **uv**, the tool we use in this course, explains the concept of virtual environments, and briefly covers alternatives like Conda and Pixi.

## Table of Contents

- [The Problem uv Solves](#the-problem-uv-solves)
- [uv vs Conda](#uv-vs-conda)
- [Virtual Environments and .venv](#virtual-environments-and-venv)
  - [Activating a virtual environment](#activating-a-virtual-environment)
- [Core uv Commands](#core-uv-commands)
  - [uv init](#uv-init)
  - [uv add](#uv-add)
  - [uv sync](#uv-sync)
- [The pyproject.toml File](#the-pyprojecttoml-file)
- [A Note on Pixi](#a-note-on-pixi)
- [Exercise](#exercise)



## The Problem uv Solves

When you work on multiple Python projects, they will often require different versions of the same library. Project A might need `pandas 1.5`, while Project B needs `pandas 2.1`. If you install everything globally, these versions clash and eventually break each other.

The standard solution is to give each project its own isolated Python environment with its own set of packages. **uv** is a modern tool that handles this cleanly and very quickly. It manages your Python version, your virtual environment, and your dependencies all in one place.

uv is written in Rust, which makes it substantially faster than older tools like pip or conda for installing packages.



## uv vs Conda

You may have used **Conda** (or its smaller variant, Miniconda) before. Both tools solve the same problem — isolated environments with specific dependencies — but they take a different approach.

| | uv | Conda |
|---|---|---|
| Language focus | Python only | Python, R, C libs, and more |
| Speed | Very fast | Slower |
| Environment location | Inside your project folder (`.venv`) | Centralised in `~/miniconda3/envs/` |
| Dependency file | `pyproject.toml` | `environment.yml` |
| Package source | PyPI | Conda channels (conda-forge, etc.) |
| Best for | Python projects, web, data pipelines | Scientific computing, mixed-language stacks |

The key practical difference is where the environment lives. With Conda, all environments are stored in a single central directory on your machine, separate from your project. With uv, the environment sits directly inside your project folder in a folder called `.venv`. This makes it obvious what belongs to what, and it travels with your project.

For this course, we use uv. If you come from a Conda background, the concepts are the same and the transition is straightforward.



## Virtual Environments and .venv

A **virtual environment** is an isolated copy of Python with its own installed packages, separate from the global Python on your system. When a virtual environment is active, any `python` or `pip` command you run uses that environment, not the system one.

When you create a project with uv, it creates a `.venv` folder inside your project directory:

```
my-project/
    .venv/          <- the virtual environment lives here
        bin/
            python
            pip
            activate
        lib/
            python3.12/
                site-packages/   <- installed packages go here
    src/
    pyproject.toml
```

The Python executable inside `.venv/bin/python` is the one your project uses. Your installed packages go into `.venv/lib/`. Nothing touches the system Python.

Because `.venv` is just a folder inside your project, you always know exactly where it is. If something goes wrong, you can delete it and recreate it in seconds with `uv sync`.

> **Note:** `.venv` should be added to your `.gitignore`. You never commit the environment itself to Git, only the `pyproject.toml` that describes it. Anyone who clones your repo can recreate the exact environment by running `uv sync`.

### Activating a virtual environment

Before you can use the environment in your terminal, you need to activate it. Activation updates your shell so that `python` points to `.venv/bin/python` instead of the system Python.

**On Mac and Linux:**

```bash
source .venv/bin/activate
```

**On Windows (Git Bash):**

```bash
source .venv/Scripts/activate
```

**On Windows (Command Prompt):**

```bash
.venv\Scripts\activate.bat
```

Once activated, your terminal prompt changes to show the environment name:

```bash
(my-project) $
```

To deactivate and return to the system Python:

```bash
deactivate
```

> **Tip:** Most code editors including VS Code detect `.venv` automatically and activate it for you in the integrated terminal. You may not need to activate manually when working inside the editor.



## Core uv Commands

### uv init

`uv init` creates a new project folder with the standard structure and files.

```bash
uv init my-project
cd my-project
```

This creates:

```
my-project/
    .python-version     <- pins the Python version
    pyproject.toml      <- project metadata and dependencies
    README.md
    src/
        my_project/
            __init__.py
```

uv also creates a `.venv` folder and installs the base Python version automatically. You are ready to start adding packages immediately.

If you want to initialise uv inside an existing folder instead of creating a new one:

```bash
cd existing-folder
uv init
```

### uv add

`uv add` installs a package into your project and records it in `pyproject.toml`.

```bash
uv add requests
uv add pandas numpy
uv add pytest --dev
```

The `--dev` flag marks a package as a development dependency: something needed for testing or tooling but not for running the project in production (e.g., pytest, ruff, black).

After running `uv add`, two things happen: the package is installed into `.venv`, and `pyproject.toml` is updated to record the new dependency. You should commit `pyproject.toml` to Git so others can reproduce your environment.

### uv sync

`uv sync` reads `pyproject.toml` and installs all the listed dependencies into `.venv`. It is the command you run after cloning a project to get the environment set up.

```bash
uv sync
```

If `.venv` does not exist yet, uv creates it. If packages are already installed but out of date with `pyproject.toml`, uv updates them. If a package is installed but no longer listed in `pyproject.toml`, uv removes it.

This makes `uv sync` the single source of truth: what is in `pyproject.toml` is exactly what ends up in `.venv`.



## The pyproject.toml File

`pyproject.toml` is the central configuration file for your project. It replaces the older `requirements.txt` and `setup.py` approaches and is the current standard for Python projects.

A typical file looks like this:

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "A short description of the project"
requires-python = ">=3.11"

dependencies = [
    "pandas>=2.0",
    "requests>=2.28",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.4",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

The `dependencies` list is what `uv add` writes to when you install a package. The `requires-python` field pins the minimum Python version. The `dev` optional group is what gets populated with `uv add --dev`.

You can also configure tools like Ruff directly in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
```

This keeps all project configuration in a single file rather than scattered across `.flake8`, `setup.cfg`, and other tool-specific files.



## A Note on Pixi

**Pixi** is a newer package manager built on top of the Conda ecosystem. It uses a `pixi.toml` file (similar to `pyproject.toml`) and supports multiple languages and platforms from one configuration.

Pixi is worth knowing about if you work in environments that mix Python with compiled software (like geospatial libraries, CUDA, or R) where Conda channels are the only reliable source of packages.

What Pixi does well: it handles complex mixed-language dependency stacks cleanly, it is faster than traditional Conda, and its lockfile approach (similar to uv) gives you reproducible environments.

What Pixi cannot do: it does not integrate as seamlessly into the Python-only tooling ecosystem. Features like editable installs, Python packaging, and publishing to PyPI are less mature than in uv. If your project is purely Python, uv is simpler and better supported.

For this course, we use uv. Pixi is mentioned here so you recognise it if you encounter it in the wild, particularly in scientific or research computing contexts.



## Exercise

In this exercise you will create a new project with uv, add a dependency, write a small script, and run it inside the virtual environment.

**Step 1: Install uv**

```bash
pip install uv
```

Verify it is installed:

```bash
uv --version
```

**Step 2: Create a new project**

```bash
uv init workshop-project
cd workshop-project
```

Look at what was created:

```bash
ls -la
```

Open `pyproject.toml` and read through it. Notice the `dependencies` field is currently empty.

**Step 3: Add a dependency**

```bash
uv add requests
```

Open `pyproject.toml` again. Notice that `requests` has been added to the `dependencies` list automatically.

Now look inside `.venv`:

```bash
ls .venv/lib/
```

You can see that packages have been installed there, not somewhere in a global Miniconda directory.

**Step 4: Activate the environment**

On Mac/Linux:

```bash
source .venv/bin/activate
```

On Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

Your prompt should now show the environment name. Verify which Python is being used:

```bash
which python
# should point to .venv/bin/python, not /usr/bin/python or similar
```

**Step 5: Write and run a small script**

Create a file called `main.py` in the project folder:

```python
import requests

response = requests.get("https://httpbin.org/get")
print("Status code:", response.status_code)
print("Your IP:", response.json()["origin"])
```

Run it:

```bash
python main.py
```

**Step 6: Simulate a fresh clone**

This step shows why `uv sync` matters. Delete the `.venv` folder to simulate what it would be like if a colleague cloned your repo:

```bash
deactivate
rm -rf .venv
```

Now recreate the environment from `pyproject.toml` alone:

```bash
uv sync
source .venv/bin/activate
python main.py
```

Everything works again, from a single file. This is the core workflow you will use on every project.

**What you practiced:**

- Creating a project with `uv init`
- Adding a dependency with `uv add` and seeing `pyproject.toml` update
- Locating the `.venv` folder inside the project
- Activating and deactivating the environment
- Recreating the environment from scratch with `uv sync`