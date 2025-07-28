#!/usr/bin/env python3
"""
Module pour les opérations mathématiques simples.

Ce module fournit une fonction `floor` qui calcule le plancher
(définition mathématique : plus grand entier inférieur ou égal)
d'un nombre flottant donné.
"""


import math


def floor(n: float) -> int:
    """
    Retourne le plancher (floor) de la valeur flottante n.

    Args:
        n (float): Le nombre flottant dont on veut le plancher.

    Returns:
        int: Le plus grand entier inférieur ou égal à n.
    """
    return math.floor(n)
