#!/usr/bin/env python3
"""Basic async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for random time period"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
