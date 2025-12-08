import re
from functools import reduce
from operator import add, mul, sub
from typing import Any, Callable

from dotenv import load_dotenv
from utils import get_day_data


def get_operation(op: str) -> Callable[[Any, Any], Any]:
    match op:
        case "*":
            return mul
        case "+":
            return add
        case "-":
            return sub
        case _:
            raise ValueError(f"Operator '{op}' is not supported.")


def main(data: str) -> None:
    pattern = re.compile(r"\s+([\S]+)")
    rows = data.splitlines()
    reversed_rows = [row[::-1] for row in rows]

    value_rows = reversed_rows[:-1]

    grand_total = 0
    op_matches_iter = pattern.finditer(reversed_rows[-1])
    op_matches = list(op_matches_iter)

    for match_index, op_match in enumerate(op_matches):
        op = op_match.group().strip()
        op_func = get_operation(op)

        start_idx = op_match.start() if match_index == 0 else op_match.start() + 1
        stop_idx = op_match.end()

        # Group numbers right-to-left
        rtl_numbers = {}
        for raw_num in value_rows:
            num_str = raw_num[start_idx:stop_idx]
            nums = dict(enumerate(num_str))
            for k, v in nums.items():
                if v.strip():
                    rtl_numbers.setdefault(k, []).append(v)
        rtl_int = [int("".join(n)) for n in rtl_numbers.values()]

        op_total = reduce(op_func, rtl_int)

        print(f"Total for operation '{op}': {op_total}")
        grand_total += op_total

    answer = grand_total
    print("Answer: ", answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = r"""123 328  51 64
    #  45 64  387 23
    #   6 98  215 314
    # *   +   *   +  """  # Sample

    main(data)
