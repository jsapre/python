def annotate(minefield):
    try:
        rc = len(minefield)
        if rc == 0:
            return minefield

        cc = len(minefield[0])
        if cc == 0:
            return minefield

        for row in minefield:
            if len(row) != cc:
                raise ValueError("The board is invalid with current input.")

        brd = []
        for row in minefield:
            brd.append(list(row))

        for row in range(rc):
            for col in range(cc):
                if brd[row][col] == "*":
                    continue
                elif brd[row][col] != " ":
                    raise ValueError("The board is invalid with current input.")

                mine_count = 0
                # process the cell by going through neighbors
                for r in range(row - 1, row + 2):
                    if r < 0 or r >= rc:
                        continue
                    for c in range(col - 1, col + 2):
                        if c < 0 or c >= cc:
                            continue
                        if r == row and c == col:
                            continue
                        # Check this neighbor to be mine
                        if brd[r][c] == "*":
                            mine_count += 1

                if mine_count > 0:
                    brd[row][col] = str(mine_count)

        return ["".join(row) for row in brd]

    except Exception as err:
        raise ValueError("The board is invalid with current input.")
