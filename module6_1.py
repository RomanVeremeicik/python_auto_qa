"""Implements a Stack data structure"""


def mod1(array: list) -> str:
    """Function return positive or negative number from list"""
    flag = 0
    for i in array:
        if i < 0:
            flag = 1
            # print(i)

    if flag == 1:
        return 'negative number in list'
    if flag != 1:
        return 'positive number in list'
    return 1
