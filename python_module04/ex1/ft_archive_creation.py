import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file: IO[str] = open(file_name, 'r')
        print("---\n")
        file_content = file.read()
        print(file_content)
        print("---")

        lines = file_content.split("\n")
        file.close()
        print(f"File '{file_name}' closed.\n")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    lines = [line + '#' for line in lines[:-1]]
    lines.append("")
    print("Tranform data:\n")
    print("---\n")
    for line in lines:
        print(line)
    print("---")
    file_name = input("Enter new file name (or empty): ")
    if (file_name == ""):
        print("Not saving data.")
        return
    try:
        file = open(file_name, 'x')
        print(f"Saving data to '{file_name}'")
        for line in lines:
            file.write(line + "\n")
        print(f"Data saved in file '{file_name}'\n")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error opening file '{file_name}': {e}")
        return


if __name__ == "__main__":
    main()
