#!/usr/bin/python3
"""
Module Doc
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function Doc
    """
    return [(i, len(i)) for i in lst]
