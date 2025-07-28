#!/usr/bin/env python3
"""
Module asynchrone qui attend un délai aléatoire.
"""
import asyncio  # permet d'écrire du code asynchrone
import random  # génère des nombres aléatoires


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un délai aléatoire entre 0 et max_delay secondes.

    Args:
        max_delay (int): Le délai maximum en secondes (par défaut 10).

    Returns:
        float: Le délai aléatoire utilisé.
    """
    delay = random.uniform(0, max_delay)
    # définition aléatoire du temps attente
    await asyncio.sleep(delay)
    # on dit au prog d'attendre, sans bloquer le reste
    return delay
