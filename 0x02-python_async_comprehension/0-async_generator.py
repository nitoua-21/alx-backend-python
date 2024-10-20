#!/usr/bin/env python3
"""Module containing an asynchronous generator function."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Coroutine that yields 10 random numbers between 0 and 10.
    Each yield is preceded by an asynchronous wait of 1 second.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
