# Python Variable Annotations Project

## Overview

This project focuses on mastering **type annotations** in Python 3 to specify function signatures and variable types.
You will learn how to use type hints, duck typing, and how to validate your code using **mypy**.

## Learning Objectives

At the end of this project, you should be able to explain, without help:

- What **type annotations** are in Python 3
- How to use type annotations to specify function signatures and variable types
- The concept of **duck typing** in Python
- How to validate your annotated code with **mypy**

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Code will be tested on **Ubuntu 20.04 LTS** with **python3.9**
- Files must end with a newline
- First line of all files must be exactly:
  `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is **mandatory**
- Code must follow **pycodestyle** (version 2.5)
- All files must be executable
- File length will be checked with `wc`
- All modules, classes, and functions must be properly documented with docstrings that explain their purpose clearly (not just one word)

## Tasks

### 0. Basic annotations - add
Write a type-annotated function `add` that takes two floats `a` and `b` and returns their sum as a float.

### 1. Basic annotations - concat
Write a type-annotated function `concat` that takes two strings `str1` and `str2` and returns their concatenation.

### 2. Basic annotations - floor
Write a type-annotated function `floor` that takes a float `n` and returns its floor as an integer.

### 3. Basic annotations - to string
Write a type-annotated function `to_str` that takes a float `n` and returns its string representation.

### 4. Define variables
Define and annotate the following variables:
- `a`: int = 1
- `pi`: float = 3.14
- `i_understand_annotations`: bool = True
- `school`: str = "Holberton"

### 5. Complex types - list of floats
Write a type-annotated function `sum_list` that takes a list of floats and returns their sum as a float.

### 6. Complex types - mixed list
Write a type-annotated function `sum_mixed_list` that takes a list of ints and floats and returns their sum as a float.

### 7. Complex types - string and int/float to tuple
Write a type-annotated function `to_kv` that takes a string `k` and a number `v` (int or float), and returns a tuple `(k, v²)` where the second element is a float.

### 8. Complex types - functions
Write a type-annotated function `make_multiplier` that takes a float multiplier and returns a function that multiplies a float by this multiplier.

### 9. Let's duck type an iterable object
Annotate the function `element_length` which takes an iterable of sequences and returns a list of tuples containing each element and its length.

---

## Example Usage

```python
#!/usr/bin/env python3
add = __import__('0-add').add
print(add(1.1, 2.2))  # 3.3
print(add.__annotations__)  # {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
