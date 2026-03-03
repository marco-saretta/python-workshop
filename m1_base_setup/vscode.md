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


## General configuration
![vs_code](Figures/vs_code.png)

### Terminal

Set bash as default terminal

### Interface settings

Open the settings:

- Editor: Cursor Smooth Caret Animation --> On
- Editor: Cursor Blinking --> Expand

### Font

**Font: JetBrains Mono**

JetBrains Mono is a free monospace font designed specifically for code. Download it from [jetbrains.com/lp/mono](https://www.jetbrains.com/lp/mono/), install it on your system, then add the following to your VS Code settings:

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

`editor.rulers` draws a faint vertical line at column 79 as a visual reminder of the PEP8 line length limit. `editor.formatOnSave` automatically runs the formatter every time you save a file, so you never have to think about it.

### Python Interpreter

When working with a uv project, you want VS Code to use the Python inside your `.venv` folder, not the system Python.

1. Open the Command Palette (`Ctrl+Shift+P`)
2. Type `Python: Select Interpreter` and press Enter
3. Type `.venv\Scripts\python.exe` (Windows).

Once set, VS Code uses that interpreter for running files, linting, and autocompletion. The status bar in the bottom right will update to confirm.

## Recommended Extensions

Install extensions by opening the Extensions panel (`Ctrl+Shift+X`) and searching by name.

**Python and code quality**

- **Python** (by Microsoft) - Required. Provides Python language support, the interpreter selector, debugging, and the test runner.
- **Pylance** (by Microsoft) - Highly recommended. Adds fast, intelligent autocompletion and type checking powered by Pyright.
- **Ruff** (by Astral Software) - Runs Ruff as you type and highlights issues inline. Pairs with the Ruff linter you installed earlier.

**Appearance**

- **One Dark Pro** - A dark theme based on the Atom editor's default theme. Clean and easy on the eyes for long sessions. After installing, apply it via `Ctrl+Shift+P` > `Color Theme`.
- **Material Icon Theme** - Replaces the default file icons with clear, colour-coded icons based on file type. Makes the Explorer sidebar much easier to scan.

**Productivity**

- **GitLens** - Enhances the built-in Git support. Shows who last changed each line of code inline, provides a detailed history view, and makes blame and diff workflows much easier.
- **indent-rainbow** - Colours each indentation level differently. Particularly helpful in Python where indentation is structural.
- **autoDocstring** - Generates a docstring template when you type `"""` inside a function. Saves time and encourages good documentation habits.
