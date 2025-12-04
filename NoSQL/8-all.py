#!/usr/bin/env python3

"""
Module Python qui contient une fonction pour pour lister
les documents présent dans la db de Mongos
"""

from pymongo import MongoClient

def list_all(mongo_collection):

    """
    Fonctions python qui prends en arguments une base de données
    Monogs et return la listes des documents présent à l'intérieur
    """
    try:
        return list(mongo_collection.find())
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return []
