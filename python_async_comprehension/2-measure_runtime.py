#!/usr/bin/env python3
"""
Module qui mesure le temps d'exécution de 4 appels concurrents
à async_comprehension.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure le temps d'exécution pour 4 appels parallèles à async_comprehension.

    Returns:
        float: Durée totale en secondes.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
