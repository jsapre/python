def tolerance(color):
    cmap = {
        "gold": "5%",
        "brown": "1%",
        "red": "2%",
        "green": "0.5%",
        "blue": "0.25%",
        "violet": "0.1%",
        "grey": "0.05%",
        "silver": "10%",
    }

    return cmap[color]


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
    if len(colors) == 4:
        for i, color in enumerate(colors[0:2]):
            num += color_code(color) * 10 ** (1 - i)
    elif len(colors) == 5:
        for i, color in enumerate(colors[0:3]):
            num += color_code(color) * 10 ** (2 - i)
    else:
        raise ValueError(f"colors with bands {len(colors)}")

    return num


def label(colors):
    num = value(colors)
    multiplier = color_code(colors[2])
    if len(colors) == 5:
        multiplier = color_code(colors[3])

    num = num * 10**multiplier
    prefix = "ohms"

    if num >= 1000000000:
        num = round(num / 1000000000, 2)
        prefix = "gigaohms"
    elif num >= 1000000:
        num = round(num / 1000000, 2)
        prefix = "megaohms"
    elif num >= 1000:
        num = round(num / 1000, 2)
        prefix = "kiloohms"

    if num == round(num):
        num = round(num)

    return f"{num} {prefix}"


def resistor_label(colors):
    if len(colors) == 1 and colors[0] == "black":
        return f"0 ohms"
    l_str = label(colors)

    if len(colors) == 5:
        t_str = tolerance(colors[4])
    elif len(colors) == 4:
        t_str = tolerance(colors[3])

    return f"{l_str} ±{t_str}"
