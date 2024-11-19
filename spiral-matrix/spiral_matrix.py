def spiral_matrix(size):
    if size == 0:
        return []

    m = [[0 for c in range(size)] for r in range(size)]
    left, right, top, bottom = -1, size, -1, size
    r, c = 0, 0
    value = 1
    while left < right or top < bottom:
        # fill right
        while c < right:
            m[r][c] = value
            value += 1
            c += 1
        top += 1
        c -= 1
        r += 1
        # fill down
        while r < bottom:
            m[r][c] = value
            value += 1
            r += 1
        right -= 1
        r -= 1
        c -= 1
        # fill left
        while c > left:
            m[r][c] = value
            value += 1
            c -= 1
        c += 1
        r -= 1
        bottom -= 1
        # fill up
        while r > top:
            m[r][c] = value
            value += 1
            r -= 1
        left += 1
        c += 1
        r += 1

    return m
