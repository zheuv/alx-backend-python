#!/usr/bin/env python3
"""
Module Doc
"""

from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function Doc
    """
    result = 0
    for i in mxd_lst:
        result += i
    return result
