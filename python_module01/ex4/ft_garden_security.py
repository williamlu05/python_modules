#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        if height < 0:
            print("Error: Height cannot be negative")
            self._height = 0.0
        self._day = day
        if day < 0:
            print("Error: Age cannot be negative")
            self._day = 0

    def set_height(self, height) -> None:
        if (height >= 0):
            self.height = height
            print(f"Height updated: {height}cm")
        else:
            print(
                "Error, height can't be negative",
                "\nHeight update rejected"
            )

    def set_age(self, age) -> None:
        if (age >= 0):
            self.age = age
            print(f"Age updated: {age} days")
        else:
            print(
                f"{self.name}: Error, age can't be negative"
                f"\nAge update rejected"
            )

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age


def show(plant) -> str:
    return (
        f"{plant.name}: {round(plant.height, 2)} cm, "
        f"{plant.age} days old"
    )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.123987123, 10)
    print(f"Plant created: {show(plant)}\n")
    plant.set_height(25)
    plant.set_age(30)
    print("\n")
    plant.set_height(-39)
    plant.set_age(-2)
