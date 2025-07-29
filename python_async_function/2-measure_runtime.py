#!/usr/bin/env python3
"""
Module de mesure de performance asynchrone.

Ce module utilise la fonction `wait_n` pour exécuter plusieurs appels
asynchrones et calcule le temps moyen d'exécution par appel.
"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps moyen d'exécution d'un appel à wait_n.

    Args:
        n (int): Le nombre de fois que la coroutine `wait_random`
        sera lancée via `wait_n`.
        max_delay (int): Le délai maximum (en secondes) pour chaque
        attente aléatoire.

    Returns:
        float: Le temps moyen d'exécution par appel (en secondes).
    """
    # On enregistre le temps de départ avec haute précision
    start = time()

    # Exécution de la coroutine `wait_n` de façon synchrone dans l'event loop
    run(wait_n(n, max_delay))

    # Temps après exécution
    end = time()

    # Temps total écoulé
    total_time = end - start

    # Temps moyen par appel
    return total_time / n
