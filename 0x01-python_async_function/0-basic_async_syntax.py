#!/usr/bin/env python3
"""Basic async"""
import asyncio
import random


async def wait_random(max_delay=10):
    """ wait for random time period"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
