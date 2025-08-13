#!/usr/bin/env python3
"""
Module 11-schools_by_topic

Ce module contient une fonction pour récupérer toutes les écoles
d'une collection MongoDB qui ont un topic spécifique dans leur liste de topics.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retourne la liste des écoles ayant un topic spécifique.

    Args:
        mongo_collection (pymongo.collection.Collection): La collection MongoDB
          contenant les écoles.
        topic (str): Le topic recherché dans la liste 'topics' de chaque école.

    Returns:
        list: Une liste de dictionnaires représentant les écoles qui
        contiennent le topic donné.
              Chaque dictionnaire correspond à un document MongoDB.

    Exemple:
        >>> schools = schools_by_topic(school_collection, "Python")
        >>> for school in schools:
        >>>     print(school.get("name"), school.get("topics"))
    """
    # Définition de la requête MongoDB :
    # On cherche tous les documents où la liste 'topics'
    # contient exactement la valeur de 'topic'
    query = {"topics": topic}
    # Exécution de la requête avec find()
    # find() renvoie un curseur qui peut être itéré pour obtenir les documents
    cursor = mongo_collection.find(query)
    # Transformation du curseur en liste pour pouvoir le retourner facilement
    results = list(cursor)
    # Retourne la liste des documents correspondant au topic
    return results
