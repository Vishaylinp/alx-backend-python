#!/usr/bin/env python3
"""Identical to wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task wait for n"""
    task = []
    delay = []

    for c in range(n):
        n_task = task_wait_random(max_delay)
        task.append(n_task)

    for n_task in asyncio.as_completed(task):
        delays = await n_task
        delay.append(delays)

    return delay
