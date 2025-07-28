#!/usr/bin/env python3
"""
Module de création de fonctions multiplicatrices.

Ce module fournit une fonction `make_multiplier` qui retourne une fonction
capable de multiplier un nombre flottant par un multiplicateur donné.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Crée une fonction qui multiplie un float par le multiplicateur donné.

    Args:
        multiplier (float): Le coefficient par lequel les valeurs seront
        multipliées.

    Returns:
        Callable[[float], float]: Une fonction qui prend un float en entrée
        et retourne le résultat de sa multiplication par `multiplier`.
    """
    def multiply(n: float) -> float:
        """
        Multiplie la valeur `n` par le multiplicateur défini dans
        make_multiplier.

        Args:
            n (float): La valeur à multiplier.

        Returns:
            float: Le résultat de la multiplication.
        """
        return n * multiplier
    return multiply
