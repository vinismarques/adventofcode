from dotenv import load_dotenv
from utils import get_day_data


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
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


def main(data: str) -> None:
    fresh_input, ingredients_input = data.split("\n\n")
    fresh_ranges = []
    for fresh_range in fresh_input.splitlines():
        start, end = map(int, fresh_range.split("-"))
        fresh_ranges.append((start, end))
    merged_ranges = merge_ranges(fresh_ranges)

    total_fresh = 0
    for range in merged_ranges:
        total_fresh += (range[1] + 1) - range[0]
    answer = total_fresh
    print(answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = r"""
    # 3-5
    # 10-14
    # 16-20
    # 12-18

    # 1
    # 5
    # 8
    # 11
    # 17
    # 32
    # """.strip()  # Sample

    main(data)
