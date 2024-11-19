def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not digits:
        return [0]

    if all([digit == 0 for digit in digits]):
        return [0]

    power = len(digits) - 1
    decimal_num = 0
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal_num += input_base**power * digit
        power -= 1

    reverse_digits = []
    while decimal_num >= output_base:
        decimal_num, rem = divmod(decimal_num, output_base)
        reverse_digits.append(rem)

    if decimal_num > 0:
        reverse_digits.append(decimal_num)
    reverse_digits.reverse()

    return reverse_digits
