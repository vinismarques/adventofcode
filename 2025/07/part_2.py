from functools import lru_cache

from dotenv import load_dotenv
from utils import get_day_data


def main(data: str) -> None:
    grid = [list(line) for line in data.splitlines()]

    @lru_cache(maxsize=None)
    def count_paths(row: int, col: int) -> int:
        # Check if is last row
        if row >= len(grid) - 1:
            return 1

        # Below is empty
        if grid[row + 1][col] == ".":
            return count_paths(row + 1, col)

        # Check if found splitter
        if grid[row + 1][col] == "^":
            total = 0
            if grid[row + 1][col - 1] == ".":
                total += count_paths(row + 1, col - 1)
            if grid[row + 1][col + 1] == ".":
                total += count_paths(row + 1, col + 1)
            return total

        raise ValueError(f"Unexpected state at ({row},{col})")

    start_col = grid[0].index("S")
    total_splits = count_paths(0, start_col)

    answer = total_splits
    print(answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = r"""
    # .......S.......
    # ...............
    # .......^.......
    # ...............
    # ......^.^......
    # ...............
    # .....^.^.^.....
    # ...............
    # ....^.^...^....
    # ...............
    # ...^.^...^.^...
    # ...............
    # ..^...^.....^..
    # ...............
    # .^.^.^.^.^...^.
    # ...............
    # """.strip()  # Sample

    main(data)
