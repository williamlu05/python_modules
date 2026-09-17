class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self):
        self.height += 0.8

    def age(self):
        self.age_days += 1

    def show(self) -> str:
        return (
            f"{self.name}: {round(self.height, 2)} cm, "
            f"{self.age_days} days old"
        )


def create(plant) -> None:
    print(f"Created: {plant.show()}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    create(Plant("Rose", 25, 30))
    create(Plant("Oak", 200, 365))
    create(Plant("Cactus", 5, 90))
    create(Plant("Sunflower", 80, 45))
    create(Plant("Fern", 15, 120))
