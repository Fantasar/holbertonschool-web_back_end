#!/usr/bin/env python3

"""
Module qui contient une simple fonction
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):

    """
    Fonction qui prends en paramètres un entier
    et retourne une task.syncio
    """

    return asyncio.ensure_future(wait_random(max_delay))
