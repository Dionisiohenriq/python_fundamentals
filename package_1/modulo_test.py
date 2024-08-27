import unittest
from modulo import sum1


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum1(1, 2), (1 + 2))  # add assertion here


if __name__ == '__main__':
    unittest.main()
