#!/usr/bin/env python3
"""
Module pagination

Ce module contient la classe Server et la fonction index_range
pour gérer la pagination d'un dataset chargé à partir d'un fichier CSV
contenant des données sur les prénoms populaires de bébés.
"""
import csv
import math
from typing import List, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retourne les informations de pagination sous forme de dictionnaire.

        Cette méthode réutilise `get_page` pour extraire les données d'une page
        et fournit des métadonnées utiles au format hypermedia.

        Paramètres
        ----------
        page : int, optionnel
            Numéro de la page à récupérer (1-indexé). Par défaut 1.
        page_size : int, optionnel
            Nombre d'éléments par page. Par défaut 10.

        Retourne
        --------
        dict
            Un dictionnaire contenant :
            - 'page_size' (int) : nombre d'éléments dans la page retournée
            (peut être inférieur à `page_size` si fin de dataset)
            - 'page' (int) : numéro de la page actuelle
            - 'data' (List[List]) : contenu de la page (lignes du dataset)
            - 'next_page' (int | None) : numéro de la page suivante,
            None si dernière page
            - 'prev_page' (int | None) : numéro de la page précédente,
            None si première page
            - 'total_pages' (int) : nombre total de pages dans le dataset

        Exemple
        -------
        >>> server.get_hyper(page=1, page_size=5)
        {
            'page_size': 5,
            'page': 1,
            'data': [...],
            'next_page': 2,
            'prev_page': None,
            'total_pages': 120
        }
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
