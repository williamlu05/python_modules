#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        if height < 0:
            print("Error: Height cannot be negative")
            self._height = 0.0
        self._age = age
        if age < 0:
            print("Error: Age cannot be negative")
            self._age = 0

    def set_height(self, height) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(
                "Error, height can't be negative",
                "\nHeight update rejected"
            )

    def set_age(self, age) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(
                f"{self._name}: Error, age can't be negative"
                f"\nAge update rejected"
            )

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> str:
        return (
            f"{self._name}: {round(self._height, 2)} cm, "
            f"{plant._age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.123987123, 10)
    print(f"Plant created: {plant.show()}\n")
    plant.set_height(25)
    plant.set_age(30)
    print("\n")
    plant.set_height(-39)
    plant.set_age(-2)
