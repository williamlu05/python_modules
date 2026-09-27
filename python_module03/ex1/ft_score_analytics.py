import sys


class NoScoreError(Exception):
    def __init__(self, message: str = "No scores provided.") -> None:
        self.message = message
        super().__init__(self.message)


def process_arguments() -> list[int]:
    array = []
    count = 1
    while count < len(sys.argv):
        try:
            array.append(int(sys.argv[count]))
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[count]}'")
        finally:
            count += 1
    if len(array) == 0:
        raise NoScoreError()
    return array


def show_stats(array: list[int]) -> None:
    print(f"Scores processed: {array}")
    print(f"Total players: {len(array)}")
    print(f"Total score: {sum(array)}")
    print(f"Average score: {sum(array) / len(array)}")
    print(f"High score: {max(array)}")
    print(f"Low score: {min(array)}")
    print(f"Score range: {max(array) - min(array)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    try:
        array = process_arguments()
        show_stats(array)
    except NoScoreError as e:
        print(
            f"{e}",
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
