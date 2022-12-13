import doctest


class Backpack:
    def __init__(self, wrap_status: bool, backpack_capacity: (int, float)):
        """
        Создание и подготовка к работе объекта "Рюкзак"
        :param wrap_status: открыт или закрыт рюкзак
        :param backpack_capacity: Вместимость рюкзака в литрах
        Пример:
        >>> my_backpack = Backpack(True, 30) # инициализация экземпляра класса
        """
        if not isinstance(wrap_status, bool):
            raise TypeError("Wrong type wrap_status")
        self.wrap_status = wrap_status

        if not isinstance(backpack_capacity, (int, float)):
            raise TypeError("Wrong type backpack_capacity")
        if not backpack_capacity > 0:
            raise ValueError("Capacity must be positive value")

    def close_backpack(self) -> bool:
        """
        Метод, который закрывает рюкзак
        Если рюкзак был закрыт, тогда получаем сообщение "Рюкзак закрыт"
        :return: bool
        Пример:
        >>> my_backpack = Backpack(True, 140)
        >>> my_backpack.close_backpack()
        """
        ...

    def open_backpack(self) -> bool:
        """
        Метод, который открывает рюкзак
        Если рюкзак был закрыт, тогда получаем сообщение "Рюкзак был открыт"
        Пример:
        >>> my_backpack = Backpack(False, 50)
        >>> my_backpack.open_backpack()
        """
        ...

    def add_things(self, things: (int, float)) -> None:
        """
        Метод добавляет вещи в рюкзак, совокупный объем которых не больше вместимости рюкзака
        :param things: объем вещей
        :raise TypeError: Ошибка, если заданное значеине не соответствует int или float
        :raise ValueError: Ошибка, если объем вещей больше вместимости рюкзака
        :return: None
        Пример:
        >>> my_backpack = Backpack(True, 100)
        >>> my_backpack.add_things(30)
        """
        ...


class Town:
    def __init__(self, area: (int, float), population: int):
        """
        Создание и подготовка к работе объекта "Город"
        :param area: Площадь города в квадратных километрах
        :param population: численность населения в городе
        Пример:
        >>> Chkalovsk = Town(460, 12000)
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Wrong type area")
        if not area > 0:
            raise ValueError("Wrong value area")
        self.area = area

        if not isinstance(population, int):
            raise TypeError("Wrong type population")
        if not population > 0:
            raise ValueError("Wrong value population")
        self.population = population

    def area_reduction(self, decrease_area: (int, float)) -> None:
        """
        Метод, который уменьшает площадь города на значение decrease_area
        :param decrease_area: величина, на которую уменьшается площадь города
        :raise TypeError: Ошибка, если decrease_area не соответсвует int или float
        :raise ValueError: Ошибка, если decrease_area меньше нуля или равно нулю
        :return: None
        Пример:
        >>> Chkalovsk = Town(460, 12000)
        >>> Chkalovsk.area_reduction(30)
        """
        ...

    def area_increase(self, new_area: (int, float)) -> None:
        """
        Метод, который увеличивает площадь города на new_area
        :raise TypeError: Ошибка, если new_area не соответствует int или float
        :raise ValueError: Ошибка, если new_area меньше нуля
        :return: None
        Пример:
        >>> Chkalovsk = Town(430, 12000)
        >>> Chkalovsk.area_increase(100)
        """
        ...

    def census_population(self, new_value_population: int) -> None:
        """
        Метод, который осуществляет перепись населения
        :param new_value_population: новая численность населения
        :raise TypeError: Ошибка, если заданное значение не соответствует int
        :raise ValueError: Ошибка, если заданное значение меньше нуля
        Пример:
        >>> Ckalovsk = Town(530, 12000)
        >>> Ckalovsk.census_population(11985)
        """
        ...


class Car:
    def __init__(self, type_engine: str, horsepower: int):
        """
        Создание и подготовка к работе объекта "Машина"
        :param type_engine: Тип двигателя
        :param horsepower: Количество лошадиных сил
        Пример:
        >>> Lada = Car("Oil", 109)
        """
        if not isinstance(type_engine, str):
            raise TypeError("type_engine")
        if type_engine == '':
            raise ValueError("Type_engine cannot be an empty string")
        self.type_engine = type_engine

        if not isinstance(horsepower, int):
            raise TypeError("Wrong type horsepower")
        if not horsepower > 0:
            raise ValueError("Wrong value horsepower")
        self.horsepower = horsepower

    def chek_engine_type(self, our_type: str) -> bool:
        """
        Метод проверяет соответствие типа двигателя в мащине, со значение которое вы ищите
        :param our_type:
        :raise TypeError: Ошибка возникает, если our_type не соответсвует str
        :raise ValueError: Ошибка возникает, если our_type пустая строка
        :return: bool
        Пример:
        >>> Lada = Car("Oil", 249)
        >>> Lada.chek_engine_type("Electric")
        """
        ...

    def horsepower_tuning(self, magnification_value: int) -> None:
        """
        Метод увеличивает значение лощадиных сио на велечину magnification_value
        :param magnification_value: значение, на которое увеличатся лошадиные силы
        :raise TypeError: Ошибка возникает, если agnification_value не соответствует int
        :raise ValueError: Ошибка возникает, если значение magnification_value меньше или равно нулю
        :return: None
        Пример:
        >>> Kia = Car("Oil", 149)
        >>> Kia.horsepower_tuning(100)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
