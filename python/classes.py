from utils import start_section


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def some_method(self):
        print(f"x is {self.x}")


start_section("Point")
p = Point(10, 20)
print(f"x: {p.x}")
print(f"y: {p.y}")
p.some_method()


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False

        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


start_section("Flight")
f = Flight(3)
passengers = ["María", "Luis", "Laura", "Pedro"]
for passenger in passengers:
    if f.add_passenger(passenger):
        print(f"{passenger} added to flight")
    else:
        print(f"{passenger} could not be added to flight")
