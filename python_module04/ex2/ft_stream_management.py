import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print("[STDERR] Usage: ft_stream_management.py <file>",
              file=sys.stderr)
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    fname = sys.argv[1]
    print(f"Accessing file '{fname}'")
    file: IO[str] | None = None
    try:
        file = open(fname, 'r')
        print("---\n")
        file_content = file.read()
        print(file_content)
        print("---")
    except (OSError, UnicodeDecodeError) as e:
        print(f"[STDERR] Error opening file '{fname}': {e}", file=sys.stderr)
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{fname}' closed.\n")

    lines = [line + "#" for line in file_content.splitlines()]
    print("Transform data:")
    print("---\n")
    for line in lines:
        print(line)
    print("\n---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    fname = sys.stdin.readline().rstrip()
    if fname == "":
        print("Not saving data.")
        return

    try:
        print(f"Saving data to '{fname}'")
        file = open(fname, 'w')
        for line in lines:
            file.write(line + "\n")
        print(f"Data saved in file '{fname}'\n")
        file.close()
    except OSError as e:
        print(f"[STDERR] Error opening file '{fname}': {e}", file=sys.stderr)
        print("Data not saved")
        return


if __name__ == "__main__":
    main()
