from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        if self.has_sidecar:
            sidecar = "есть"
        else:
            sidecar = "нет"
        return super().get_info() + ", коляска: " + sidecar

    def move(self):
        return "Мотоцикл едет по дороге"
