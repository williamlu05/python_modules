class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def show(plant) -> str:
    return (
        f"{plant.name}: {round(plant.height, 2)} cm, "
        f"{plant.age} days old"
    )

def create(plant) -> None:
    print(f"Created: {show(plant)}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    create(Plant("Rose", 25, 30))
    create(Plant("Oak", 200, 365))
    create(Plant("Cactus", 5, 90))
    create(Plant("Sunflower", 80, 45))
    create(Plant("Fern", 15, 120))