#!/usr/bin/env python3

"""
Type-annotation function that takes a string.
Imports Tuple; an immutable sequence data structure.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))
