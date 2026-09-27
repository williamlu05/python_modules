import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        count = 1
        while count < len(sys.argv):
            print(f"Argument {count}: {sys.argv[count]}")
            count += 1
    print(f"Total arguments: {len(sys.argv)}")
