def secure_archive(file_name: str, operation: str = "r",
                   text: str = "") -> tuple[bool, str]:
    if operation not in ["r", "w"]:
        return (False, "Not a valid file operation")

    try:
        with open(file_name, operation) as file:
            if operation == "r":
                return (True, file.read())
            else:
                file.write(text)
                return (True, "Content successfully written to file")
    except (OSError, UnicodeDecodeError) as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("hola"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    file_result = secure_archive("ancient_fragment.txt")
    print(file_result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("resultado.txt", "w", file_result[1]))
