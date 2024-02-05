
import numpy as np

# 创建一个一维数组
a = np.array([1])

# 将这个数组重塑为一个 2x3 的二维数组
a_reshaped = a.reshape(1, 1)
res = np.dot(3,8)
print(res)

print("Original array:\n", a)
print("Reshaped array (2x3):\n", a_reshaped)
