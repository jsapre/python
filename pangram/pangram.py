def is_pangram(sentence: str):
    return set("abcdefghijklmnopqrstuvwxyz").issubset(set(sentence.lower()))
