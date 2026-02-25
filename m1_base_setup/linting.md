---
layout: default
title: Code Style, Linting, and PEP8
parent: Base Setup
nav_order: 5
---

# Code Style, Linting, and PEP8

Writing code that works is only half the job. Code is read far more often than it is written, and messy, inconsistently styled code slows everyone down including your future self. This section covers why style matters, what PEP8 is, and how to use **Ruff** to automatically catch and fix style issues.

## Table of Contents

- [What is PEP8?](#what-is-pep8)
- [Key PEP8 Rules to Know](#key-pep8-rules-to-know)
- [What is a Linter?](#what-is-a-linter)
- [Ruff: The Linter We Use](#ruff-the-linter-we-use)
  - [Installing Ruff](#installing-ruff)
  - [Running Ruff](#running-ruff)
  - [What Ruff Fixes Automatically](#what-ruff-fixes-automatically)
  - [What Ruff Cannot Fix](#what-ruff-cannot-fix)
- [Linting Score](#linting-score)
- [Exercise](#exercise)


## What is PEP8?

**PEP8** is Python's official style guide. PEP stands for Python Enhancement Proposal, and number 8 is specifically the document that defines how Python code should be formatted and structured. It is not enforced by the Python interpreter (your code will still run if you ignore it), but it is the standard followed by virtually every serious Python project.

The full guide is available at [peps.python.org/pep-0008](https://peps.python.org/pep-0008/), but you do not need to memorise it. The important thing is to understand the principles and let tooling do most of the checking.


## Key PEP8 Rules to Know

**Naming conventions**

These are some of the most commonly violated rules, and also the ones no tool can fix for you automatically since only you know what something should be called.

| What | Convention | Example |
|------|-----------|---------|
| Variables and functions | `snake_case` | `user_name`, `calculate_sum()` |
| Classes | `PascalCase` | `UserAccount`, `DataProcessor` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES`, `DEFAULT_TIMEOUT` |
| Private attributes | leading underscore | `_internal_value` |

**Spacing**

- Put one space around operators: `x = 10` not `x=10`, `result = a + b` not `result=a+b`
- No space before a colon or comma, one space after: `def f(a, b):` not `def f(a ,b) :`
- Two blank lines between top-level functions and classes, one blank line between methods inside a class

**Line length**

Lines should not exceed **79 characters**. For docstrings and comments, the limit is 72 characters. Long lines are harder to read and make side-by-side diffs difficult.

**Imports**

Imports should be at the top of the file, one per line, and grouped in this order: standard library, third-party packages, local modules. Unused imports should be removed.

```python
# Good
import os
import sys

import requests

from myproject import utils

# Bad: multiple imports on one line, unused imports left in
import os, sys, json
```


## What is a Linter?

A **linter** is a tool that analyses your code without running it and reports problems. These problems can be style violations (like wrong spacing or naming), logic issues (like using a variable before it is defined), or code quality warnings (like importing something you never use).

The term comes from an early Unix tool called `lint` that checked C code for suspicious patterns. Today every major language has linters.

Linters give you a fast feedback loop. Instead of waiting for a code review or a runtime crash, you find problems the moment you save a file.


## Ruff: The Linter We Use

**Ruff** is a modern Python linter written in Rust. It is extremely fast (10 to 100 times faster than older Python linters), covers the same rules as tools like Flake8 and isort, and can automatically fix many issues.

We use Ruff in this course because it is the current industry standard for new projects.

### Installing Ruff

```bash
pip install ruff
```

You can verify the installation with:

```bash
ruff --version
```

### Running Ruff

To check a file for issues:

```bash
ruff check script.py
```

To check all Python files in the current directory and subfolders:

```bash
ruff check .
```

Example output:

```
script.py:6:2: E225 Missing whitespace around operator
script.py:10:1: E302 Expected 2 blank lines, got 1
script.py:14:5: F841 Local variable `x` is assigned to but never used
script.py:23:1: E501 Line too long (91 > 79 characters)
Found 4 errors.
```

Each line tells you the file, line number, column, the rule code (like `E225`), and a plain-English description. Rules starting with `E` and `W` come from PEP8. Rules starting with `F` come from Pyflakes and catch logical issues like unused variables or missing imports.

**Auto-fixing issues**

Ruff can automatically fix many of the problems it finds:

```bash
ruff check --fix script.py
```

After running this, check the file again to see what changed, and look at what remains for you to fix manually.

### What Ruff Fixes Automatically

Ruff can safely fix a wide range of formatting and style issues without any risk of changing how your code behaves. This includes things like removing trailing whitespace at the end of lines, adding or removing blank lines to meet spacing requirements, sorting and organising imports, removing unused imports, fixing whitespace around operators and after commas, and converting some redundant patterns (like `if x == True` to `if x`).

### What Ruff Cannot Fix

Ruff will report these issues but will not touch them, because fixing them would require understanding the intent of your code:

**Naming violations.** If you write `def Calculate_Sum()`, Ruff will tell you it should be `def calculate_sum()`, but it will not rename it. Renaming a function requires updating every place it is called, and Ruff does not make that kind of judgement. This is your job.

**Line length in complex expressions.** Ruff flags long lines but will not restructure your logic to make them shorter. You need to decide how to break it up sensibly.

**Logic and design issues.** Ruff does not know whether your variable names are meaningful, whether your function does too many things, or whether your structure is good. A linter checks style, not quality of thought.

**Docstrings.** Ruff can flag missing docstrings if you configure it to, but it cannot write them for you.

In short: Ruff handles the mechanical, objective stuff. The meaningful naming, the clear structure, the readable logic — that is still on you.


## Linting Score

Some projects and CI pipelines use a **linting score** to measure overall code quality. The most common tool for this is **Pylint**, which scores your code from 0 to 10 based on how many issues it finds relative to the size of the codebase.

```bash
pip install pylint
pylint script.py
```

Example output:

```
************* Module script
script.py:6:0: C0103: Variable name "x" doesn't conform to snake_case naming style (invalid-name)
script.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 4.50/10 (previous run: 3.20/10, +1.30)
```

A score of 10/10 means no issues were found. A score below 7 usually means the code has significant style or structural problems.

In this course we do not require a perfect score, but you should aim to understand every warning Pylint gives you and resolve the ones that matter. The score itself is less important than the habit of reading and acting on the feedback.

> **Note:** Ruff and Pylint overlap in some areas but are not the same tool. Ruff is faster and better suited to real-time checking during development. Pylint is more thorough and better suited to generating a quality report. You will often see both used together on professional projects.

---

## Exercise

The file `raw_script.py` contains a mix of PEP8 violations and style issues. Your task is to clean it up.

**Step 1: Run Ruff and read the output**

```bash
ruff check raw_script.py
```

Read through each reported issue. Make sure you understand what each rule code means before fixing anything. You can look up any rule code at [docs.astral.sh/ruff/rules](https://docs.astral.sh/ruff/rules/).

**Step 2: Let Ruff fix what it can**

```bash
ruff check --fix raw_script.py
```

Run `ruff check raw_script.py` again and compare the output. Notice which issues have been resolved and which ones remain.

**Step 3: Fix the remaining issues manually**

The issues that remain after `--fix` will mostly be naming violations. Go through the file and rename everything to follow PEP8 conventions. Remember:

- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Parameters: `snake_case`

When you rename something, make sure you update every place it is used in the file, not just the definition.

**Step 4: Address code quality issues**

Beyond naming, look at the file for these patterns and improve them:

- The `load_config` function opens a file but does not use a `with` statement. Rewrite it to use `with open(...) as f:` so the file is closed automatically even if an error occurs.
- The `process_list` function uses `for i in range(len(myList))` to loop with an index. Rewrite it to iterate directly over the list values.
- The `CheckPassword` method returns `True` or `False` from an `if/else`. Simplify it to a single return statement.

**Step 5: Run Pylint and read the score**

```bash
pylint raw_script.py
```

Note your starting score. Then run it again after your fixes and compare.

**What you are looking for in the final file:**

- `ruff check raw_script.py` reports zero errors
- All functions use `snake_case`, all classes use `PascalCase`
- No unused imports
- No lines over 79 characters
- `load_config` uses a `with` statement
- Pylint score is 7.0 or above