#!/usr/bin/env python3

"""
Module qui permet contient une fonctions pour réaliser
une division avec un rest de type float.
"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:

    """
    Fonction prenant en paramètre deux entiers afin de
    réaliser une fonction est de renvoyer un nombre de
    type float.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = (end - start)
    return total_time / n
