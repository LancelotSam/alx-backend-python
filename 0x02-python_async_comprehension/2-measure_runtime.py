#!/usr/bin/env python3
""" Third task, imported from the second task
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures runtime of async_comp
    """
    start = time.time()
    res = await asyncio.gather(*(async_comprehension() for x in range(4)))
    end = time.time() - start

    return end
