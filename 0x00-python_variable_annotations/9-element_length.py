#!/usr/bin/env python3
"""
Module 9-element_length

Functions:
    element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
        Returns a list of tuples with each element and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple
    contains an element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
        with each element and its length.
    """
    return [(i, len(i)) for i in lst]
