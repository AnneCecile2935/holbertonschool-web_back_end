#!/usr/bin/env python3
"""
Module pagination

Ce module contient la classe Server et la fonction index_range
pour gérer la pagination d'un dataset chargé à partir d'un fichier CSV
contenant des données sur les prénoms populaires de bébés.
"""
import csv
from typing import List


def index_range(page, page_size):
    """
    Calcule la plage d'indices (start, end) correspondant à une page
    spécifique et à une taille de page donnée.

    Paramètres:
    -----------
    page : int
        Numéro de la page (1-indexé).
    page_size : int
        Nombre d'éléments par page.

    Retourne:
    ---------
    tuple (int, int)
        Tuple contenant l'indice de début (inclusif) et l'indice de fin
        (exclusif)
        pour découper une liste correspondant à la page demandée.

    Exemple:
    --------
    >>> index_range(1, 10)
    (0, 10)
    """
    # calcul indice de début
    start = (page - 1) * page_size
    # calcul indice de fin
    end = page * page_size
    # return tuple stard, end
    return (start, end)


class Server:
    """
    Classe Server qui pagine un dataset de prénoms populaires
    chargé depuis un fichier CSV.

    Attributs:
    ----------
    DATA_FILE : str
        Chemin vers le fichier CSV des données.
    __dataset : List[List] | None
        Cache des données chargées depuis le CSV.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialise une instance de Server avec dataset vide (None).
        """
        self.__dataset = None   # Le dataset n'est pas encore chargé

    def dataset(self) -> List[List]:
        """
        Charge et met en cache le dataset depuis le fichier CSV,
        en ignorant la première ligne (en-tête).

        Retourne:
        ---------
        List[List]
            Liste des lignes de données, chaque ligne étant une liste de
            valeurs.
        """
        # Si le dataset n'a pas encore été chargé
        if self.__dataset is None:
            # Ouvre le fichier CSV
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                # Transforme toutes les lignes du CSV en liste de listes
                dataset = [row for row in reader]
            # Ignore la première ligne (en-tête) et stocke les données
            self.__dataset = dataset[1:]

        # Retourne les données mises en cache
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Récupère une page du dataset, selon le numéro de page et la taille
        de page.

        Paramètres:
        -----------
        page : int
            Numéro de la page à récupérer (1-indexé).
        page_size : int
            Nombre d'éléments par page.

        Retourne:
        ---------
        List[List]
            La sous-liste correspondant à la page demandée.
            Retourne une liste vide si la page est hors limites.

        Lève:
        -----
        AssertionError
            Si `page` ou `page_size` ne sont pas des entiers > 0.
        """
        # Vérifie que page est un entier strictement positif
        assert isinstance(page, int) and page > 0
        # Vérifie que page_size est un entier strictement positif
        assert isinstance(page_size, int) and page_size > 0
        # Récupère les données
        data = self.dataset()
        # Utilise index_range pour obtenir les indices
        # de début et fin pour la pagination
        start, end = index_range(page, page_size)
        # Si l'indice de début est au-delà des données disponibles,
        # retourne une liste vide
        if start >= len(data):
            return []
        # Sinon retourne la tranche correspondant à la page demandée
        return data[start:end]
