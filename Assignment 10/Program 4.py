import random

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = (0)):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_speed):
        self.current_speed = change_speed + self.current_speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,hours):
        distance = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + distance

class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.kilometers = kilometers
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.kilometers:
                return True
        return False

    def print_status(self):
        print(f"{'Registration':<15}{'Max speed':>12}{'Speed':>10}{'Distance':>12}")
        print("-" * 49)
        for car in self.cars:
            print(f"{car.registration_number:<15}{car.maximum_speed:>12}{car.current_speed:>10}{car.travelled_distance:>12.1f}")

cars = []
for i in range(1, 11):
    cars.append(Car(f"ABC-{i}", random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours = hours + 1
    if hours % 10 == 0:
        print(f"\nAfter {hours} hours:")
        race.print_status()

print(f"\nFinal status after {hours} hours:")
race.print_status()