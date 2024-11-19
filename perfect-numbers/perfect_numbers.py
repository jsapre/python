from math import sqrt


def find_factors_sum(number):
    sq_root = round(sqrt(number))
    factors = []
    if number > 1:
        factors.append(1)

    for factor in range(2, sq_root + 1):
        if number % factor == 0:
            factors.append(factor)
            factors.append(number // factor)
    return sum(set(factors))


def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factor_sum = find_factors_sum(number)

    if factor_sum == number:
        return "perfect"

    if factor_sum > number:
        return "abundant"

    return "deficient"
