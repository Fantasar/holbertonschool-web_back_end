#!/usr/bin/env python3
"""
Module qui permet de récupérer des nombres
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:

    """
    Coroutine qui récupère 10 nombres aléatoires et
    retourne une listes entre 0 et 10
    """

    return [i async for i in async_generator()]
