class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age} days old"
        )

    def grow(self, dh):
        self.height += dh

    def age(self):
        self.age_days += 1


def main():
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
    rose.grow(.8)


if __name__ == "__main__":
    main()
