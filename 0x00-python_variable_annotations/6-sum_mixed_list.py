#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats.

Functions:
    sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
        Returns the sum of a list of integers and floats as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]): List containing integers and floats.

    Returns:
        float: The sum of the elements in mxd_lst.
    """
    return float(sum(mxd_lst))
