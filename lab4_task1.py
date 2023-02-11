import doctest


class Car:
    """Базовый класс"""
    def __init__(self, car_brand: str, max_speed: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param car_brand: Название марки автомобиля
        :param max_speed: Максимальная скорость автомобиля в км/ч
        Пример:
        >>> my_car = ('Hyundai', 220)
        """
        if not isinstance(car_brand, str):
            raise TypeError('Название марки вашего автомобиля должно соответствовать типу str')
        self.car_brand = car_brand
        if not isinstance(max_speed, int):
            raise TypeError('Максимальная скорость вашего автомобиля дожна соответствовать типу int')
        if not max_speed > 0:
            raise ValueError('Максимальная скорость автомобиля должна быть положительным числом')
        self.max_speed = max_speed

    def __str__(self):
        return f"Автомобиль. Марка автомобиля {self.car_brand}. Максимальная скорость {self.max_speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}(car_brand={self.car_brand!r}, max_speed={self.max_speed!r})"


class PassengerCar(Car):
    """ Дочерний класс """
    def __init__(self, car_brand: str, max_speed: int, color: str):
        """
        Создание и подготовка к работе дочернего класса "Легковой автомобиль"
        :param car_brand: Название марки автомобиля
        :param max_speed: Максимальная скорость автомобиля в км/ч
        :param color: Цвет автомобиля
        Пример:
        >>> car = PassengerCar('Lada', 180, 'Чёрный')
        """
        super().__init__(car_brand, max_speed)
        self.color = color
    def __call__(self, new_color):
        """
        Метод производит замену цвета автомобиля, если клиент хочет его изменить
        :param new_color: Новый цвет
        >>> car = PassengerCar('Lada', 180, 'Чёрный')
        >>> car('Красный')
        """
        self.color = new_color

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Цвет автомобиля {self.color}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f"({super_repr}, color={self.color})"


if __name__ == "__main__":
    doctest.testmod()
    pass
