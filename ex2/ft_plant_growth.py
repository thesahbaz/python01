#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, grow_rate: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age
        self.grow_rate = grow_rate

    def grow(self) -> None:
        self.height = round(self.height + self.grow_rate, 1)

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


def main():
    print("=== Garden Plant Growth ===")
    lily = Plant("Lily", 25.0, 30, 0.8)
    lily.show()
    first_height = lily.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        lily.grow()
        lily.age()
        lily.show()
    print(f"Growth this week: {round(lily.height - first_height, 1)}cm")

if __name__ == "__main__":
    main()
