# KD_tree/test_kd_tree.py

import unittest
from kd_tree import KDTree

class TestKDTree(unittest.TestCase):
    def setUp(self):
        self.data = [
            [2, 3],
            [5, 4],
            [9, 6],
            [4, 7],
            [8, 1],
            [7, 2]
        ]
        self.kd_tree = KDTree(self.data)

    def test_nearest_neighbor(self):
        point = [9, 2]
        nearest = self.kd_tree.nearest_neighbor(point)
        self.assertEqual(nearest, [8, 1])

        point = [3, 4]
        nearest = self.kd_tree.nearest_neighbor(point)
        self.assertEqual(nearest, [2, 3])

if __name__ == '__main__':
    unittest.main()