#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page of data starting from the given index,
        resilient to deletions in the dataset.
        """
        # Vérifie que l'index est un entier positif ou nul
        assert isinstance(index, int) and index >= 0
        # Récupère le dataset indexé
        # (un dictionnaire index -> ligne de données)
        indexed_data = self.indexed_dataset()
        # Vérifie que l'index demandé est inférieur
        # à la taille du dataset indexé
        assert index < len(indexed_data)

        data = []   # Liste qui contiendra la page de données à retourner
        current_index = index  # Position courante dans le dataset indexé

        # Tant que la page n'a pas atteint la taille souhaitée
        # et que l'index courant est inférieur
        # à la plus grande clé de indexed_data + 1
        while (len(data) < page_size and
                current_index < max(indexed_data.keys()) + 1):
            # Si l'index courant existe dans le dataset
            # (il peut manquer à cause des suppressions)
            if current_index in indexed_data:
                # Ajoute la ligne correspondante à la page de données
                data.append(indexed_data[current_index])
            # Passe à l'index suivant (pour gérer les "trous" dans les données)
            current_index += 1
        # Retourne un dictionnaire avec :
        # - l'index de départ de cette page,
        # - la liste des données récupérées,
        # - la taille réelle de la page
        # (peut être inférieure à page_size si peu de données restantes),
        # - et le prochain index à utiliser pour la page suivante
        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current_index
        }
