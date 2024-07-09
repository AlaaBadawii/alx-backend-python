#!/usr/bin/env python3
'''Task 1's module.
'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    Collect 10 random numbers using
    an async comprehensing over async_generator.
    """
    nums = [num async for num in async_generator()]

    return nums
