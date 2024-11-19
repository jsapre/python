def rotate(text, key):
    a, A, z, Z = ord("a"), ord("A"), ord("z"), ord("Z")
    num_list = [ord(ch) for ch in text]
    code_list = []
    for nch in num_list:
        if a <= nch <= z:
            nch += key
            if nch > z:
                nch = a + nch - z - 1

            code_list.append(nch)
        elif A <= nch <= Z:
            nch += key
            if nch > Z:
                nch = A + nch - Z - 1

            code_list.append(nch)
        else:
            code_list.append(nch)

    return "".join([chr(nch) for nch in code_list])
