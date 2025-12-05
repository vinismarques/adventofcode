from aocd import get_data
from dotenv import load_dotenv


def main() -> None:
    data = get_data(day=1, year=2025)

    print("Hello from adventofcode!\n\nData:", data)


if __name__ == "__main__":
    load_dotenv()
    main()
