#!/usr/bin/env python3
"""
Module de calcul simple.

Ce module contient une fonction `add` qui permet de calculer la somme
de deux nombres à virgule flottante (float). Il illustre l'utilisation
des annotations de type et des docstrings en Python.
"""


def add(a: float, b: float) -> float:
    """
    Calcule la somme de deux nombres flottants.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: La somme de a et b.
    """
    return a + b
