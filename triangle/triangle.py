def valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a and all([a, b, c])


def equilateral(sides):
    a, b, c = sides
    if not valid_triangle(a, b, c):
        return False
    return a == b == c


def isosceles(sides):
    a, b, c = sides
    if not valid_triangle(a, b, c):
        return False
    return a == b or a == c or b == c


def scalene(sides):
    a, b, c = sides
    if not valid_triangle(a, b, c):
        return False
    return a != b and a != c and b != c
