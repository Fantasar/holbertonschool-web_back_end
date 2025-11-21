#!/usr/bin/env python3
from typing import Callable

"""
Module qui permet de réaliser une multiplication
avec un nombre flottant.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    """
    Fonctions qui prends la valeurs de la variable
    multiplier et retourne le resultat.
    """

    def multiply(value: float) -> float:

        """
        Fonctions pour multiplier une
        valeur par le multiplicateur.
        """

        return value * multiplier

    return multiply
