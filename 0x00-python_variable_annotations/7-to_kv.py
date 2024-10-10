#!/usr/bin/env python3
"""
This module provides a function that returns a tuple with a
string and the square of a given integer or float.

Functions:
    to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        Returns a tuple with the string and the square
        of the int/float as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the given string and the square
    of the given number as a float.

    Args:
        k (str): The string to be the first element of the tuple.
        v (Union[int, float]): An integer or float to be squared.

    Returns:
        Tuple[str, float]: A tuple
    """
    return (k, float(v ** 2))
