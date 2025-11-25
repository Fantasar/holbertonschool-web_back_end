#!/usr/bin/env python3

"""
Module qui permet de travailler sur la fonction
précèdament construite wait-random.
"""

import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    """
    Fonction qui prends en paramètre deux entiers
    et qui renvoir une listes de float définie entre
    la fourchette des deux entiers.
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)
    return delays
