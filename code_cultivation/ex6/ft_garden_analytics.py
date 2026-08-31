class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, {self._show_count} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)
        self.stats = self.Stats()

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = (name)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = (height)

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age

    def age(self) -> None:
        self.stats._age_count += 1
        self.set_age(self._age + 1)

    def grow(self, dh: float) -> None:
        self.stats._grow_count += 1
        self.set_height(self._height + dh)

    def show(self) -> None:
        self.stats._show_count += 1
        print(
            f"{self._name}: {round(float(self._height), 1)}cm, "
            f"{self._age} days old"
        )

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 seed: int) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of {self._height}cm long "
            f"and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(
            f" Harvest season: {self.harvest_season}\n"
            f" Nutritional value: {self.nutritional_value}"
            )


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print(f"[asking the {rose.get_name()} to grow and bloom]")
    rose.bloom()
    rose.show()
    print(f" [statistics for {rose.get_name()}]")
    rose.stats.display()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[asking the {oak.get_name()} to produce shade]")
    oak.produce_shade()
    print()
    print("=== Seed")
    Sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    Sunflower.show()
    print(f"[make {Sunflower.get_name()} grow, age and bloom]")
    Sunflower.bloom()
    Sunflower.grow(30)
    for _ in range(20):
        Sunflower.age()
    Sunflower.bloom()
    Sunflower.show()
    print(f"[statistics for {Sunflower.get_name()}]")
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()


if __name__ == "__main__":
    main()
