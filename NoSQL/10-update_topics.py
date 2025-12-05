#!/usr/bin/env python3

"""
Module python qui contient une fonction qui permet
de modifier les valeurs présente dans un document de la
base de donée.
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):

    """
    Fonction qui permet de mettre à jour une valeurs
    présente dans la db.
    Prends en arguments :
        le nom --> string
        topics --> list de strings
    """

    if not isinstance(topics, list):
        raise TypeError("Erreur de type")

    result = mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
    return result.modified_count
