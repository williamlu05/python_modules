import math


def distance(pos1: tuple[float, float, float],
             pos2: tuple[float, float, float]) -> float:
    total = (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2
    total += (pos1[2] - pos2[2])**2
    return math.sqrt(total)


def to_float(text: str) -> float:
    try:
        return float(text)
    except ValueError as e:
        raise ValueError(f"Error on parameter '{text.strip()}': {e}")


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x, y, z = text.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            return (to_float(x), to_float(y), to_float(z))
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance_center = distance((0, 0, 0), pos1)
    print(f"Distance to center: {round(distance_center, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates:",
        f"{round(distance(pos1, pos2), 4)}"
    )
