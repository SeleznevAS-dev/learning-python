import unittest
import os
import random
from working_with_files.working_with_files import (
    create_files,
    sum_six_numbers,
    create_cats,
)


class WorkingWithFilesTests(unittest.TestCase):
    # 3.1.
    def test_regression_create_files(self):
        create_files()
        for i in range(1, 11):
            self.assertTrue(os.path.exists(f"working_with_files/{i}.txt"))
            with open(f"working_with_files/{i}.txt", "rt") as f:
                for _ in range(3):
                    s = f.readline().rstrip()
                    num = int(s)
                    self.assertTrue(1 <= num)
                    self.assertTrue(num <= 999)

    # 3.2.
    def test_regression_sum_six_numbers(self):
        create_files()

        nums = []
        for _ in range(2):
            nums.append(random.randint(1, 10))

        result = sum_six_numbers(nums, "working_with_files/")

        expected_sum = 0
        for num in nums:
            with open(f"working_with_files/{num}.txt", "rt") as f:
                for _ in range(3):
                    expected_sum += int(f.readline().strip())

        self.assertEqual(result, expected_sum)

    def test_null_sum_six_numbers(self):
        self.assertEqual(sum_six_numbers([], "working_with_files/"), 0)
        with self.assertRaises(FileNotFoundError):
            sum_six_numbers([1, 2], "")

    # 3.3.
    def test_regression_create_cats(self):
        with open("working_with_files/cats.txt", "w", encoding="UTF-8") as f:
            f.write("Барсик 5.0 75\n")
            f.write("Мурка 3.7 80\n")
            f.write("Леопольд 4.7 60\n")
        cats = create_cats()
        self.assertIsInstance(cats, list)
        for cat in cats:
            self.assertTrue(hasattr(cat, "name"))
            self.assertTrue(hasattr(cat, "weight"))
            self.assertTrue(hasattr(cat, "freq"))
            self.assertIsInstance(cat.name, str)
            self.assertIsInstance(cat.weight, float)
            self.assertIsInstance(cat.freq, int)

    def test_null_create_cats(self):
        with open("working_with_files/cats.txt", "wt", encoding="UTF-8") as f:
            f.write("\n")
            f.write("\n")
            f.write("\n")
        cats = create_cats()
        self.assertEqual(cats, [])

    def test_random_create_cats(self):
        for _ in range(100):
            with open("working_with_files/cats.txt", "wt", encoding="UTF-8") as f:
                for _ in range(5):
                    name = f"Кот{random.randint(1, 100)}"
                    weight = random.uniform(1.0, 10.0)
                    freq = random.randint(1, 100)
                    f.write(f"{name} {weight} {freq}\n")
            cats = create_cats()
            self.assertEqual(len(cats), 5)

    def test_min_max_create_cats(self):
        with open("working_with_files/cats.txt", "wt", encoding="UTF-8") as f:
            f.write("Кот 0.1 1\n")
            f.write("Кот 49.9 999\n")
        cats = create_cats()
        self.assertEqual(len(cats), 2)

if __name__ == "__main__":
    unittest.main()
