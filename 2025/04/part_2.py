import os
from copy import deepcopy
from typing import Any

from dotenv import load_dotenv
from utils import DIRECTIONS_8, get_day_data, get_neighbors, pretty_print

DEBUG = False


def find_accessibles(grid, directions) -> list[tuple[int, int, Any]]:
    accessible_cells: list[tuple[int, int, Any]] = []
    debug = os.getenv("DEBUG") or DEBUG

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            value = grid[i][j]

            if value != "@":
                continue  # Not paper

            neighbors = get_neighbors(grid, i, j, directions)
            if debug:
                print("All neighbors:")
                pretty_print(grid, neighbors)

            blocking_neighbors = []
            for ni, nj, n_value in neighbors:
                if n_value == "@":
                    blocking_neighbors.append((ni, nj, n_value))
            if debug:
                print("Blocking neighbors:")
                pretty_print(grid, blocking_neighbors)

            if len(blocking_neighbors) < 4:
                accessible_cells.append((i, j, value))

    return accessible_cells


def main(data: str) -> None:
    grid = [list(r) for r in data.splitlines()]
    print("Original:")
    pretty_print(grid)

    all_accessibles = []
    working_grid = deepcopy(grid)
    while accessible_cells := find_accessibles(working_grid, directions=DIRECTIONS_8):
        all_accessibles.extend(accessible_cells)

        for i, j, value in accessible_cells:
            working_grid[i][j] = "."

    pretty_print(grid, all_accessibles)
    answer = len(all_accessibles)
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
