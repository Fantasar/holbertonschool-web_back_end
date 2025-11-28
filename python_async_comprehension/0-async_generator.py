#!/usr/bin/env python3
"""
Module qui permet de génerer un nombres aléaatoires
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:

    """
    Module qui permet de créer une coroutine
    d'une boucle de 10, avec 1 secondes d'attentes
    entres les tours.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
