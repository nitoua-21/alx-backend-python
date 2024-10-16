#!/usr/bin/env python3
"""
Mdoule 102-type_checking

Functions:
    zoom_array(lst: Tuple[int, ...], factor: int) -> List[int]:
        Returns a list with elements of the tuple repeated by the factor.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Creates multiple copies of items in a tuple.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
