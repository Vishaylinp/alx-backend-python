#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return random number"""
    res = [c async for c in async_generator()]
    return res
