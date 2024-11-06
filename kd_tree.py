# KD_tree/kd_tree.py

import numpy as np # type: ignore
import sys

class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, data):
        self.k = len(data[0])  # 维度
        self.root = self.build_tree(data)
    
    # 递归构建KD树
    def build_tree(self, data, depth=0):
        if not data:
            return None

        axis = depth % self.k
        data.sort(key=lambda x: x[axis])
        median = len(data) // 2

        return Node(
            point=data[median],
            left=self.build_tree(data[:median], depth + 1),
            right=self.build_tree(data[median + 1:], depth + 1)
        )
    #  递归查找最近邻
    def _nearest(self, root, point, depth, best):
        if root is None:
            return best

        axis = depth % self.k
        next_best = None
        next_branch = None

        if best is None or np.linalg.norm(np.array(point) - np.array(root.point)) < np.linalg.norm(np.array(point) - np.array(best.point)):
            next_best = root
        else:
            next_best = best

        if point[axis] < root.point[axis]:
            next_branch = root.left
            other_branch = root.right
        else:
            next_branch = root.right
            other_branch = root.left

        best = self._nearest(next_branch, point, depth + 1, next_best)
        if np.linalg.norm(np.array(point) - np.array(best.point)) > abs(point[axis] - root.point[axis]):
            best = self._nearest(other_branch, point, depth + 1, best)

        return best
    #   查找最近邻
    def nearest_neighbor(self, point):
        return self._nearest(self.root, point, 0, None).point
    
    
