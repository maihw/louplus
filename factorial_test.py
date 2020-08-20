import unittest
from factorial import fact
class TestFactorial(unittest.TestCase):
    """
    our basic test class
    """
    def test_fact(self):
        """
        alctually test
        elerything begin test is a testing
        """
        res = fact(5)
        self.assertEqual(res, 120)

if __name__ == "__main__":
    unittest.main()
