#!/usr/bin/env python3
"""
DOc for task 4
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that wraps the wait_random coroutine.

    Args:
    max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
    asyncio.Task: An asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
