import importlib
import sys


REAGENTS: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
}


def check_reagent(name: str, purpose: str) -> bool:
    try:
        module = importlib.import_module(name)
    except ImportError:
        print(f"[MISSING] {name} - not installed")
        return False
    version = getattr(module, "__version__", "unknown")
    print(f"[OK] {name} ({version}) - {purpose}")
    return True


def explain_pip_vs_poetry() -> None:
    print("pip vs Poetry:")
    print("requirements.txt declares what to install; pip resolves it "
          "at install time.")
    print("pyproject.toml declares the same constraints, and Poetry pins "
          "the resolved")
    print("versions in poetry.lock so every install is identical.")


def show_install_help(missing: list[str]) -> None:
    print(f"Missing reagents: {', '.join(missing)}")
    print("Install them with pip (inside a virtual environment):")
    print("  pip install -r ex0/requirements.txt")
    print("Or with Poetry (from inside ex0/):")
    print("  poetry install")
    print("  poetry run python loading.py")


if __name__ == "__main__":
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    missing = [name for name, purpose in REAGENTS.items()
               if not check_reagent(name, purpose)]
    print()
    print(f"Running from: {sys.prefix}")
    print()
    explain_pip_vs_poetry()
    print()
    if missing:
        show_install_help(missing)
    else:
        print("All reagents present and accounted for.")
