lenXMAS = 4


def search_XMAS_all_directions_from(coord, cross_word, lenXMAS, len_i, len_j):
    i, j = coord
    # print(i, j)

    # search forward
    # dont need to search if j > 140-4 = 136
    local_XMAS = 0
    if j <= len_j - lenXMAS:
        # print(cross_word[i][j : j + lenXMAS])
        if "".join(cross_word[i][j : j + lenXMAS]) == "XMAS":
            local_XMAS += 1
            # print("found forward")

    # search backwards
    # dont need to search if j < 4-1 = 3
    if j >= lenXMAS - 1:
        if "".join(cross_word[i][j - 3 : j + 1]) == "SAMX":
            local_XMAS += 1
            # print("found backward")

    # search diagonal up right
    # dist(j-rightborder)>=3 dist(i-rightborder)>=3
    if (len_j - j - 1) > 2 and i > 2:
        diag = (
            cross_word[i][j]
            + cross_word[i - 1][j + 1]
            + cross_word[i - 2][j + 2]
            + cross_word[i - 3][j + 3]
        )
        if diag == "XMAS":
            local_XMAS += 1
            # print("found diag up right")

    # search diagonal up left
    if j > 2 and i > 2:
        diag = (
            cross_word[i][j]
            + cross_word[i - 1][j - 1]
            + cross_word[i - 2][j - 2]
            + cross_word[i - 3][j - 3]
        )
        if diag == "XMAS":
            local_XMAS += 1
            # print("found diag up left")

    # search diag down right
    if (len_j - j - 1) > 2 and (len_i - i - 1) > 2:
        diag = (
            cross_word[i][j]
            + cross_word[i + 1][j + 1]
            + cross_word[i + 2][j + 2]
            + cross_word[i + 3][j + 3]
        )
        if diag == "XMAS":
            local_XMAS += 1
            # print("found diag down right")

    # search diag down left
    if j > 2 and (len_i - i - 1) > 2:
        diag = (
            cross_word[i][j]
            + cross_word[i + 1][j - 1]
            + cross_word[i + 2][j - 2]
            + cross_word[i + 3][j - 3]
        )
        if diag == "XMAS":
            local_XMAS += 1
            # print("found diag down left")
    # search down
    if (len_i - 1 - i) > 2:
        down = (
            cross_word[i][j]
            + cross_word[i + 1][j]
            + cross_word[i + 2][j]
            + cross_word[i + 3][j]
        )
        if down == "XMAS":
            local_XMAS += 1
            # print("found down")

    # search up
    if i > 2:
        up = (
            cross_word[i][j]
            + cross_word[i - 1][j]
            + cross_word[i - 2][j]
            + cross_word[i - 3][j]
        )
        if up == "XMAS":
            local_XMAS += 1
            # print("found up")

    return local_XMAS


def search_X_MAS_all_directions_from(coord, cross_word, len_i, len_j):
    i, j = coord
    # print(i, j)

    # search forward
    # dont need to search if j > 140-4 = 136
    local_XMAS = 0
    if i > 0 and j > 0 and i < len_i - 1 and j < len_j - 1:
        # print("inside condition")
        # top left
        if cross_word[i - 1][j - 1] == "M" and cross_word[i + 1][j + 1] == "S":
            # print(
            #     f"checking {i-1}{j-1} which is {cross_word[i-1][j-1]} and {i+1}{j+1} which is {cross_word[i + 1][j + 1]}"
            # )
            local_XMAS += 1
        # top right
        if cross_word[i - 1][j + 1] == "M" and cross_word[i + 1][j - 1] == "S":
            local_XMAS += 1
            # print(
            #     f"checking {i-1}{j+1} which is {cross_word[i-1][j+1]} and {i+1}{j-1} which is {cross_word[i + 1][j - 1]}"
            # )
        # bottom left
        if cross_word[i + 1][j - 1] == "M" and cross_word[i - 1][j + 1] == "S":
            local_XMAS += 1
            # print(
            #     f"checking {i+1}{j-1} which is {cross_word[i+1][j-1]} and {i-1}{j+1} which is {cross_word[i - 1][j + 1]}"
            # )
        # bottom right
        if cross_word[i + 1][j + 1] == "M" and cross_word[i - 1][j - 1] == "S":
            local_XMAS += 1
            # print(
            #     f"checking {i+1}{j+1} which is {cross_word[i+1][j+1]} and {i-1}{j-1} which is {cross_word[i - 1][j - 1]}"
            # )

    if local_XMAS == 2:
        return 1
    else:
        return 0


cross_word = []
idx_X = []
idx_A = []

with open("d4/input.txt") as f:
    for i, line in enumerate(f):
        new_line = list(line.strip("\n"))
        idx_X += [(i, j) for j, char in enumerate(new_line) if char == "X"]
        idx_A += [(i, j) for j, char in enumerate(new_line) if char == "A"]
        cross_word.append(new_line)

len_i, len_j = len(cross_word), len(cross_word[0])

# part 1
counter = 0
for coord in idx_X:
    counter += search_XMAS_all_directions_from(coord, cross_word, lenXMAS, len_i, len_j)

print(f"P1 counter is {counter}")

# part 2
counter = 0
for coord in idx_A:
    counter += search_X_MAS_all_directions_from(coord, cross_word, len_i, len_j)

print(f"P2 counter is {counter}")
