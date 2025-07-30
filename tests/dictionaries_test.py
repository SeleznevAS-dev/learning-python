import unittest
import random
from dictionaries.dictionaries import (
    task1_add_keys,
    task1_delete_dictionary,
    task1_fill_dictionary,
    n_values,
)


class DictionariesTests(unittest.TestCase):
    def test_regression_task1(self):
        keys = task1_add_keys()
        self.assertTrue(len(keys) == 100)
        dictionary = task1_fill_dictionary(keys)
        self.assertTrue(len(dictionary.keys()) == 100)
        self.assertTrue(len(dictionary.values()) == 100)
        for key, value in dictionary.items():
            self.assertIsInstance(key, int)
            self.assertIsInstance(value, str)
        dictionary = task1_delete_dictionary(dictionary)
        self.assertEqual(dictionary, {})

    def test_regression_task2(self):
        arr = []

        for _ in range(100):
            arr.append(random.randint(1, 10))
        n = random.randint(1, 10)
        ans_test = []
        for i in range(1, 11):
            if arr.count(i) >= n:
                ans_test.append(i)
        ans = n_values(arr, n)
        self.assertEqual(sorted(ans), ans_test)


if __name__ == "__main__":
    unittest.main()
