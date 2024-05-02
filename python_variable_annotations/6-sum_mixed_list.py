#!/usr/bin/env python3

"""
Type-annotation function with a provided sum_list and returns aa float.
Imports List which is a list of items where all elements are of the same type.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
