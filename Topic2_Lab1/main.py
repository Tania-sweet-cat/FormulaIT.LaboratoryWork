import doctest
from typing import Union, Any


class Laptop:
    def __init__(self, brand: str, memory_capacity: int, screen_diagonal: float):
        """
        Создание и подготовка к работе объекта Ноутбук.
        :param brand: Бренд ноутбука.
        :param memory_capacity: Объём памяти ноутбука.
        :param screen_diagonal: Размер диагонали экрана ноутбука.

        Пример:
        >>> laptop = Laptop("MSI", 512, 15.6)
        """
        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть представлено в виде строки.")
        self.brand = brand

        if not isinstance(memory_capacity, int):
            raise TypeError("Объём памяти должен быть представлен целым числом.")
        if memory_capacity <= 0:
            raise ValueError("Объём памяти должен быть больше нуля.")
        self.memory_capacity = memory_capacity

        if not isinstance(screen_diagonal, float):
            raise TypeError("Диагональ ноутбука должна быть представлена вещественным числом.")
        if screen_diagonal <= 0.0:
            raise ValueError("Размер диагонали ноутбука должен быть больше нуля.")
        self.screen_diagonal = screen_diagonal

        self.working_condition = 0

    def power_on(self) -> int:
        """
        Включение ноутбука.

        :return: код ошибки, либо 0 при выполнении без ошибок.

        Пример:
        >>> laptop = Laptop("MSI", 512, 15.6)
        >>> result = laptop.power_on()
        """
        ...

    def is_charging(self) -> bool:
        """
        Проверяет, заряжается ли ноутбук.

        :return: Заряжается ли ноутбук.

        Пример:
        >>> laptop = Laptop("MSI", 512, 15.6)
        >>> is_charging = laptop.is_charging()
        """
        ...

    def connect_to_wifi(self, wifi_name: str, password: str) -> int:
        """
        Осуществляет подключение к сети WIFI.

        :param wifi_name: Название сети WIFI.
        :param password: Пароль к сети WIFI.
        :return: Код ошибки, либо 0 при выполнении без ошибок.
        Пример:
        >>> laptop = Laptop("MSI", 512, 15.6)
        >>> result = laptop.connect_to_wifi("WIFI1", "123456789")
        """
        if not isinstance(wifi_name, str):
            raise TypeError("Название сети WIFI должно быть представлено в виде строки.")
        if not isinstance(password, str):
            raise TypeError("Пароль к сети WIFI должен быть представлен в виде строки.")
        ...


class Cat:
    def __init__(self, name: str, breed: str, age: Union[int, float], color: str):
        """
        Создание и подготовка к работе объекта Кошка.
        :param name: Кличка кошки.
        :param breed: Порода кошки.
        :param age: Возраст кошки.
        :param color: Цвет шерсти кошки.

        Пример:
        >>> cat = Cat("Дуся", "Уличная", 12, "Болотный")
        """
        if not isinstance(name, str):
            raise TypeError("Имя кошки должно быть представлено в виде строки.")
        self.name = name

        if not isinstance(breed, str):
            raise TypeError("Порода кошки должна быть представлена в виде строки.")
        self.breed = breed

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст кошки должен быть представлен в виде целого или вещественного числа.")
        if age <= 0:
            raise ValueError("Возраст кошки должен быть больше нуля.")
        self.age = age

        if not isinstance(breed, str):
            raise TypeError("Цвет шерсти кошки должен быть представлен в виде строки.")
        self.color = color

    def say_meow(self, count: int) -> None:
        """
        Мяуканье необходимое число раз.

        :param count: Количество раз, сколько кошка должна мяукнуть.

        Пример:
        >>> cat = Cat("Дуся", "Уличная", 12, "Болотный")
        >>> cat.say_meow(2)
        """
        if not isinstance(count, int):
            raise TypeError("Количество мяуканья должно быть целым числом.")
        if count <= 0:
            raise ValueError("Количество мяуканья должно быть больше нуля.")
        ...

    def sleep(self, time: Union[int, float]) -> None:
        """
        Функция, отвечающая за сон кошки.

        :param time: Время, на которое кошка должна уснуть.

        Пример:
        >>> cat = Cat("Дуся", "Уличная", 12, "Болотный")
        >>> cat.sleep(4)
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время сна должно быть представлено в виде целого или вещественного числа.")
        if time <= 0:
            raise ValueError("Время сна должно быть больше нуля.")
        if time > 6:
            raise ValueError("Время сна должно быть не больше 6 часов.")
        ...

    def come_to_owner(self) -> int:
        """
        Прийти к хозяину.

        :return: -1 - если невозможно добраться до хозяина, иначе 0.

         Пример:
        >>> cat = Cat("Дуся", "Уличная", 12, "Болотный")
        >>> result = cat.come_to_owner()
        """
        ...


class Stack:
    def __init__(self):
        """
        Инициализирует стек.

        Пример:
        >>> stack = Stack()
        """
        self.list_ = []
        self.size = 0

    def push(self, elem: Any) -> None:
        """
        Добавляет элемент в конец стека.

        :param elem: Элемент, который необходимо добавить в стек.

        Пример:
        >>> stack = Stack()
        >>> stack.push(123)
        >>> stack.push('str')
        """
        ...

    def get_size(self) -> int:
        """
        Возвращает текущее количество элементов в стеке.

        :return: Текущее количество элементов в стеке.

        Пример:
        >>> stack = Stack()
        >>> count = stack.get_size()
        """
        ...

    def pop(self) -> Any:
        """
        Возвращает последний добавленный элемент и удаляет его из стека.

        :return: Последний элемент в стеке.

        Пример:
        >>> stack = Stack()
        >>> stack.push(123)
        >>> elem = stack.pop()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
