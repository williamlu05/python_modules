import os
import site
import sys


def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def show_open_laboratory() -> None:
    print("LABORATORY STATUS: You are working in the open\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print()
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate  # On Unix")
    print("lab_env\\Scripts\\activate     # On Windows")
    print()
    print("Then run this program again.\n")
    print("Reagent installation path:")
    for path in site.getsitepackages():
        if os.path.isdir(path):
            print(f"  {path}")


def show_sealed_laboratory() -> None:
    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting")
    print("the global system.")
    print()
    print("Reagent installation path:")
    for path in site.getsitepackages():
        if os.path.isdir(path):
            print(f"  {path}")


if __name__ == "__main__":
    if in_virtual_env():
        show_sealed_laboratory()
    else:
        show_open_laboratory()
