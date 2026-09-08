#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.set_height(height)
        self.set_age(age)

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

    def grow(self) -> None:
        self.height += 0.4

    def age_days(self) -> None:
        self.age += 1

    def show(self) -> str:
        return (
            f"{self.name}: {round(self.height, 2)} cm, "
            f"{self.age} days old"
        )


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        print(super().show())
        print(f"Color {self.color}")
        if self.bloomed is True:
            print(f"{self.name} is blooming beautifully")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, diameter):
        super().__init__(name, height, age)
        self.diameter = diameter
        self.shade = False

    def produce_shade(self) -> None:
        self.shade = True
        print(
            f"{self.name} now produces a shade of"
            f"{self.height}cm long and {self.diameter}cm wide"
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.diameter, 2)}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, season, nutritional_value):
        super().__init__(name, height, age)
        self.season = season
        self.nutritional_value = nutritional_value

    def increase_nutritional_value(self) -> None:
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print(f"[asking the {flower.name} to bloom]")
    flower.bloom()
    flower.show()

    print("\n=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    print(f"make {vegetable.name} grow and age for 20 days")
    for i in range(0, 20):
        vegetable.age_days()
        vegetable.grow()
        vegetable.increase_nutritional_value()
