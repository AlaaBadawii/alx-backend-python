#!/usr/bin/env python3
"""Task 2's module."""
import asyncio
import time
from typing import List
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of async_comprehension called 4 times."""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )

    return time.time() - start
