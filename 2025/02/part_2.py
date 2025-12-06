import re

from dotenv import load_dotenv
from utils import get_day_data


def main() -> None:
    data = get_day_data()
    # data = """
    # 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
    # """.strip()

    repeated_pattern = re.compile(r"^(\w+)(\1+)$")

    ranges = data.split(",")
    mistakes = []
    for r in ranges:
        raw_start, raw_end = r.split("-", maxsplit=2)
        start = int(raw_start)
        stop = int(raw_end) + 1
        for value in range(start, stop):
            value_str = str(value)
            match = repeated_pattern.search(value_str)
            if match:
                mistakes.append(value)

    print(sum(mistakes))


if __name__ == "__main__":
    load_dotenv()
    main()
