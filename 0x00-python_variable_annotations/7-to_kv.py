#!/usr/bin/env python3
"""convert to string"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """convert float number to a string"""
    return float(k, v * v)
