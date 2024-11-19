import re


def is_valid(isbn: str):
    input = isbn.replace("-", "")
    num_list = []
    for ch in input:
        if ch == "X":
            if len(num_list) != 9:
                return False
            num_list.append(10)
        else:
            num_list.append(ord(ch) - ord("0"))

    if len(num_list) != 10:
        return False

    return sum((10 - ind) * num for ind, num in enumerate(num_list)) % 11 == 0
