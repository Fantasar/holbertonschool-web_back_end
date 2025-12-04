#!/usr/bin/env python3

"""
Module python qui contient une fonction pour inserer un nouveau
document dans une base de donée
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):

    """
    Fonction qui prends en argument deux paramètres et
    retourne un nouvelle id.
    """

    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
