def color_code(color):
    cmap = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    return cmap[color]


def value(colors):
    num = 0
    for i, color in enumerate(colors[0:2]):
        num += color_code(color) * 10 ** (1 - i)

    return num


def label(colors):
    num = value(colors)
    third = color_code(colors[2])
    num = num * 10**third
    prefix = "ohms"
    zeros = third
    if color_code(colors[1]) == 0:
        zeros += 1

    if 3 <= zeros < 6:
        prefix = "kiloohms"
        num //= 1000
    elif 6 <= zeros < 9:
        prefix = "megaohms"
        num //= 1000000
    elif zeros >= 9:
        prefix = "gigaohms"
        num //= 1000000000

    return f"{num} {prefix}"
