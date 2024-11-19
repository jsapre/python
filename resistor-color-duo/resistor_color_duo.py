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
