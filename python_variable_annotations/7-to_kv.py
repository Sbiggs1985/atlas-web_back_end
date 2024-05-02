#!/usr/bin/env python3

"""
Type-annotation function that takes a string.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Imports Tuple
    """
    return (k, float(v ** 2))
