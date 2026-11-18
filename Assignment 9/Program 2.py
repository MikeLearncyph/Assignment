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

car = Car("ABC-123", 142)
car.accelerate(30)
car.accelerate(50)
car.accelerate(70)
print(f"The car have {car.current_speed} km/h")

car.accelerate(-200)
print(f"Final speed {car.current_speed} km/h")
