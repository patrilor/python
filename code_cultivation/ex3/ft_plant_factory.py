class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age_days} days old"
        )

    def grow(self, dh: float) -> None:
        self.height += dh

    def age(self) -> None:
        self.age_days += 1


def main() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    flowers = [rose, oak, cactus, sunflower, fern]
    for n in flowers:
        print("Created: ", end="")
        n.show()


if __name__ == "__main__":
    main()
