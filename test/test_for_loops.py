import unittest
from looping import for_loops

class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(90, for_loops.average([90, 85, 95]))


if __name__ == '__main__':
    unittest.main()
