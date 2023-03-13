import numpy as np

a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
k = int(input().strip())

a = np.array(a)

difference_array = np.absolute(a-k)
index = difference_array.argmin()

print(a[index])
