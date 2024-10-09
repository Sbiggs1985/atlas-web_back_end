#!/usr/bin/env python3

"""
Type-annotation function with parameters with values.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Using the element_length function
    """
    return [(i, len(i)) for i in lst]
