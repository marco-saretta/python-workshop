---
layout: default
title: VS Code setup
parent: Base Setup
nav_order: 3
---

# VS Code Setup

Visual Studio Code is the editor we use in this course. It is free, widely used in industry, and has excellent Python support. This section walks through the interface, how to configure it for Python, and a set of recommended extensions and settings.

## Table of Contents

- [The Interface](#the-interface)
  - [Editor](#editor)
  - [Sidebar and Explorer](#sidebar-and-explorer)
  - [Terminal](#terminal)
  - [Command Palette](#command-palette)
- [Python Interpreter](#python-interpreter)
  - [Setting the uv interpreter](#setting-the-uv-interpreter)
- [Recommended Extensions](#recommended-extensions)
- [Recommended Settings](#recommended-settings)

---

## The Interface

### Editor

The editor is the main area where you write code. You can have multiple files open as tabs. VS Code provides syntax highlighting, autocompletion, and inline error markers as you type.

A few things worth knowing from the start:

- Click any file in the sidebar to open it in the editor
- Split the editor with `Ctrl+\` (Mac: `Cmd+\`) to view two files side by side
- `Ctrl+P` (Mac: `Cmd+P`) opens a quick file search, which is faster than navigating folders manually

### Sidebar and Explorer

The left sidebar contains several panels. The most important one is the **Explorer** (the pages icon at the top), which shows your project folder as a file tree. You can open, rename, create, and delete files from here.

Other panels you will use regularly are the **Source Control** panel (the branch icon) for Git operations, and the **Extensions** panel (the puzzle piece icon) for installing extensions.

### Terminal

VS Code has a built-in terminal. Open it with `` Ctrl+` `` (the backtick key, top-left of most keyboards) or via the menu at **Terminal > New Terminal**.

The terminal opens at the root of your project folder automatically, which means you can run `git`, `uv`, `ruff`, and `python` commands without navigating anywhere. You can open multiple terminal tabs side by side, which is useful for running a script in one pane while monitoring output in another.

> **Important:** When you open a project that has a `.venv` folder, VS Code usually detects it and activates the virtual environment automatically in new terminals. You will see `(.venv)` at the start of the prompt. If it does not activate automatically, see the section below on setting the interpreter.

### Command Palette

The Command Palette is the fastest way to access any VS Code feature. Open it with `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`) and start typing what you want to do. Nearly every setting, action, and extension feature is reachable from here.

---

## Python Interpreter

VS Code needs to know which Python to use for your project: which interpreter to run, and where to find your installed packages. If you select the wrong one, imports will fail and autocompletion will not work correctly.

When you open a `.py` file, VS Code shows the current interpreter in the bottom-right corner of the status bar. It will say something like `Python 3.12.0` with a path next to it.

### Setting the uv interpreter

When working with a uv project, you want VS Code to use the Python inside your `.venv` folder, not the system Python.

1. Open the Command Palette (`Ctrl+Shift+P`)
2. Type `Python: Select Interpreter` and press Enter
3. A list of detected environments will appear. Look for the one that shows a path containing `.venv` inside your project folder, for example: `Python 3.12.0 ('.venv': venv) ./venv/bin/python`
4. Select it

If the `.venv` interpreter does not appear in the list, click **Enter interpreter path** and navigate manually to `.venv/bin/python` (Mac/Linux) or `.venv/Scripts/python.exe` (Windows).

Once set, VS Code uses that interpreter for running files, linting, and autocompletion. The status bar in the bottom right will update to confirm.

---

## Recommended Extensions

Install extensions by opening the Extensions panel (`Ctrl+Shift+X`) and searching by name.

**Python and code quality**

- **Python** (by Microsoft) — Required. Provides Python language support, the interpreter selector, debugging, and the test runner.
- **Pylance** (by Microsoft) — Highly recommended. Adds fast, intelligent autocompletion and type checking powered by Pyright.
- **Ruff** (by Astral Software) — Runs Ruff as you type and highlights issues inline. Pairs with the Ruff linter you installed earlier.

**Appearance**

- **One Dark Pro** — A dark theme based on the Atom editor's default theme. Clean and easy on the eyes for long sessions. After installing, apply it via `Ctrl+Shift+P` > `Color Theme`.
- **Material Icon Theme** — Replaces the default file icons with clear, colour-coded icons based on file type. Makes the Explorer sidebar much easier to scan.

**Productivity**

- **GitLens** — Enhances the built-in Git support. Shows who last changed each line of code inline, provides a detailed history view, and makes blame and diff workflows much easier.
- **indent-rainbow** — Colours each indentation level differently. Particularly helpful in Python where indentation is structural.
- **autoDocstring** — Generates a docstring template when you type `"""` inside a function. Saves time and encourages good documentation habits.

---

## Recommended Settings

**Font: JetBrains Mono**

JetBrains Mono is a free monospace font designed specifically for code. It improves readability with wider characters, increased letter-spacing, and ligatures that render symbols like `->`, `!=`, and `=>` as single glyphs.

Download it from [jetbrains.com/lp/mono](https://www.jetbrains.com/lp/mono/), install it on your system, then add the following to your VS Code settings:

1. Open the Command Palette > `Preferences: Open Settings (JSON)`
2. Add or update these entries:

```json
{
  "editor.fontFamily": "JetBrains Mono, monospace",
  "editor.fontSize": 13,
  "editor.fontLigatures": true,
  "editor.lineHeight": 1.6
}
```

**Other useful settings to add while you are there:**

```json
{
  "editor.formatOnSave": true,
  "editor.rulers": [79],
  "editor.wordWrap": "off",
  "files.trimTrailingWhitespace": true,
  "python.defaultInterpreterPath": ".venv/bin/python"
}
```

`editor.rulers` draws a faint vertical line at column 79 as a visual reminder of the PEP8 line length limit. `editor.formatOnSave` automatically runs the formatter every time you save a file, so you never have to think about it.