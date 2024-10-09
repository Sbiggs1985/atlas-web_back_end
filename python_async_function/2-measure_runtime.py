#!/usr/bin/env python3

"""
Measuring the runtime by using imports and a runtime.py file.
"""
import time
import asyncio
from typing import Tuple, List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Using the measure_time function
    """
    start_time: float = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end_time: float = time.perf_counter()
    total_time: float = end_time - start_time
    return total_time / n
