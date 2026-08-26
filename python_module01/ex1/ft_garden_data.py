class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def show(plant) -> None:
    print(plant.name + ":", plant.height, "cm,", plant.age, "days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    show(Plant("Rose", 25, 30))
    show(Plant("Sunflower", 80, 45))
    show(Plant("Cactus", 15, 120))


if __name__ == "__main__":
    ft_garden_data()
