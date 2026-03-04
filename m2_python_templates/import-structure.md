---
layout: default
title: Import Structure
parent: Python Templates
nav_order: 1
---

# Import Structure

Learning how to import files and scripts is essential to keep your code modular and reusable. Python uses the `import` statement to include code from other files or libraries.

## Basic Imports

If you have a file named `helpers.py` in the same directory:

```python
import helpers
helpers.greet_user("Alice")
```

You can import specific functions or classes:

```python
from helpers import greet_user
greet_user("Alice")
```

You can also rename imports for convenience:

```python
import helpers as hp
hp.greet_user("Alice")
```

## Importing from Subfolders

If your project has folders, Python treats them as *packages* when they contain an `__init__.py` file.

Example project structure:

```
project/
    app/
        __init__.py
        main.py
        utils.py
```

To import `utils` inside `main.py`:

```python
from app import utils
```

or

```python
from app.utils import some_function
```

## Managing Paths

If you need to import a file that’s not in your current directory, you can modify the Python path:

```python
import sys
sys.path.append('../path/to/module')
```

However, it’s usually better to organize your project so Python can find everything naturally by package imports.

{: .note }
Always keep your imports organized: standard libraries → third-party packages → your own modules.
