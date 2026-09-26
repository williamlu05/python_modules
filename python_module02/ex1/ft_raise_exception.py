def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    if temperature > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    return temperature


def test_temperature() -> None:
    for temp_str in ["25", "abc", "100", "-50"]:
        print(f"Input data is '{temp_str}'")
        try:
            temperature = input_temperature(temp_str)
            print(f"Temperature is now {temperature}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
