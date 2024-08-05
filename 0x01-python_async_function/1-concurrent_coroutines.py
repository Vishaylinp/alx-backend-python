#!/usr/bin/env python3
"""execute multiple corountines"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait n"""
    task = []
    delays = []

    for c in range(n):
        n_task = wait_random(max_delay)
        task.append(n_task)

    for n_task in asyncio.as_completed(task):
        delay = await n_task
        delays.append(delay)

    return delays
