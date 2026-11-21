class Elevator:
    def __init__(self,bottom, top):
        self.bottom=bottom
        self.top=top
        self.current=bottom

    def floor_up(self):
        self.current = self.current + 1
        print(f"Elevator is at floor {self.current}")

    def floor_down(self):
        self.current = self.current - 1
        print(f"Elevator is at floor {self.current}")

    def floors(self, move):
        while self.current < move:
            self.floor_up()
        while self.current > move:
            self.floor_down()

class Building:
    def __init__(self, bottom_floors, top_floors, number_elevators):
        self.elevators = []
        for i in range(number_elevators):
            self.elevators.append(Elevator(bottom_floors, top_floors))

    def run_elevator(self, elevator_number, target_floors):
        elevator = self.elevators[elevator_number - 1]
        elevator.floors(target_floors)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.floors(elevator.bottom)

building = Building(1, 10, 3)

building.run_elevator(1, 5)
building.run_elevator(2, 8)
building.run_elevator(3, 4)

building.fire_alarm()