#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, grow_rate: float) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.grow_rate = grow_rate

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self.grow_rate, 1)

    def age(self) -> None:
        self._age += 1

    def valid(self, value) -> bool:
        return value >= 0

    def set_height(self, new_height) -> None:
        if self.valid(new_height):
            self._height = new_height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age) -> None:
        if self.valid(new_age):
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> float:
        return self._age

def main():
    print("=== Garden Security System ===")
    lily = Plant("Lily", 15.0, 10, 0.8)
    print("Plant created: ", end="")
    lily.show()
    print()
    lily.set_height(25)
    lily.set_age(30)
    print()
    lily.set_height(-5)
    lily.set_age(-3)
    print()
    print("Current state: ", end="")
    lily.show()

if __name__ == "__main__":
    main()
