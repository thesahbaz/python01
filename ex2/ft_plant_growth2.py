#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, grow_rate: float) -> None:
        self.name = name
        self.height = height
        self.age_days = age
        self.grow_rate = grow_rate

    def grow(self) -> None:
        self.height = round(self.height + self.grow_rate, 1)
    
    def age(self)