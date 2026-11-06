from models.car import Car
from models.truck import Truck
from models.motorcycle import Motorcycle
from models.bus import Bus
from garage import Garage


def main():
    car = Car("Toyota", "Camry", 2024, 4)
    truck = Truck("Volvo", "FH", 2022, 20)
    motorcycle = Motorcycle("Yamaha", "MT-07", 2023, False)
    bus = Bus("LiAZ", "5292", 2021, 42, 100)

    print("Проверка методов:")
    car.accelerate(60)
    car.brake(20)
    print(car.get_info())
    car.brake(100)
    print("После сильного торможения:", car.speed)
    car.stop()
    print("После остановки:", car.speed)

    try:
        car.speed = -10
    except ValueError as error:
        print("Ошибка:", error)

    print()
    vehicles = [car, truck, motorcycle, bus]
    for vehicle in vehicles:
        print(vehicle.get_info())
        print(vehicle.move())

    print()
    garage = Garage()
    for vehicle in vehicles:
        garage.add_vehicle(vehicle)

    print("Все в гараже:")
    garage.show_all()

    print()
    print("Поиск по марке Toyota:")
    for vehicle in garage.find_by_brand("Toyota"):
        print(vehicle.get_info())

    garage.remove_vehicle(truck)
    print()
    print("После удаления Volvo:")
    garage.show_all()


if __name__ == "__main__":
    main()
