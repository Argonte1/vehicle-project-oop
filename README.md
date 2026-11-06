# vehicle_project

Лабораторная работа № 5 по дисциплине «Введение в информационные технологии».

Тема: объектно-ориентированное программирование в Python.

## Что реализовано

- базовый класс `Vehicle`;
- инкапсуляция скорости через `@property`;
- метод `__str__`;
- наследование и `super()`;
- классы `Car`, `Truck`, `Motorcycle`, `Bus`;
- абстрактный класс `ABC` и метод `move()`;
- полиморфизм;
- класс `Garage` для хранения транспорта;
- функция `main()` и точка входа.

## Структура

```text
vehicle_project/
├── main.py
├── garage.py
└── models/
    ├── __init__.py
    ├── vehicle.py
    ├── car.py
    ├── truck.py
    ├── motorcycle.py
    └── bus.py
```

## Запуск

```bash
python main.py
```

Из папки выше:

```bash
python vehicle_project/main.py
```

## Пример вывода

```text
Все в гараже:
Toyota Camry (2024), 0 км/ч
Volvo FH (2022), 0 км/ч
Yamaha MT-07 (2023), 0 км/ч
LiAZ 5292 (2021), 0 км/ч

Поиск по марке Toyota:
Toyota Camry, 2024 г., скорость: 0 км/ч, дверей: 4
```
