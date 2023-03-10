import numpy as np

values = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr = np.array(values)
arr = arr[arr % 2 == 1]

print(arr)
