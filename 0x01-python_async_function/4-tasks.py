#!/usr/bin/env python3
'''Task 4: Modify the code for task 3
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Modified Task 3
    '''
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
