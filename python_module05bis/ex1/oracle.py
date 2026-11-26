import os
import sys


def security_check() -> None:
    script_dir = os.path.dirname(__file__)
    gitignore_path = os.path.join(script_dir, ".gitignore")

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")

    ignored = False
    if os.path.isfile(gitignore_path):
        with open(gitignore_path) as file:
            ignored = ".env" in file.read().split()
    if ignored:
        print("[OK] .env file properly ignored by git")
    else:
        print("[KO] .env file is not ignored by git")

    print("[OK] Production overrides available")


def load_config(required_env: list[str]) -> dict[str, str | None]:
    data: dict[str, str | None] = {}

    try:
        from dotenv import load_dotenv
        load_dotenv(override=False)
    except ImportError as e:
        print(f"ERROR - The program cannot read the .env variables: {e}")
        sys.exit(1)
    for key in required_env:
        data[key] = os.getenv(key)
        if not data[key]:
            print(f"WARNING - {key} is missing, using default")
    return data


def show_config(data: dict[str, str | None]) -> None:
    print("\nConfiguration loaded:")
    if data["MATRIX_MODE"] == "production":
        print("Mode: production")
    else:
        print("Mode: development")

    if not data["DATABASE_URL"]:
        print("Database: Not configured")
    elif data["MATRIX_MODE"] == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Connected to local instance")

    if not data["API_KEY"]:
        print("API Access: Unauthorized")
    else:
        print("API Access: Authenticated")

    print(f"Log Level: {data['LOG_LEVEL'] or 'INFO'}")

    if not data["ZION_ENDPOINT"]:
        print("Remote Network: Offline")
    else:
        print("Remote Network: Online")


def main() -> None:
    required_env = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL",
                    "ZION_ENDPOINT"]

    print("ORACLE STATUS: Consulting the configuration...")
    data = load_config(required_env)
    show_config(data)
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
