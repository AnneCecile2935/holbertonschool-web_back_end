#!/usr/bin/env python3
"""
Module de manipulation de chaînes.

Ce module fournit une fonction `concat` qui concatène deux chaînes de
caractères.
Il illustre l’usage des annotations de type et des docstrings en Python.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatène deux chaînes de caractères.

    Args:
        str1 (str): La première chaîne.
        str2 (str): La deuxième chaîne.

    Returns:
        str: Le résultat de la concaténation de str1 et str2.
    """
    return str1 + str2
