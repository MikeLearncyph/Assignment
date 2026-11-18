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

car = Car("AB-123", 142, 60, 2000)
car.drive(1.5)
print(car2.travelled_distance)