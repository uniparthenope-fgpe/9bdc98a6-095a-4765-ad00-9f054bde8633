import numpy as np

x = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])
y = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])
concat = np.concatenate([x, y])

print(concat)
