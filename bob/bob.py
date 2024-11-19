def response(hey_bob: str):
    index = 4  # default response
    question_flag = hey_bob.rstrip().endswith("?")
    uppercase_flag = hey_bob.isupper()
    space_flag = not hey_bob or hey_bob.isspace()

    if space_flag:
        index = 3
    elif question_flag and uppercase_flag:
        index = 2
    elif uppercase_flag:
        index = 1
    elif question_flag:
        index = 0
    else:
        index = 4  # default response

    return RESPONSES[index]


RESPONSES = (
    "Sure.",
    "Whoa, chill out!",
    "Calm down, I know what I'm doing!",
    "Fine. Be that way!",
    "Whatever.",
)
