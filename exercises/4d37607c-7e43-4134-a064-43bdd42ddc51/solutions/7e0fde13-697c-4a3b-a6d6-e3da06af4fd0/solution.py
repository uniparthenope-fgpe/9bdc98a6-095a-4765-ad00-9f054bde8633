import numpy as np

a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
k = int(input().strip())

a = np.array(a)

res = np.argpartition(a, k)

print(a[res[:k]])
