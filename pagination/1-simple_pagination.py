#!/usr/bin/env python3

"""
Module qui contient  une fonction permettant de
renvoyer un tuple de deux entier contenant la début et
la fin de la page qui contient l'information souhaiter.
Les information sont stocker dans une databass.css sur
des serveur de amazon.aws.
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:

    """
    Fonction qui prends en paramètres deux entier page et page_size
    pour retourner un tuple de deux élèments.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:

    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:

        """
        Cached dataset
        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

        """
        Foncion qui permer de récuper et retourner une page présente
        dans la databass.
        """

        assert (
            isinstance(page, int) and page > 0
        ), "page must be a positive integer"

        assert (
            isinstance(page_size, int) and page_size > 0
        ), "page must be a positive integer"

        start, end = index_range(page, page_size)

        if start >= len(self.dataset()):
            return []

        return self.__dataset[start:end]
