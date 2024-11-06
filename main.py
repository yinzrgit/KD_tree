# KD_tree/main.py

from kd_tree import KDTree

# 示例数据
data = [
    [3, 7],
    [2, 6],
    [0, 5],
    [1, 8],
    [7, 5],
    [5, 4],
    [6, 7]
]

# 构建KD树
kd_tree = KDTree(data)


# 查找最近邻
point = [6, 5]
nearest = kd_tree.nearest_neighbor(point)
print(f"点 {point} 的最近邻是 {nearest}")