#!/usr/bin/env python3
"""module defining type checking function"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """function that returns list of multiple copies of items in a tuple."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
