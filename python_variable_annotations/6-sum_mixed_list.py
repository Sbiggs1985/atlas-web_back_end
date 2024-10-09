#!/usr/bin/env python3

"""
Type-annotation function with a provided sum_list and returns aa float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Imports Sum_list
    """
    return float(sum(mxd_lst))
