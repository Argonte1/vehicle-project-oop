from models.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, brand, model, year, route, capacity):
        super().__init__(brand, model, year)
        self.route = route
        self.capacity = capacity

    def get_info(self):
        return super().get_info() + f", маршрут: {self.route}, мест: {self.capacity}"

    def move(self):
        return "Автобус едет по маршруту"
