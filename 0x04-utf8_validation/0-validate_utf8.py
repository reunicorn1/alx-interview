#!/usr/bin/python3
"""
0. UTF-8 Validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    This method determines if a given data aset represents a valid
    UTF-8 encoding

    Parameters:
    ----------
    data: a list of dataset as int

    Returns: a boolean
    """
    byte = 0
    seq = False

    for i in data:
        if not seq:
            byte = bytesnumber(i) - 1
            seq = True
        else:
            if i & 192 != 128:
                return False
            byte -= 1
        if not byte:
            seq = False
    return True


def bytesnumber(num: int) -> int:
    """
    This function determine the number of bytes a certain char has
    which marks the start of a sequenece of bytes

    Parameters:
    ----------
    num: a number which starts thr sequenece of bytes which
    represent a certain character

    Returns:
    --------
    the number of bytes to expect
    """
    if num & 192 == 192:
        if num & 224 == 224:
            if num & 240 == 240:
                return 4
            return 3
        return 2
    return 1
