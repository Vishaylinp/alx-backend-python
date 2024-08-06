#!/usr/bin/env python3
"""Run time for parallel comprehension"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for c in range(4)))
    end = time.time()
    res = end - start
    return res
