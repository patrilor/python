

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def show(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def grow(self, growth_rate: float = 1.0) -> None:
        self._height += growth_rate
        self._stats.add_grow()

    def age(self, days: int = 1) -> None:
        self._age += days
        self._stats.add_age()

    def show(self) -> None:
        self._stats.add_show()
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def display_all_stats(self) -> None:
        self._stats.show()


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def grow(self, growth_rate: float = 8.0) -> None:
        super().grow(growth_rate)

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def display_all_stats(self) -> None:
        super().display_all_stats()
        print(f"{self._shade_calls} shade")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def grow(self, growth_rate: float = 30.0) -> None:
        Plant.grow(self, growth_rate)

    def age(self, days: int = 20) -> None:
        super().age(days)

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_plant_stats(plant: Plant) -> None:
    plant.display_all_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print(f"[statistics for {rose._name}]")
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print(f"[statistics for {rose._name}]")
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[statistics for {oak._name}]")
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak._name}]")
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print(f"[statistics for {sunflower._name}]")
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print(f"[statistics for {anonymous._name}]")
    display_plant_stats(anonymous)
