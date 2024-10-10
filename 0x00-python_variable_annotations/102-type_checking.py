#!/usr/bin/env python3
"""
Mdoule 102-type_checking

Functions:
    zoom_array(lst: Tuple[int, ...], factor: int) -> List[int]:
        Returns a list with elements of the tuple repeated by the factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a list where each element in the tuple
    lst is repeated factor times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to be repeated.
        factor (int, optional): The number of times to repeat each element.

    Returns:
        List[int]: A list containing the repeated elements.
    """
    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = (12, 72, 91)  # Modified to be a tuple as expected by the function

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected to pass an integer, as expected
