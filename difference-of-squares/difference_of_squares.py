def square_of_sum(number):
    n = number
    s = n * (n + 1) // 2
    return s**2


def sum_of_squares(number):
    n = number
    return n * (n + 1) * (2 * n + 1) // 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
