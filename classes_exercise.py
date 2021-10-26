# classes_exercise.py

"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""

# My code


class Vehicle:
    """Represents a vehicle

    Attributes:
        name: str
        max_speed: int
        capacity: int
    """

    def __init__(self):
        """Creates a new vehicle with default value"""
        self.name = "v"
        self.max_speed = 200
        self.capacity = 5

    def vroom(self) -> str:
        """'Vroom' {max_speed} times"""
        return "Vroom\n" * self.max_speed


class Bus(Vehicle):
    """represents a price which is an int

    Attributes:
        age: an int indicating the age
    """

    def __init__(self, age: int = 5):
        """Creates a price when age is 5"""
        # Call the superclass constructor
        super().__init__()

        self.age = age
        self.bus_fare = 5

    def fare(self) -> str:
        """Return the price of this age"""
        if 18 <= self.age <= 60:
            return f"The fare of the bus ride is {self.bus_fare}."
        else:
            return "The fare of the bus ride is free."


some_vehicle = Vehicle()
print(some_vehicle.vroom())

some_bus = Bus(5)
print(some_bus.fare())
