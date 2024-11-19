from itertools import combinations as comb


def combinations(target, size, exclude):
    usable = list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(exclude))
    result = []
    if size > len(usable):
        return result

    for t in comb(usable, size):
        if sum(t) == target:
            result.append(list(t))

    return result
