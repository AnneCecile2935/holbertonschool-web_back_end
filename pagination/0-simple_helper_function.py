#!/usr/bin/env python3
"""
Module pagination_utils

Ce module contient des fonctions utilitaires pour gérer la pagination
dans des listes ou d'autres structures de données indexables.
"""


def index_range(page, page_size):
    """
    Calcule la plage d'indices (start, end) correspondant à une page donnée
    et à une taille de page spécifiée.

    Les indices sont destinés à être utilisés pour découper une liste
    (par exemple list[start:end]).

    Paramètres:
    -----------
    page : int
        Le numéro de la page (1-indexé, donc la première page est page 1).
    page_size : int
        Le nombre d'éléments par page.

    Retourne:
    ---------
    tuple (int, int)
        Un tuple contenant l'indice de début (inclusif) et l'indice de fin
        (exclusif) correspondant à la plage des éléments pour la page demandée.

    Exemples:
    ---------
    >>> index_range(1, 10)
    (0, 10)
    >>> index_range(2, 10)
    (10, 20)
    """
    # calcul indice de début
    start = (page - 1) * page_size
    # calcul indice de fin
    end = page * page_size
    # return tuple stard, end
    return (start, end)
