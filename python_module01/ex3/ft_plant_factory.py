class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 2)}cm, "
            f"{self.age_days} days old"
        )


def create(plant: "Plant") -> None:
    print("Created: ", end="")
    plant.show()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    create(Plant("Rose", 25.0, 30))
    create(Plant("Oak", 200.0, 365))
    create(Plant("Cactus", 5.0, 90))
    create(Plant("Sunflower", 80.0, 45))
    create(Plant("Fern", 15.0, 120))
