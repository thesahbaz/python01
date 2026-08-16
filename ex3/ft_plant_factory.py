#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, 
            age: int, grow_rate: float) -> None:
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
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Lily", 25.0, 30, 1),
        Plant("Carnation", 200.0, 365, 1),
        Plant("Daisy", 5.0, 90, 1),
        Plant("Rose", 80.0, 45, 1),
        Plant("Fern", 15.0, 120, 1),
    ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()

if __name__ == "__main__":
    main()