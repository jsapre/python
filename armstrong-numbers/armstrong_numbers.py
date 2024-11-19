from functools import reduce


def is_armstrong_number(number):
    num_str: str = f"{number}"
    length = len(num_str)
    total = reduce(lambda accum, x: accum + (ord(x) - ord("0")) ** length, num_str, 0)
    return total == number
