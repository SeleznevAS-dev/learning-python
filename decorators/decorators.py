# 7.1.
import datetime


def get_time_of_execution(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        finish_time = datetime.datetime.now()
        time_difference = finish_time - start_time
        print("Время выполнения функции:", time_difference)
        return result

    return wrapper


def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print("Во время работы функции произошла ошибка:", e)

    return wrapper


# 7.2.
class Weapon:
    def __init__(self, name, damage, max_ammo):
        self.__name = name
        self.__damage = damage
        self.__max_ammo = max_ammo
        self.__ammo = self.__max_ammo
        self.__durability = 100
        self.__max_durability = 100

    def __fire(self):
        if self.__ammo <= 0:
            print("Нет патронов для выстрела.")
            return 0
        if self.__durability <= 0:
            print("Оружие сломано.")
            return 0

        self.__ammo -= 1
        self.__durability -= 2
        return self.__damage

    @property
    def ammo(self):
        return self.__ammo

    @ammo.setter
    def ammo(self, new_ammo):
        self.__ammo = new_ammo

    @property
    def durability(self):
        return self.__durability

    @durability.setter
    def durability(self, new_durability):
        self.__durability = new_durability


ak47 = Weapon("AK-47", 30, 30)
print("Было патронов:", ak47.ammo)
ak47.ammo = 20
print("Стало патронов:", ak47.ammo)
ak47.durability = 60
print("Новая прочность оружия:", ak47.durability)


# 7.3.
# @staticmethod: работает независимо экземпляров.
# @classmethod: относится к классу, а не к экземплярам класса.
# Разница в том, что staticmethod только логически связан с классом (находится в списке его методов), в нём нет аргумента self, значит в теории его даже можно вынести за предела класса, а classmethod использует аргумент cls, который указывает на этот же класс, но в отличии от обычных методов он не связан с экземплярами.

# 7.4.
from functools import wraps


def invariant(predicate):
    def invariant_decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            assert predicate(self), f"Invariant condition failed {method.__name__}"
            return result

        return wrapper

    return invariant_decorator


class Weapon:
    def __init__(self, name, damage, max_ammo):
        self.__name = name
        self.__damage = damage
        self.__max_ammo = max_ammo
        self.__ammo = self.__max_ammo
        self.__durability = 100
        self.__max_durability = 100

    @property
    def ammo(self):
        return self.__ammo

    @ammo.setter
    def ammo(self, new_ammo):
        self.__ammo = new_ammo

    @invariant(lambda self: self.__ammo >= 0)
    def fire(self, ammo):
        self.__ammo -= ammo
        self.__durability -= 2
        return self.__damage


m4 = Weapon("M4", 35, 30)
# m4.fire(60)  # AssertionError: Invariant condition failed fire


# 7.5
def is_substring(string: str, substring: str) -> bool:
    # 7.5.1 (если бы не было тайпинга), 7.5.6
    assert isinstance(string, str) and isinstance(substring, str), (
        "String and substring must be str"
    )
    # 7.5.3, 7.5.7
    assert string != "", "String must contains at least one symbol"
    if substring == "":
        return True

    for i in range(len(string) - len(substring) + 1):
        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                break

            if j == (len(substring) - 1):
                return True
    return False


string = "123"
substring = "1"
# 7.5.5
assert isinstance(string, str) and isinstance(substring, str), (
    "String and substring must be str"
)
result = is_substring(string, substring)
# 7.5.2, 7.5.4
assert result is not None, "Result should not be None"
print(is_substring("123", "1"))

# 7.6
# Данный вид полиморфизма позволяет коду автоматически "выбирать" поведение при передаче различных типов параметров, не меняя при это название функции.
