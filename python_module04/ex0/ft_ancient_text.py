import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file: IO[str] = open(file_name, 'r')
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    print("---\n")
    print(file.read())
    print("---")
    file.close()
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
