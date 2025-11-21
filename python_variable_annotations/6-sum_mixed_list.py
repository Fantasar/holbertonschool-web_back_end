#!/usr/bin/env python3

import math
from typing import List, Union

"""
Module qui permet de faire une addition
avec des nombres entiers et flottant.
"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:

    """
    Permet de réaliser une opération et renvoie
    un float.
    """

    return float(math.fsum(mxd_lst))
