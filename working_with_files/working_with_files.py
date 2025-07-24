# 3.1.
import random

for i in range(1, 11):
    with open(f"working_with_files/{i}.txt", "w") as file:
        for j in range(3):
            file.write(f"{random.randint(1, 999)}\n")
