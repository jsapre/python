from string import ascii_lowercase


def is_isogram(string: str):
    letters = sorted(list(string.lower()))
    for i in range(len(letters) - 1):
        if letters[i] == letters[i + 1] and letters[i] in ascii_lowercase:
            return False

    return True
