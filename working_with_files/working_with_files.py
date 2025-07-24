# 3.1.
import random

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


nums = []
for _ in range(2):
    nums.append(random.randint(1, 10))
print(sum_six_numbers(nums, "working_with_files/"))
