class Plant:
    class Stats:
        def __init__(self) -> None:
            self._age = 0
            self._grow = 0
            self._show = 0
            self._shade = 0
            self._istree = False

        def increment_age(self) -> None:
            self._age += 1

        def increment_grow(self) -> None:
            self._grow += 1

        def increment_show(self) -> None:
            self._show += 1

        def increment_shade(self) -> None:
            self._shade += 1

        def is_tree(self) -> None:
            self._istree = True

        def show_stats(self) -> str:
            total = (
                f"Stats: {self._grow} grow, "
                f"{self._age} age, {self._show} show"
            )
            if self._istree:
                total += f"\n{self._shade} shade"
            return total

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
        self._stats = Plant.Stats()

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
        self._stats.increment_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.increment_age()

    def show(self) -> None:
        self._stats.increment_show()
        print(
            f"{self._name}: {round(self._height, 2)}cm, "
            f"{self._age} days old"
        )

    def get_stats(self) -> Stats:
        return self._stats

    @staticmethod
    def check_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def grow(self) -> None:
        self._height += 8
        self._stats.increment_grow()

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
        self._stats.is_tree()

    def produce_shade(self) -> None:
        self._stats.increment_shade()
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
        super().grow()
        self._height += 1.7
        self.increase_nutritional_value()

    def age(self) -> None:
        super().age()
        self.increase_nutritional_value()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self) -> None:
        self._bloomed = True
        self._seeds = 42

    def grow(self) -> None:
        self._height += 1.5
        self._stats.increment_grow()


def stats(plant: "Plant") -> None:
    print(plant.get_stats().show_stats())


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    stats(rose)
    print("[asking the Rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    stats(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    stats(oak)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    stats(sunflower)
    print("\n=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    stats(anonymous)
