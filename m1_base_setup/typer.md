---
layout: default
title: Typer
parent: Base Setup
nav_order: 4
---

# Typing and Type Hints

Python is a dynamically typed language, which means variables do not have a fixed type and the interpreter figures out types at runtime. This is flexible and quick to write, but it makes code harder to read, harder to debug, and harder to refactor safely in larger projects.

**Type hints** let you annotate your code with the expected types of variables, function arguments, and return values. Python does not enforce them at runtime, but editors, linters, and type checkers like Pylance use them to catch errors before you run anything.

This section covers the basics of typing in Python, good habits to build from the start, and where type hints connect to PEP8.

## Table of Contents

- [Basic Type Hints](#basic-type-hints)
- [Function Signatures](#function-signatures)
- [Common Types from the typing Module](#common-types-from-the-typing-module)
- [When to Use Type Hints](#when-to-use-type-hints)
- [Type Hints and PEP8](#type-hints-and-pep8)
- [Typer: Building CLIs with Types](#typer-building-clis-with-types)
- [Exercise](#exercise)

---

## Basic Type Hints

You annotate a variable by adding a colon and the type after the name:

```python
name: str = "Alice"
age: int = 30
score: float = 92.5
is_active: bool = True
```

This tells anyone reading the code (and any editor or type checker) exactly what kind of value is expected. If you later do something like `age = "thirty"`, Pylance will immediately flag it as a type error.

For variables that might be `None`, use `Optional` or the shorthand `| None` (available from Python 3.10):

```python
from typing import Optional

nickname: Optional[str] = None  # older style, works in all versions
nickname: str | None = None     # modern style, Python 3.10+
```

---

## Function Signatures

Function annotations are where type hints provide the most value. Annotate both the parameters and the return type:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


def add(a: int, b: int) -> int:
    return a + b


def find_user(user_id: int) -> dict | None:
    # Returns a user dict if found, None if not
    ...
```

The `-> type` part is the return type annotation. Use `-> None` for functions that do not return a value:

```python
def log_message(message: str) -> None:
    print(f"[LOG] {message}")
```

When your editor knows the return type of a function, it can autocomplete attributes and methods on whatever that function returns. This is one of the biggest practical benefits of type hints.

---

## Common Types from the typing Module

For more complex types, import from the `typing` module. In Python 3.9+, some of these are available as built-in generics, which is the preferred style in new code.

```python
from typing import List, Dict, Tuple, Set  # older style, still works

# Modern style (Python 3.9+), no import needed
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 95, "Bob": 82}
coordinates: tuple[float, float] = (48.8566, 2.3522)
unique_tags: set[str] = {"python", "data"}
```

For functions that accept more than one possible type:

```python
def process(value: int | str) -> str:
    return str(value)
```

For collections where items can be anything:

```python
from typing import Any

def log(data: Any) -> None:
    print(data)
```

Use `Any` sparingly. It effectively disables type checking for that variable, which defeats the purpose.

---

## When to Use Type Hints

You do not need to annotate every single variable in every file. The goal is to make code clearer, not to clutter it. A practical rule of thumb:

**Always annotate:** function parameters and return types. These are the contract between the caller and the function and carry the most value.

**Annotate when it adds clarity:** variables whose type is not obvious from the assignment. `count: int = 0` is redundant since `0` is clearly an int. But `result: dict[str, list[int]] = {}` is genuinely helpful.

**Skip when it is obvious:** `x = 10`, `name = "Alice"`, `is_done = True`. The type is clear from the value.

```python
# Redundant - type is obvious
name: str = "Alice"

# Useful - type is not obvious from context
user_cache: dict[int, dict] = {}

# Always annotate function signatures
def calculate_average(values: list[float]) -> float:
    return sum(values) / len(values)
```

---

## Type Hints and PEP8

PEP8 has specific formatting rules for type annotations. These are largely what you would expect from PEP8's general spacing rules, but worth stating explicitly.

**No space before the colon, one space after:**

```python
# Correct
name: str = "Alice"
def greet(name: str) -> str:

# Wrong
name :str = "Alice"
name : str = "Alice"
def greet(name:str)->str:
```

**Spaces around `|` in union types:**

```python
# Correct
def find(user_id: int) -> dict | None:

# Wrong
def find(user_id: int) -> dict|None:
```

**Return type annotation on the same line as `def`:** if the signature is short enough to fit within 79 characters, keep it on one line. For long signatures, you may break across lines:

```python
def process_records(
    records: list[dict],
    output_path: str,
    verbose: bool = False,
) -> list[str]:
    ...
```

**Imports for typing go with the other imports at the top of the file**, grouped after the standard library imports:

```python
import os
from typing import Optional
```

Ruff will flag most of these violations automatically and can fix spacing issues around colons and operators.

---

## Typer: Building CLIs with Types

**Typer** is a library for building command-line interfaces that uses type hints as its entire configuration mechanism. Instead of manually parsing `sys.argv` or configuring argparse, you write a normal typed Python function and Typer handles the rest.

Install it:

```bash
uv add typer
```

A minimal example:

```python
import typer

app = typer.Typer()


@app.command()
def greet(name: str, count: int = 1) -> None:
    for _ in range(count):
        print(f"Hello, {name}!")


if __name__ == "__main__":
    app()
```

Run it:

```bash
python main.py Alice
# Hello, Alice!

python main.py Alice --count 3
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

python main.py --help
# Usage: main.py [OPTIONS] NAME
# ...
```

Typer reads the type of each parameter (`str`, `int`, `bool`, etc.) and automatically validates the input, converts it to the right type, and generates a `--help` message. The type hints you write for clarity also drive the entire CLI behaviour, with no extra configuration.

This is a good example of why typing is not just a documentation practice. When libraries are built around type annotations, the hints you write carry real functional weight.

---

## Exercise

**Part 1: Add type hints to a function**

Take the following untyped code and add complete type hints to all function signatures and key variables:

```python
def filter_scores(scores, threshold):
    passing = []
    for score in scores:
        if score >= threshold:
            passing.append(score)
    return passing


def build_report(name, scores):
    average = sum(scores) / len(scores)
    return {
        "name": name,
        "scores": scores,
        "average": average,
        "passed": filter_scores(scores, 60),
    }
```

After adding hints, run Pylance (or `mypy` if installed) to confirm there are no type errors.

**Part 2: Build a small Typer CLI**

Create a file called `cli.py` that accepts two arguments from the command line: a name (string) and an age (integer). Print a formatted message like `Alice is 30 years old.`

Make it runnable:

```bash
python cli.py Alice 30
```

Add a `--shout` flag (boolean, default False) that prints the message in uppercase when provided:

```bash
python cli.py Alice 30 --shout
# ALICE IS 30 YEARS OLD.
```

Run `python cli.py --help` and confirm that Typer has generated a sensible help message automatically.