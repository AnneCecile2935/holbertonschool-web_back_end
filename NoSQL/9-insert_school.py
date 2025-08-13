#!/usr/bin/env python3
"""
Module pour insérer un document dans une collection MongoDB.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insère un nouveau document dans la collection mongo_collection
    avec les champs passés en kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection):
        La collection MongoDB.
        **kwargs: Champs et valeurs du document à insérer.

    Returns:
        ObjectId: L’_id du document inséré.
    """
    new_insert = mongo_collection.insert_one(kwargs)
    return new_insert.inserted_id
