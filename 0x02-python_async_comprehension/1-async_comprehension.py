#!/usr/bin/env python3
"""Module containing an async comprehension function."""

from typing import List
from importlib import import_module

# Dynamically import async_generator from the previous task
async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [number async for number in async_generator()]
