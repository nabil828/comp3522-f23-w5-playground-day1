# unit testing
import unittest
from unittest.case import _AssertRaisesContext


def sum(a, b):
    """
    Add a and b
    return a + b

    Args:
        a (int): first number and positive
        b (int): second number and positive
    Exceptions:
         raise ValueError if a or b is negative
    """
    if a < 0 or b < 0:
        raise ValueError("Cannot sum negative numbers")
    return a + b


class TestSum(unittest.TestCase):
    # first unit test
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3, "Should be 3")

    def test_sum2(self):
        try:
            sum(-1, 2)
            self.fail("Should have raised an exception")
        except ValueError as e:
            print(e)
            

    def test_sum3(self):
        with self.assertRaises(ValueError) as e:
            sum(-1, 2)


if __name__ == '__main__':
    unittest.main()
