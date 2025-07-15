# 4.1.

class Ear:
    def __init__(self, size):
        self._size = size

    def hear(self, sound):
        print(f"Уши слышат звук: {sound}.")


class Animal:
    def __init__(self, age, weight, speed, color):
        self._age = age
        self._weight = weight
        self._speed = speed
        self._color = color
        self._ears = []
        for i in range(2):
            self._ears.append(Ear("средние"))

    def hear(self, sound):
        for ear in self._ears:
            ear.hear(sound)


class Dog(Animal):
    def __init__(self, age, weight, speed, color):
        super().__init__(age, weight, speed, color)
        self.__bite_damage = 15

    def bark(self):
        print("Гав-гав!")

    def bite(self, target):
        print(f"Собака укусила {target} и нанесла {self.__bite_damage} урона.")


class Cat(Animal):
    def __init__(self, age, weight, speed, color):
        super().__init__(age, weight, speed, color)
        self.__claw_damage = 5

    def meow(self):
        print("Мяу-мяу!")

    def scratch(self, target):
        print(f"Кошка поцарапала {target} и нанесла {self.__claw_damage} урона.")


dog = Dog(3, 15, 0, "коричневый")
cat = Cat(2, 4, 0, "серый")

print(f"Собака: возраст {dog._age}, вес {dog._weight} кг, цвет {dog._color}.")
print(f"Кошка: возраст {cat._age}, вес {cat._weight} кг, цвет {cat._color}.")

cat.hear("шуршание")
dog.hear("хозяин")

class Battery:
    def __init__(self, capacity):
        self.__capacity = capacity
        self._charge = capacity

class Device:
    def __init__(self, brand, model, battery):
        self.__brand = brand
        self.__model = model
        self._is_on = False
        self.__battery = battery

    def turn_on(self):
        if self.__battery._charge > 0:
            self._is_on = True
            print(f"{self.__brand} {self.__model} включён.")
        else:
            print(f"{self.__brand} {self.__model} не может быть включён, батарея разряжена.")

    def turn_off(self):
        self._is_on = False
        print(f"{self.__brand} {self.__model} выключен.")


class MobilePhone(Device):
    def __init__(self, brand, model, phone_number, battery):
        super().__init__(brand, model, battery)
        self.__phone_number = phone_number

    def call(self, number):
        if self._is_on:
            print(f"Звоним на номер {number}.")
        else:
            print("Телефон выключен.")

    def sms(self, number, message):
        if self._is_on:
            print(f"Отправляем SMS на номер {number}: {message}.")
        else:
            print("Телефон выключен.")


class Laptop(Device):
    def __init__(self, brand, model, operating_system, battery):
        super().__init__(brand, model, battery)
        self.__operating_system = operating_system

    def run_program(self, program_name):
        if self._is_on:
            print(f"Запущена программа: {program_name}.")
        else:
            print("Ноутбук выключен.")

    def play_game(self, game_name):
        if self._is_on:
            print(f"Запущена игра: {game_name}.")
        else:
            print("Ноутбук выключен.")

zero_battery = Battery(0)
full_battery = Battery(100)
phone = MobilePhone("Samsung", "Galaxy S23", "+78005553535", full_battery)
phone.turn_on()
phone.call("88001234567")
laptop = Laptop("Apple", "MacBook Pro", "macOS", zero_battery)
laptop.turn_on()

# 4.2. Есть два вида полиморфизма: полиморфизм подтипов и параметрический полиморфизм. Первый заключается в том, что при вызове метода у переданного класса, родителем которого является указанный класс, будет вызван именно переопределенный метод дочернего класса. Второй заключается в том, что при передаче в функцию дочернего класса (при этом указание типизацией родительского класса), код будет одинаково работать для всех классов (дочерних или родительского).

# 4.3.
import random


class Animal:
    def foo(self):
        pass


class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")


class Bird(Animal):
    def foo(self):
        print("Птица поет")


def do_something_with_animal(animal: Animal):
    animal.foo()


def fill_animal_list(animal_list: list[Animal]) -> list[Animal]:
    for i in range(len(animal_list)):
        animal_list[i] = None
    for i in range(500):
        if random.randint(0, 1) == 0:
            animal_list.append(Cat())
        else:
            animal_list.append(Bird())
    return animal_list


animals = []
animals = fill_animal_list(animals)

for animal in animals:
    animal.foo()

# Выводится результат функции foo случайного животного из списка. Так получается, потому что в список было случайно добавлено одно из двух животных, и, так как они имеют один и тот же родительский класс и одно и то же название функции, корректно выводится результат функции foo, соответствующий животному, которое было случайно добавлено.
