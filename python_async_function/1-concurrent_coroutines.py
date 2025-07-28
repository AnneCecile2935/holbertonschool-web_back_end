#!/usr/bin/env python3
"""
Module asynchrone qui lance plusieurs appels à wait_random et
retourne les délais obtenus, triés par ordre croissant.
"""


from basic_async_syntax import wait_random
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance wait_random n fois de manière asynchrone et retourne
    la liste des délais obtenus, triée par ordre croissant.

    Args:
        n (int): nombre d’appels à wait_random.
        max_delay (int): valeur max pour chaque délai aléatoire.

    Returns:
        List[float]: liste des délais, en ordre croissant.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
