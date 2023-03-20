import numpy as np
import scipy

p1 = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])
p2 = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])

dist = np.linalg.norm(p2 - p1)
print(dist)
