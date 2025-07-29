#!/usr/bin/env python3
"""
Module qui crée une tâche asyncio à partir de la coroutine wait_random.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Crée une tâche asyncio pour exécuter la coroutine wait_random.

    Args:
        max_delay (int): Délai maximum pour l'attente aléatoire.

    Returns:
        asyncio.Task: Tâche planifiée pour wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
