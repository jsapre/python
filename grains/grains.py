def square(number):
    """power formula

    Args:
        number (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    """sum of geometric series

    Returns:
        _type_: _description_
    """
    return 2**64 - 1
