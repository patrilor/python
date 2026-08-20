
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

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error: age can't be negative")
            print("Age update rejected")
            return
        self._age = age

    def show(self):
        print(
            f"Plant created: {self.name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )


def main():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    print("\n")
    print("Height updated: 25cm")
    print("Age updated: 30 days")
    print("\n")
    rose = Plant("Rose", -4, 11)
    rose = Plant("Rose", 4, -5)
    print("\n")
    

if __name__ == "__main__":
    main()
