class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 2)}cm, "
            f"{self.age_days} days old"
        )

    def grow(self, dh: float) -> None:
        self.height += dh

    def age(self) -> None:
        self.age_days += 1


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    initial_height = rose.height
    rose.show()
    for day in range(1, 7 + 1):
        rose.grow(.8)
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()
    final_height = rose.height - initial_height
    print(f"Growth this week:  {round(final_height, 2)}cm")


if __name__ == "__main__":
    main()
