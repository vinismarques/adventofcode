from dotenv import load_dotenv
from utils import get_day_data


def main(data: str) -> None:
    # Code here

    answer = None
    print(answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = r"""
    # """.strip()  # Sample

    main(data)
