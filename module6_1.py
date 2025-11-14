"""Implements a Stack data structure"""
from typing import Any


def mod1(array: list) -> str:
    flag = 0
    for i in array:
        if i < 0:
            flag = 1
            # print(i)

    if flag == 1:
        return 'negative number in list'
    else:
        return 'positive number in list'
