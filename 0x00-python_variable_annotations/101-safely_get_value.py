#!/usr/bin/env python3
"""
This module provides a function to safely retrieve a value from a dictionary.

Functions:
    safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) ->
    Union[Any, T]:
        Returns the value associated with key if it exists, otherwise returns
        the default value.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with the given key
    if it exists in the dictionary,
    otherwise returns the provided default value.

    Args:
        dct (Mapping): A dictionary-like mapping
        from which to retrieve the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The value to return
        if key is not in dct.

    Returns:
        Union[Any, T]: The value associated with key
        or the default value if key is not present.
    """
    if key in dct:
        return dct[key]
    return default
