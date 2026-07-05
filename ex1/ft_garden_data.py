#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    plants = [
        Plant("Lily", 24, 2),
        Plant("Carnation", 26, 3),
        Plant("Daisy", 28, 6),
    ]
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
