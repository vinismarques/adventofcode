from dotenv import load_dotenv
from utils import get_day_data


def main() -> None:
    data = get_day_data()

    print("Hello from adventofcode!\n\nData:", data)


if __name__ == "__main__":
    load_dotenv()
    main()
