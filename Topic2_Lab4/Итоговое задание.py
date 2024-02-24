class Transport:
    """
    Базовый класс транспортного средства.
    """
    name = 'Транспортное средство'

    def __init__(self, brand: str, model: str, year_of_production: int) -> None:
        """
        Конструктор, где определяются основные значения.

        :param brand: Бренд транспортного средства.
        :param model: Модель транспортного средства.
        :param year_of_production: Год выпуска транспортного средства.

        Атрибут _is_turn_on, отвечающий за то, включено ли транспортное средство,
        был сделан непубличным, так как нужен для внутреннего использования.
        Состояние транспортного средства можно узнать с помощью геттера.

        Пример:
        >>> transport = Transport("Toyota", "X785qR", 2024)
        """
        self.brand = brand
        self.model = model
        self.year_of_production = year_of_production
        self.is_turn_on = False

    @property
    def is_turn_on(self) -> bool:
        """
        Геттер для атрибута _is_turn_on, то есть метод, возвращающий значение
        атрибута _is_turn_on.

        :return: Включено ли транспортное средство.

        Пример:
        >>> transport = Transport("Toyota", "X785qR", 2024)
        >>> print(transport.is_turn_on)
        False
        """
        return self._is_turn_on

    @is_turn_on.setter
    def is_turn_on(self, condition: bool) -> None:
        """
        Сеттер для атрибута _is_turn_on, то есть метод, устанавливающий значение
        атрибута _is_turn_on.

        :param condition: Состояние работы транспортного средства, которое нужно установить.

        Пример:
        >>> transport = Transport("Toyota", "X785qR", 2024)
        >>> transport.is_turn_on = True
        """
        self._is_turn_on = condition

    def __str__(self) -> str:
        """
        Определяет поведение функции str(), вызванной для экземпляра класса.
        Например, print(), f-string и другие.

        :return: Строковое представления объекта, понятное для человека.

        Пример:
        >>> print(Transport("Toyota", "X785qR", 2024))
        Транспортное средство бренда 'Toyota'
        Модель - X785qR
        Год выпуска - 2024
        """
        return f"{self.name} бренда '{self.brand}'\n" \
               f"Модель - {self.model}\n" \
               f"Год выпуска - {self.year_of_production}"

    def __repr__(self) -> str:
        """
        Метод возвращает строку, показывающую, как может быть
        проинициализирован объект.

        :return: Строковое представления объекта, которым можно
        проинициализировать такой же объект.

        Пример:
        >>> transport = Transport("Toyota", "X785qR", 2024)
        >>> print(transport.__repr__())
        Transport(brand='Toyota', model='X785qR', year_of_production=2024)
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, " \
               f"model={self.model!r}, year_of_production={self.year_of_production})"

    def start(self) -> None:
        """
        Метод, ответственный за включение транспортного средства.

        Пример:
        >>> transport = Transport("Toyota", "X785qR", 2024)
        >>> transport.start()
        """
        if not self.is_turn_on:
            self.is_turn_on = True
        ...

    def stop(self) -> None:
        """
        Метод, ответственный за выключение транспортного средства.

        Пример:
        >>> transport = Transport("Toyota", "X785qR", 2024)
        >>> transport.stop()
        """
        if self.is_turn_on:
            self.is_turn_on = False
        ...

    def refuel(self, count: int) -> None:
        """
        Метод, ответственный за заправку транспортного средства топливом
        на volume литров.

        :param count: Количество литров, на которое необходимо заправить.

        Пример:
        >>> transport = Transport("Toyota", "X785qR", 2024)
        >>> transport.refuel(45)
        Транспортное средство заправляется топливом на 45 литров...
        """
        print(f'{self.name} заправляется топливом на {count} литров...')
        ...


class Car(Transport):
    """
    Класс, описывающий машину. Дочерний класс транспортного средства.
    """
    name = 'Машина'
    fuel = 'Бензин'

    def __init__(self, brand: str, model: str, year_of_production: int,
                 body_type: str, num_doors: int) -> None:
        """
        Конструктор, где вызывается конструктор базового класса, а также
        определяются некоторые дополнительные параметры машины.

        :param brand: Бренд транспортного средства.
        :param model: Модель транспортного средства.
        :param year_of_production: Год выпуска транспортного средства.
        :param body_type: Тип кузова.
        :param num_doors: Количество дверей.

        Пример:
        >>> car = Car("Volkswagen", "Tiguan", 2007, "Кроссовер", 5)
        """
        super().__init__(brand, model, year_of_production)
        self.body_type = body_type
        self.num_doors = num_doors

    def __str__(self) -> str:
        """
        Определяет поведение функции str(), вызванной для экземпляра класса.
        Например, print(), f-string и другие.

        :return: Строковое представления объекта, понятное для человека.

        Пример:
        >>> print(Car("Volkswagen", "Tiguan", 2007, "Кроссовер", 5))
        Машина бренда 'Volkswagen'
        Модель - Tiguan
        Год выпуска - 2007
        Тип кузова - Кроссовер
        Количество дверей - 5
        """
        return super().__str__() + f"\nТип кузова - {self.body_type}\n" \
                                   f"Количество дверей - {self.num_doors}"

    def __repr__(self) -> str:
        """
        Метод возвращает строку, показывающую, как может быть
        проинициализирован объект.

        :return: Строковое представления объекта, которым можно
        проинициализировать такой же объект.

        Пример:
        >>> car = Car("Volkswagen", "Tiguan", 2007, "Кроссовер", 5)
        >>> print(car.__repr__())
        Car(brand='Volkswagen', model='Tiguan', year_of_production=2007,body_type='Кроссовер', num_doors=5)
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, " \
               f"model={self.model!r}, year_of_production={self.year_of_production}," \
               f"body_type={self.body_type!r}, num_doors={self.num_doors})"

    def refuel(self, count: int):
        """
        Метод, ответственный за заправку машины бензином на volume литров.
        Метод перегружается, так как при реализации заправки для машины есть нюансы,
        которые не будут рассматриваться в одноимённом обобщённом методе родительского
        класса.

        :param count: Количество литров, на которое необходимо заправить.

        Пример:
        >>> car = Car("Volkswagen", "Tiguan", 2007, "Кроссовер", 5)
        >>> car.refuel(10)
        Машина заправляется топливом 'Бензин' на 10 литров...
        """
        print(f'{self.name} заправляется топливом {self.fuel!r} на {count} литров...')
        ...
