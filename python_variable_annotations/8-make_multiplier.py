#!/usr/bin/env python3

"""
Type-annotation function that returns a function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Imports callable which is a built-in function used to check an object.
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
