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

cars = []
for i in range(1, 11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(registration, max_speed))

race_finished = False

while race_finished == False:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True


print(f"{'Registration':<15}{'Max speed':>12}{'Speed':>10}{'Distance':>12}")
print("-" * 49)
for car in cars:
    print(
        f"{car.registration_number:<15}{car.maximum_speed:>12}{car.current_speed:>10}{car.travelled_distance:>12.1f}")