from copy import deepcopy
from typing import Any

from dotenv import load_dotenv
from utils import get_day_data

DEBUG = False

# 8-directional neighbors (including diagonals)
directions_8 = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]  # fmt: off


def get_neighbors(m, i, j, directions) -> list[tuple[int, int, Any]]:
    rows, cols = len(m), len(m[0])

    neighbors = []
    for offset_i, offset_j in directions:
        n_i = i + offset_i
        n_j = j + offset_j
        if rows > n_i >= 0 and cols > n_j >= 0:
            n_value = m[n_i][n_j]
            neighbors.append((n_i, n_j, n_value))
    return neighbors


def pretty_print(m, targets: list[tuple] | None = None) -> None:
    pretty_m = deepcopy(m)

    for i in range(len(pretty_m)):
        for j in range(len(pretty_m[i])):
            value = pretty_m[i][j]
            if targets and (i, j, value) in targets:
                pretty_m[i][j] = "x"
        print("".join(pretty_m[i]))
    print("")


def find_accessables(m) -> list[tuple[int, int, Any]]:
    accessables: list[tuple[int, int, Any]] = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            value = m[i][j]

            if value != "@":
                continue  # Not paper

            neighbors = get_neighbors(m, i, j, directions=directions_8)
            if DEBUG:
                print("All neighbors:")
                pretty_print(m, neighbors)

            blocking_neighbors = []
            for n_i, n_j, n_value in neighbors:
                if n_value == "@":
                    blocking_neighbors.append((n_i, n_j, n_value))
            if DEBUG:
                print("Blocking neighbors:")
                pretty_print(m, blocking_neighbors)

            if len(blocking_neighbors) < 4:
                accessables.append((i, j, value))

    return accessables


def main(data: str) -> None:
    rows = data.splitlines()
    m = [list(r) for r in rows]
    print("Original:")
    pretty_print(m)

    all_accessables = []
    mutated_m = deepcopy(m)
    while accessables := find_accessables(mutated_m):
        all_accessables.extend(accessables)

        for i, j, value in accessables:
            mutated_m[i][j] = "."

    pretty_print(m, all_accessables)
    answer = len(all_accessables)
    print(answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = """
    # ..@@.@@@@.
    # @@@.@.@.@@
    # @@@@@.@.@@
    # @.@@@@..@.
    # @@.@@@@.@@
    # .@@@@@@@.@
    # .@.@.@.@@@
    # @.@@@.@@@@
    # .@@@@@@@@.
    # @.@.@@@.@.
    # """.strip()

    main(data)
