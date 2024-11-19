ACTIONS = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str: str):
    rev_str = "".join(reversed(binary_str))
    actions = []
    reverse_flag = False
    for i, ch in enumerate(rev_str):
        if i == 4 and ch == "1":
            reverse_flag = True
        elif i < 4 and ch == "1":
            actions.append(ACTIONS[i])

    if reverse_flag:
        actions.reverse()

    return actions
