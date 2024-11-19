def find(search_list, value):

    start, end = 0, len(search_list)
    while start < end:
        index = start + (end - start) // 2
        candidate = search_list[index]
        if candidate == value:
            return index
        elif candidate < value:
            start = index + 1
        else:
            end = index

    raise ValueError("value not in array")
