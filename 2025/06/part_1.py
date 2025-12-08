import re
from operator import add, mul, sub

from dotenv import load_dotenv
from utils import get_day_data


def get_operation(op: str):
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
    pattern = re.compile(r"([\S]+)")
    parsed_rows = [pattern.findall(row) for row in data.splitlines()]

    ops = parsed_rows[-1]
    rows = parsed_rows[:-1]

    grand_total = 0
    for col, op in enumerate(ops):
        op_func = get_operation(op)
        numbers = [int(row[col]) for row in rows]

        op_total = 0
        for idx, number in enumerate(numbers):
            if idx == 0:
                op_total = number
            else:
                op_total = op_func(op_total, number)

        print(f"Total for operation '{op}': {op_total}")
        grand_total += op_total

    answer = grand_total
    print("Answer: ", answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = r"""
    # 123 328  51 64
    #     45 64  387 23
    #     6 98  215 314
    # *   +   *   +
    # """.strip()  # Sample

    main(data)
