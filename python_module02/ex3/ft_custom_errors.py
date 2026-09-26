class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown Water Error") -> None:
        super().__init__(message)


def check_plant(plant_name: str, is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_tank(water_level: int) -> None:
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        check_plant("tomato", True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        check_water_tank(5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_tank(5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_plant_error()
    test_water_error()
    test_garden_errors()
    print("All custom error types work correctly!")
