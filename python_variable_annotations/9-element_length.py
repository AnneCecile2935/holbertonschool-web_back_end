#!/usr/bin/env python3
"""
Module de traitement de séquences itérables.

Ce module fournit une fonction `element_length` qui prend une collection
de séquences (listes, chaînes, tuples, etc.) et retourne une liste de
tuples contenant chaque séquence et sa longueur.
"""

from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calcule la longueur de chaque élément dans une collection de séquences.

    Args:
        lst (Iterable[Sequence]): Une collection d’objets de type séquence
                                  (par exemple : listes, tuples, chaînes).

    Returns:
        List[Tuple[Sequence, int]]: Une liste de tuples contenant chaque
                                    séquence et sa longueur.
    """
    return [(i, len[i]) for i in lst]
