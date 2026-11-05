import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    file: IO[str] | None = None
    try:
        file = open(file_name, 'r')
        print("---\n")
        print(file.read())
        print("---")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
