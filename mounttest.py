import unittest
from mounttab2 import parse_mounts

class TestMount(unittest.TestCase):
    """
    our basic test class
    """
    def test_parsemount(self):
        """
        real test
        all begin with test is a testing
        """
        result = parse_mounts()
        self.assertIsInstance(result,list)
        self.assertIsInstance(retult[0],tuple)

    def test_rootext4(self):
        """
        test to find the basic system file
        """
        result = parse_mounts()
        for line in result:
            if line[1] == "/" and line[2] != "rootfs":
                self.assertEqual(line[2],"ext4")

if __name__ == "__main__":
    unittest.main()
