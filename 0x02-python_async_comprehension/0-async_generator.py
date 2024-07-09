#!/usr/bin/env python3
"""
async_generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async_generator: coroutine that loops 10 times, each time asynchronously
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
