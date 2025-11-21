#!/usr/bin/env python3

"""
Voici un module pour retourner une
lists de tuples
"""

def element_lenght(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """
    Fonction qui retourne une listes de tuples
    prends en base la longeur avec lenght.
    """

    return [(i, len(i)) for i in lst]
