#!/usr/bin/env python3
"""
Module de transformation clé-valeur.

Ce module fournit une fonction `to_kv` qui prend une clé de type chaîne
et une valeur numérique (int ou float), et retourne un tuple contenant
la clé et le carré de la valeur, converti en float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Retourne un tuple contenant une chaîne et le carré de la valeur numérique.

    Args:
        k (str): Une chaîne de caractères représentant une clé.
        v (Union[int, float]): Une valeur numérique (entier ou flottant).

    Returns:
        Tuple[str, float]: Un tuple avec la chaîne d'origine et le carré
                           de la valeur, converti en float.
    """
    return (k, float(v**2))
