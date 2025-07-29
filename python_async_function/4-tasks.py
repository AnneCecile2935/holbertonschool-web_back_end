#!/usr/bin/env python3
"""
Module qui exécute plusieurs fois task_wait_random et retourne les délais.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance n fois la fonction task_wait_random et retourne une liste triée
    des délais.

    Args:
        n (int): nombre d'exécutions.
        max_delay (int): délai max à transmettre à task_wait_random.

    Returns:
        List[float]: Liste des délais, triée par ordre croissant.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
