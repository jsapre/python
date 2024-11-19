""" This is NOT using existing functions
    Note: There is another solution iteration on exercism that has all functions using existing library functions
"""

from functools import reduce


def append(list1, list2):
    for l in list2:
        list1.append(l)

    return list1


def concat(lists):
    result = []
    for l in lists:
        result = append(result, l)

    return result


def filter(function, list):
    return [l for l in list if function(l)]


def length(list):
    l = 0
    for _ in list:
        l += 1

    return l


def map(function, list):
    return [function(l) for l in list]


def foldl(function, list, initial):
    if initial is not None:
        list.insert(0, initial)

    if len(list) == 1:
        return list[0]

    result = function(list[0], list[1])
    for l in list[2:]:
        result = function(result, l)

    return result


def foldr(function, list: list, initial):
    list.reverse()
    if initial is not None:
        list.insert(0, initial)

    if len(list) == 1:
        return list[0]

    result = function(list[0], list[1])
    for l in list[2:]:
        result = function(result, l)

    return result


def reverse(list: list):
    result = []
    l = len(list)
    i = -1
    while i >= -l:
        result.append(list[i])
        i -= 1

    return result
