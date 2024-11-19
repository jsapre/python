def get_lettter_freq(word: str):
    freq = {}
    for letter in word.lower():
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    return freq


def find_anagrams(word: str, candidates):
    base_freq = get_lettter_freq(word.lower())

    result = []
    for w in candidates:
        if w.lower() != word.lower() and get_lettter_freq(w) == base_freq:
            result.append(w)

    return result
