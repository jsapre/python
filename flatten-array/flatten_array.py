import typing


def flatten_rec(input):
    if not isinstance(input, typing.List):
        return [input]
    result = []
    for item in input:
        result += flatten_rec(item)

    return [i for i in result if i is not None]


def flatten(iterable):
    result = []
    for item in iterable:
        result += flatten_rec(item)

    return [i for i in result if i is not None]
