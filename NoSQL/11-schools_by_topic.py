#!/usr/bin/env python3

"""
Module python qui contient une fonction qui permet
renvoyer une listes d'école
"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):

    """
    retourne la liste des écoles qui possède la particularité
    d'avoir un sujet original
    """

    return mongo_collection.find({'topics': topic})
