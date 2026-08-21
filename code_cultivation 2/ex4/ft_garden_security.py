
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self.set_height(height)
        self._age = 0
        self.set_age(age)

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm")

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")

    def show(self):
        print(
            f"{self.name}: {round(float(self._height), 1)}cm, "
            f"{self._age} days old"
        )


def main():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print("\n")
    rose.set_height(25.0)
    rose.set_age(30)
    print("\n")
    rose.set_height(-4)
    rose.set_age(-5)
    print("\n")
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
