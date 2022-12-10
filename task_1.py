import doctest


class Backpack:  # TODO Написать 3 класса с документацией и аннотацией типов
    def __int__(self, wrap_status: bool, backpack_capacity: (int, float)):
        """

        Создани и подготовка к работе объекта "Рюкзак"
        :param wrap_status: открыт или закрыт рюкзак
        :param backpack_capacity: вместимость рюкзака(в литрах)

        примеры:

        >>> my_backpack = Backpack(0, 30)
        """

        if not isinstance(backpack_capacity, (int, float)):
            raise TypeError("Wrong type capacity")
        if not backpack_capacity > 0:
            raise ValueError("Wrong value capacity")
        self.backpack_capacity = backpack_capacity
        if (wrap_status != 0) and (wrap_status != 1):
            raise ValueError("Your backpack must be closed(0) or open(1)")
        self.wrap_status = wrap_status

    def close_backpack(self) -> bool:
        """

        Если рюкзак был открыт, тогда функция закрывает его
        Если рюкзак был закрыт, тогда получаем сообщение "Рюкзак закрыт"
        :raise ValueError: возвращает ошибку, если рюкзак изначально был закрыт
        Пример:

        >>> my_backpack = Backpack(0,13)
        >>> my_backpack.close_backpack()
        """

    ...

    def open_backpack(self) -> bool:
        """
        Если рюкзак был закрыт, тогда функция открывает его
        Если рюкзак был открыт, тогда получаем сообщение "Рюкзак открыт"
        :raise ValueError: возвращает ошибку, если рюкзак изначально был открыт
        Примеры:

        >>> my_backpack = Backpack(0, 100)
        >>> my_backpack.close_backpack()
        """

    ...

    def add_things(self, things: (int, float)) -> None:
        """

        Функция добавляет вещи в рюкзак, совокупный объем которых не больше вместимости рюкзака
        :param things: объем вещей
        :raise ValueError: вернет ошибку, если попытаться переполнить рюкзак
        :return: вернёт число занятого объема
        Примеры:
        >>>my_backpack = Backpack(1,150)
        >>>my_backpack.add_things(30)
        """


class Town:
    def __int__(self, area: (int, float), population: int):
        """
        Создание и подготовка к работе объекта "Город"
        :param area: площадь города в квадратных километрах
        :param population: численность населения в городе

        Пример:

        >>> Chkalovsk = (460, 12000)
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
        Данный метод уменьшает площадь города на значение decrease_area
        :param decrease_area: площадь, на которую город уменьшается
        :raise TypeError: возникает ошибка, если значение не соответсвует int или float
        :return: возвращает уменьшенную площадь города

        Примеры:

        >>> Chkalovsk = Town(460, 12000)
        >>> Chkalovsk.area_reduction(40)
        """
        ...

    def area_increase(self, new_area: (int, float)) -> None:
        """
        Данный метод увеличивает площадь города на значение new_area
        :param new_area: площадь, на которую город увеличивается
        :raise TypeError: Возникает ошибка, если значение не соответсвует int или float
        :return: возвращает увеличенную площадь города

        Примеры:
        >>> Chkalovsk = Town(460, 12000)
        >>> Chkalovsk.area_increase(30)

        """
        ...

    def census_population(self, new_value_population: int) -> None:
        """
        Данный метод осуществляет перепись населения
        :param new_value_population: новое значение населения
        :raise TypeError: возникает ошибка, если значение не соответствует int
        :return: возвращает новое значение населения

        Примеры:
        >>> Chkalovsk = Town(420, 12000)
        >>> Chkalovsk.census_population(11985)

        """
        ...


class Car:
    def __int__(self, type_engine: str, four_wheel_drive: bool, horsepower: (int, float)):
        """
        Создание и подготовка к работе объкта "Машина"
        :param type_engine: вид двигателя
        :param four_wheel_drive: есть ли полный привод у машины
        :param horsepower: количество лощадиных сил

        Примеры:

        >>> Lada = Car("Oil", 0, 109)

        """
        if not isinstance(type_engine, str):
            raise TypeError("Engine type must be a string")
        self.type_engine = type_engine
        if (four_wheel_drive != 1) and (four_wheel_drive != 0):
            raise TypeError("Your car mast have(1) four_wheel_drive or not(0)")
        self.four_wheel_drive = four_wheel_drive
        if not isinstance(horsepower, (int, float)):
            raise TypeError("Wrong type horsepower")
        if not horsepower > 0:
            raise ValueError("Wrong value horsepower")
        self.horsepower = horsepower

    def engine_type_check(self, our_type: str) -> bool:
        """
        Метод проверяет соответствие типа двигателя в машине, со значением которое вы ищите
        :param our_type: значение, которое я выбираю
        :raise TypeError: ошибка возникает, если значение our_type не соответсвует string
        :return: возвращает True, если значение совпадает, возвращает False, если значение не совподает

        Примеры:
        >>> Lada = Car("Oil", 1, 70)
        >>> Lada.engine_type_check("electric")

        """
        ...

    def is_four_wheel_drive(self) -> bool:
        """
        Метод проверяет, есть ли у машины полный привод, или нет
        :return: возвращает True, если есть полный привод, False, если нет полного привода

        Примеры:

        >>> Tesla = Car("Electric", 1, 249)
        >>> Tesla.is_four_wheel_drive()

        """
        ...

    def horsepower_tuning(self, magnification_value: int) -> None:
        """
        Метод увеличивает значение лошадиных сил на величину magnification_value
        :param magnification_value: значение, на которое увеличатся лошадиные силы
        :raise TypeError: ошибка возникает, если magnification_value не соответствует int
        :return: возвращает новое значение лошадиных сил

        Примеры:

        >>> Kia = Car("Oil", 0, 149)
        >>> Kia.horsepower_tuning(100)

        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
