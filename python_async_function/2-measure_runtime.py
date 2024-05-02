#!/usr/bin/env python3

"""
Measuring the runtime by using imports and a runtime.py file.
"""


import time
import asyncio
from typing import Tuple
from your_previous_file import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Using the measure_time function
    """
    start_time = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
