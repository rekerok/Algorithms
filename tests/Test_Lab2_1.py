import random
import unittest

from Lab1 import lab1
from Lab2 import lab2


class Test_Lab2_1(unittest.TestCase):
    min = 0
    max = 100
    len = 100

    def test_binary_search(self):
        arr = lab1.generate_list_range(self.min, self.max, self.len)
        item = random.randint(self.min, self.max)
        self.assertEqual(lab2.binary_search(arr, item), item in arr)

    def test_interpolation_search(self):
        arr = lab1.generate_list_range(self.min, self.max, self.len)
        item = random.randint(self.min, self.max)
        self.assertEqual(lab2.interpolation_search(arr, item), item in arr)


if __name__ == "__main__":
    unittest.main()
