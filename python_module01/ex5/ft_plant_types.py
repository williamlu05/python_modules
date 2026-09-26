#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        if height < 0:
            print("Error: Height cannot be negative")
            self._height = 0.0
        self._age = age
        if age < 0:
            print("Error: Age cannot be negative")
            self._age = 0

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print(
                f"{self._name}: Error, height can't be negative"
                "\nHeight update rejected"
            )

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days")
        else:
            print(
                f"{self._name}: Error, age can't be negative"
                f"\nAge update rejected"
            )

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self._height += 0.4

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 2)}cm, "
            f"{self._age} days old"
        )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed is True:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = diameter
        self._shade = False

    def produce_shade(self) -> None:
        self._shade = True
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide"
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 2)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = season
        self._nutritional_value = nutritional_value

    def increase_nutritional_value(self) -> None:
        self._nutritional_value += 1

    def grow(self) -> None:
        self._height += 2.1
        self.increase_nutritional_value()

    def age(self) -> None:
        super().age()
        self.increase_nutritional_value()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print("[asking the Rose to bloom]")
    flower.bloom()
    flower.show()

    print("\n=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the Oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(0, 20):
        vegetable.age()
        vegetable.grow()
    vegetable.show()
