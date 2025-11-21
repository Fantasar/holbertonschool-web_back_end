#!/usr/bin/env python3

from typing import Union, Tuple

"""
Module qui contient une fonction de 
types-annotée et renvoie un tuple.
"""

def to_kv(k: str, v: Union[int,float]) -> Tuple[str, float]:

    """
    Fonction qui prends en paramètres k et v
    pour return un tuple.
    """

    return (k, float(v * v))
