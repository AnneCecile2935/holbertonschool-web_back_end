# Python Async Function Project

## Description

This project aims to teach you how to master asynchronous programming in Python using the `async` and `await` syntax along with the `asyncio` module. You will learn how to run asynchronous programs, execute multiple coroutines concurrently, create asyncio tasks, and handle random delays using the `random` module.

## Learning Objectives

By the end of this project, you will be able to:

- Understand and use the `async` and `await` syntax in Python.
- Run an asynchronous program with the `asyncio` module.
- Run multiple coroutines concurrently.
- Create and manage asyncio tasks (`asyncio.Task`).
- Use the `random` module to generate random delays.
- Annotate your functions and coroutines with Python types.
- Follow best practices for documentation and styling (PEP8).

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- Allowed editors: vi, vim, emacs
- Adhere to pycodestyle standard (version 2.5.x)
- All files must be executable and start with the line:
  `#!/usr/bin/env python3`
- All modules, functions, and coroutines must be documented and type-annotated.

## Task Summary

| Task | Description |
|-------|-------------|
| 0 - The basics of async | Write an asynchronous coroutine `wait_random(max_delay=10)` that waits for a random delay between 0 and `max_delay` seconds and returns the delay. |
| 1 - Concurrent coroutines | Write a coroutine `wait_n(n, max_delay)` that runs `wait_random` `n` times concurrently and returns a list of delays sorted in ascending order (without using `sort()`). |
| 2 - Measure the runtime | Write a function `measure_time(n, max_delay)` that measures and returns the average execution time of `wait_n(n, max_delay)`. |
| 3 - Tasks | Write a function `task_wait_random(max_delay)` that returns an asyncio Task executing `wait_random(max_delay)`. |
| 4 - Tasks (continued) | Modify `wait_n` to use `task_wait_random` and rename it `task_wait_n(n, max_delay)`. |

## Example Usage

```bash
$ ./0-basic_async_syntax.py
9.034261504534394
1.6216525464615306
10.634589756751769

$ ./1-concurrent_coroutines.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]

$ ./2-measure_runtime.py
1.759705400466919

$ ./3-tasks.py
<class '_asyncio.Task'>

$ ./4-tasks.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
