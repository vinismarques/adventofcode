from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

from aocd import get_data

# 8-directional neighbors (including diagonals)
DIRECTIONS_8 = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]  # fmt: off


def get_day_and_year() -> tuple[int, int]:
    """
    Extract day and year from the file path, assuming it matches .../YEAR/DAY/...
    """
    p = Path(__file__).resolve()
    # We look for two parent folder names that are both digit (year and day)
    # e.g. .../2025/02/utils.py
    try:
        day_str = p.parent.name  # '02'
        year_str = p.parent.parent.name  # '2025'
        day = int(day_str)
        year = int(year_str)
    except Exception as e:
        raise RuntimeError(f"Could not determine day and year from file path: {p}") from e
    return day, year


def get_day_data() -> str:
    day, year = get_day_and_year()
    return get_data(day=day, year=year)


@dataclass
class Node:
    data: Any
    prev: Node | None = None
    next: Node | None = None


class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.current = None  # Cursor navigation

    @property
    def current_data(self) -> Any:
        assert self.current
        return self.current.data

    def is_empty(self) -> bool:
        return self.head is None

    def ensure_not_empty(self) -> None:
        if self.is_empty():
            raise ValueError("List is empty")

    def append(self, data: Any) -> None:
        if self.is_empty():
            new_node = Node(data)
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
            self.current = new_node  # Initialize cursor
        else:
            assert self.head
            tail = self.head.prev
            new_node = Node(data, prev=tail, next=self.head)
            assert tail
            tail.next = new_node
            self.head.prev = new_node

    def prepend(self, data: Any) -> None:
        self.ensure_not_empty()
        assert self.head
        self.head = self.head.prev

    def move_forward(self, steps=1) -> None:
        self.ensure_not_empty()
        for i in range(steps):
            assert self.current
            self.current = self.current.next

    def move_backward(self, steps=1) -> None:
        self.ensure_not_empty()
        for i in range(steps):
            assert self.current
            self.current = self.current.prev

    def goto(self, data: Any) -> None:
        """Moves the cursor to the first occurence of `data`."""
        self.ensure_not_empty()
        cur = self.head
        while True:
            assert cur
            if cur.data == data:
                self.current = cur
                return
            if cur.next == self.head:
                raise ValueError(f"Node with data '{data}' not found")
            cur = cur.next


def monotonic_decreasing(seq: Sequence, k: int | None = None) -> list:
    """
    Select k elements from seq (preserving order) to form the optimal subsequence.

    Args:
        seq: Input sequence
        k: Number of elements to select
    """
    stack = []
    to_remove = len(seq) - k if k else len(seq)

    for num in seq:
        # Remove elements that are smaller than current
        while to_remove > 0 and stack and stack[-1] < num:
            stack.pop()
            to_remove -= 1
        stack.append(num)

    return stack[:k]


def get_neighbors(grid, i, j, directions) -> list[tuple[int, int, Any]]:
    rows, cols = len(grid), len(grid[0])

    neighbors = []
    for offset_i, offset_j in directions:
        ni = i + offset_i
        nj = j + offset_j
        if rows > ni >= 0 and cols > nj >= 0:
            n_value = grid[ni][nj]
            neighbors.append((ni, nj, n_value))
    return neighbors


def pretty_print(grid, targets: list[tuple] | None = None) -> None:
    pretty_m = deepcopy(grid)

    for i in range(len(pretty_m)):
        for j in range(len(pretty_m[i])):
            value = pretty_m[i][j]
            if targets and (i, j, value) in targets:
                pretty_m[i][j] = "x"
        print("".join(pretty_m[i]))
    print("")


def merge_ranges(ranges: list[tuple[int, int]]) -> list[list[int]]:
    if not ranges:
        return []

    ranges.sort(key=lambda x: x[0])

    merged = []
    for r in ranges:
        if not merged or r[0] > merged[-1][1]:
            merged.append([*r])
        else:
            merged[-1][1] = max(merged[-1][1], r[1])
    return merged
