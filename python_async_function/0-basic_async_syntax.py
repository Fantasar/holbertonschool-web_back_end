#!/usr/bin/env python3

"""
Module Async qui prends une valeurs aléatoires pour
l'attente de la fonction.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:

    """
    Fonction qui prends une valeurs aléatoire
    entre 0 et max_delay.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
