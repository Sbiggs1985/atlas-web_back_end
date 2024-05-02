#!/usr/bin/env python3

"""
Type-annotation function with parameters with values.
Thee imports bring type hinting capabilities into your Python code.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
