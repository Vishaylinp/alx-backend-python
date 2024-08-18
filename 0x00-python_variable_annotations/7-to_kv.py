#!/usr/bin/env python3
"""type-function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """tuple"""
    return (k, float(v)**2)
