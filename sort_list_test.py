import unittest
import random
from sort_list import sort_list


class SortListTests(unittest.TestCase):
    def test_regression(self):
        self.assertEqual(sort_list([3, 2, 1]), [1, 2, 3])
        self.assertEqual(sort_list([3, 2, 4, 1, 6, 5]), [1, 2, 3, 4, 5, 6])

    def test_random(self):
        arr = []
        for i in range(1000):
            arr.append(random.randint(-1000, 1000))
        self.assertEqual(sort_list(arr), sorted(arr))

    def test_null(self):
        self.assertEqual(sort_list([]), [])
        self.assertEqual(sort_list([0]), [0])
        self.assertEqual(sort_list([0, 0, 0]), [0, 0, 0])

    def test_max(self):
        arr = [
            -2245342365676756321231236784520313534,
            -22453423656767563212312367845203135341,
            874361834329438501392595239434943041,
            762632351487478372310384939232938453,
        ]
        self.assertEqual(
            sort_list(arr),
            [
                -22453423656767563212312367845203135341,
                -2245342365676756321231236784520313534,
                762632351487478372310384939232938453,
                874361834329438501392595239434943041,
            ],
        )


if __name__ == "__main__":
    unittest.main()
