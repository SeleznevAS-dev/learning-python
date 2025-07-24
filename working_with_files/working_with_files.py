# 3.1.
import random


def create_files():
    for i in range(1, 11):
        with open(f"working_with_files/{i}.txt", "wt") as file:
            for j in range(3):
                file.write(f"{random.randint(1, 999)}\n")


# 3.2.
import random


def sum_six_numbers(nums: list[int], path: str):
    sm = 0
    for i in range(len(nums)):
        path_to_file = f"{path}{nums[i]}.txt"
        with open(path_to_file, "rt") as f:
            try:
                for j in range(3):
                    s = f.readline().rstrip()
                    sm += int(s)
                assert j == 2
            except AssertionError:
                return f"Длина файла {path_to_file} не соответствует требуемой"
            except ValueError:
                return f"Файл {path_to_file} испорчен"
    return sm

def sum_six_numbers_main():
    nums = []
    for _ in range(2):
        nums.append(random.randint(1, 10))
    print(sum_six_numbers(nums, "working_with_files/"))


# 3.3.


def create_cats():
    class Cat:
        def __init__(self, name, weight, freq):
            self.name = name
            self.weight = weight
            self.freq = freq

    path = "working_with_files/cats.txt"
    with open(path, "rt", encoding="UTF-8") as f:
        s = f.readline()
        while s != "":
            attrs = s.split(" ")
            try:
                for i in range(len(attrs)):
                    if i == 0:
                        name = str(attrs[i])
                    if i == 1:
                        weight = float(attrs[i])
                        if weight <= 0 or weight >= 50:
                            raise ValueError
                    if i == 2:
                        freq = int(attrs[i])
                        if freq <= 0 or freq >= 1000:
                            raise ValueError
                assert i == 2
                cat = Cat(name, weight, freq)
                print(cat.name, cat.weight, cat.freq)
            except AssertionError:
                print("Количество атрибутов не равно 3")
            except ValueError:
                print("Заданы некорректные параметры")

            s = f.readline()
