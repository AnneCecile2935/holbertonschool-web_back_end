#!/usr/bin/env python3
"""
Module contenant la fonction list_all qui liste tous les documents
d'une collection MongoDB.
"""


def list_all(mongo_collection):
    """
    Retourne une liste de tous les documents présents dans la collection
    MongoDB.

    Args:
        mongo_collection (pymongo.collection.Collection): La collection
        MongoDB.

    Returns:
        list: Liste des documents sous forme de dictionnaires.
              Retourne une liste vide si la collection est vide ou
              None est passé.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
