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

h = Elevator(1, 10)
h.floors(5)
h.floors(1)