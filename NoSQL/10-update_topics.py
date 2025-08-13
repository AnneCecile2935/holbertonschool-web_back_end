#!/usr/bin/env python3
"""
Module pour mettre à jour la liste des topics d'un document école
dans une collection MongoDB
en fonction du nom de l'école.
"""


def update_topics(mongo_collection, name, topics):
    """
    Met à jour le champ 'topics' du document dont le nom est `name`
    dans la collection mongo_collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
        La collection MongoDB.
        name (str): Nom de l’école à mettre à jour.
        topics (list of str): Nouvelle liste des topics.

    Returns:
        pymongo.results.UpdateResult: Résultat de l’opération de mise à jour.
    """
    filter = {"name": name}
    new_values = {"$set": {"topics": topics}}
    result = mongo_collection.update(filter, new_values)
    return result
