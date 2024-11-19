def encode(numbers):
    result = []
    for n in numbers:
        b = bin(n)[2:]
        d, m = divmod(len(b), 7)
        first = 0  # default
        if m != 0:
            first = f"{b[0:m]:0>7s}"
        elif d == 0:
            result.append(0)
            continue

        rest = []
        index = m
        for i in range(d):
            rest.append(b[index + i * 7 : index + (i + 1) * 7])

        if rest:
            if first != 0:
                first = "1" + first

            for i in range(len(rest)):
                if i == len(rest) - 1:
                    rest[i] = "0" + rest[i]
                else:
                    rest[i] = "1" + rest[i]
        else:
            first = "0" + first

        if first != 0:
            rest.insert(0, first)

        for item in rest:
            result.append(int(item, 2))

    return result


def decode(bytes_):
    state = "NEW"  # state can be NEW, ONGOING
    result = []
    cur_list = []
    for i, b in enumerate(bytes_):
        if state == "NEW" and cur_list:  ## should be empty
            raise ValueError("incomplete sequence")

        if state == "ONGOING" and not cur_list:  ## should not be empty
            raise ValueError("incomplete sequence")

        if b & 0b10000000 == 0b10000000:  ## continuation byte
            cur_list.append(bin(b)[3:])
            state = "ONGOING"
            if i == len(bytes_) - 1:
                raise ValueError("incomplete sequence")
        else:  ## end byte
            b_str = f"{bin(b)[2:]:0>7s}"
            cur_list.append(b_str)
            result.append(int("".join(cur_list), 2))
            state = "NEW"
            cur_list = []

    return result
