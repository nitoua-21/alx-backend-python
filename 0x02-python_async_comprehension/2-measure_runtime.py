#!/usr/bin/env python3
"""Module for measuring the runtime of async_comprehension."""

import asyncio
import time
from typing import List
from importlib import import_module

# Dynamically import async_comprehension from the previous task
async_comprehension = import_module(
        '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
