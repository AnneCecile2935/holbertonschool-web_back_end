#!/usr/bin/env python3
"""
Module de calcul sur des listes de nombres mixtes.

Ce module contient une fonction `sum_mixed_list` qui prend en
entrée une liste composée d'entiers (`int`) et de nombres à virgule
flottante (`float`), et retourne leur somme en tant que `float`.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calcule la somme des éléments d'une liste contenant des floats et des
    entiers.

    Args:
        mxd_lst (List[Union[float, int]]): Une liste contenant des nombres
                                           entiers et/ou flottants.

    Returns:
        float: La somme des éléments de la liste, en tant que nombre flottant.
    """
    return sum(mxd_lst)
