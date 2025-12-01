#!/usr/bin/env python3

"""
Module qui contient  une fonction permettant de
renvoyer un tuple de deux entier contenant la début et
la fin de la page qui contient l'information souhaiter.
Les information sont stocker dans une databass.css sur
des serveur de amazon.aws.
"""

def index_range(page: int, page_size: int) -> tuple:

    """
    Fonction qui prends en paramètres deux entier page et page_size
    pour retourner un tuple de deux élèments.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
