#!/usr/bin/env python3

"""
Type-annotation function thaat takes a input_list.
I have imported the required sum_list and input_list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
