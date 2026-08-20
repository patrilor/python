class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_days = age

    def show(self):
        print(
            f"{self.name}: {round(self.height, 2)}cm, "
            f"{self.age_days} days old"
        )

    def grow(self, dh):
        self.height += dh

    def age(self):
        self.age_days += 1


def main():
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    cactus = Plant("Cactus", 24, 7)
    initial_height = rose.height
    initial_heightc = cactus.height
    for day in range(1, 7 + 1):
        rose.grow(.8)
        rose.age()
        cactus.grow(.5)
        cactus.age()
        print(f"=== Day {day} ===")
        rose.show()
        cactus.show()
    final_height = rose.height - initial_height
    final_height1 = cactus.height - initial_heightc
    print("Growth this week: ", round(final_height, 2))
    print("Growth this week: ", round(final_height1, 2))


if __name__ == "__main__":
    main()
