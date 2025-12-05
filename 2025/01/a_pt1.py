import re

from aocd import get_data
from dotenv import load_dotenv
from utils import CircularDoublyLinkedList


def main() -> str:
    data = get_data(day=1, year=2025)

    # Initialize circular linked list
    linked_list = CircularDoublyLinkedList()
    for i in range(0, 100):
        linked_list.append(i)

    # Go to initial position
    linked_list.goto(50)

    parsed_data = data.splitlines()

    secret = 0  # Total number of times that cursor was at zero
    for rotation in parsed_data:
        match = re.match(r"([LR])(\d+)", rotation)
        if not match:
            raise ValueError(f"Rotation '{rotation}' could not be parsed")
        direction, raw_steps = match.groups()
        steps = int(raw_steps)
        if direction.lower() == "l":
            linked_list.move_backward(steps)
        else:
            linked_list.move_forward(steps)
        if linked_list.current_data == 0:
            secret += 1

    return str(secret)


if __name__ == "__main__":
    load_dotenv()
    result = main()
    print(result)
