#!/usr/bin/python3
from typing import Union

def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    result = 0
    for i in mxd_lst:
        result += i
    return result
