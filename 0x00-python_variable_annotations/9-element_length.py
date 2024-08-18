#!/usr/bin/env python3
"""iterable"""
from typing import Tuple, Iterable, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """length of list"""
    return [(i, len(i)) for i in lst]
