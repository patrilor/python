def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature > 40:
        raise ValueError(
            f"{temperature}°C is too hot for plants (max 40ºC)"
        )
    if temperature < 0:
        raise ValueError(
            f"{temperature}ºC is too cold for plants (min 0ºC)"
        )
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    for data in ("25", "abc", "100", "-50"):
        print(f"Input data is '{data}'")
        try:
            temperature = input_temperature(data)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

