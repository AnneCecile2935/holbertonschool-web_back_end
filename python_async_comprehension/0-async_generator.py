#!/usr/bin/env python3
"""
Module contenant une coroutine génératrice asynchrone.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine qui génère 10 nombres flottants aléatoires entre 0 et 10,
    avec une pause de 1 seconde entre chaque.

    Returns:
        AsyncGenerator[float, None]: Générateur asynchrone de floats.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
