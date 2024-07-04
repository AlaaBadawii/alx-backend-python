#!/usr/bin/env python3
"""Make a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> callable:
    """Make a multiplier"""
    def multiply(n: float) -> float:
        """Multiply a float by multiplier"""
        return n * multiplier
    return multiply
