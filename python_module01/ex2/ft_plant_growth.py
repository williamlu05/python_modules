class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self):
        self.height += 0.8

    def age(self):
        self.age_days += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 2)} cm, "
            f"{self.age_days} days old"
        )


def ft_plant_growth(plant) -> None:
    print("=== Garden Plant Growth ===")
    plant.show()
    init_height = plant.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        plant.show()
    growth = plant.height - init_height
    print(f"Growth this week: {round(growth, 2)}cm")


if __name__ == "__main__":
    ft_plant_growth(Plant("Rose", 25, 30))
