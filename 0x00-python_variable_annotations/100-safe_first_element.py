#!/usr/bin/env python3
"""
Module 100-safe_first_element

Functions:
    safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
        Returns the first element if the list is not empty, otherwise None.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it is not empty, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence containing elements of any type.

    Returns:
        Union[Any, None]: The first element of lst or None if lst is empty.
    """
    if lst:
        return lst[0]
    return None
