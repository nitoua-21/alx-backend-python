#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier function.

Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        Returns a function that multiplies a float
        by the specified multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given float
    by a specified multiplier.

    Args:
        multiplier (float): The multiplier to apply.

    Returns:
        Callable[[float], float]: A function that
        multiplies its argument by multiplier.
    """
    return lambda x: x * multiplier
