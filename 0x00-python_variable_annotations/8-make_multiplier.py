#!/usr/bin/env python3
"""multiple"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiple"""
    return lambda c: c * multiplier
