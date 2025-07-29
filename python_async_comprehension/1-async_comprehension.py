#!/usr/bin/env python3
"""
Module qui collecte 10 nombres générés de façon asynchrone.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Utilise une compréhension asynchrone pour récupérer 10 nombres aléatoires
    depuis async_generator.

    Returns:
        List[float]: Une liste de 10 nombres flottants.
    """
    return [i async for i in async_generator()]
