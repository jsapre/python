from math import sqrt


def dist(x, y):
    return sqrt(x**2 + y**2)


def score(x, y):
    distance = dist(x, y)
    if distance > 10:
        return 0
    if distance > 5:
        return 1
    if distance > 1:
        return 5
    return 10
