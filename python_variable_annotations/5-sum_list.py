#!/usr/bin/env python3
"""
Module pour la manipulation de listes de nombres flottants.

Ce module fournit une fonction `sum_list` qui calcule la somme
des éléments d'une liste de floats, avec annotations de type
et documentation complète.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calcule la somme des éléments d'une liste de floats.

    Args:
        input_list (List[float]): Une liste de nombres flottants.

    Returns:
        float: La somme des éléments de la liste.
    """
    return sum(input_list)
