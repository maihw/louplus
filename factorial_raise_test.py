import unittest
from factorial import fact, div

class TestFactorial(unittest.TestCase):
    """
    our basic test class
    """
    def test_fact(self):
        """
        real test
        begin with test is a testing
        """
        res = fact(5)
        self.assertEqual(res, 120)
    def test_error(self):
        """
        test error when run
        """
self.assertRaises(ZeroDivisionError, div, 0)

if __name__ == "__main__":
    unittest.main()
