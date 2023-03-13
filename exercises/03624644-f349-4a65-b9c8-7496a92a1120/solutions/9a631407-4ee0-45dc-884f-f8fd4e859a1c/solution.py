import numpy as np

a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
b = [int(arr_temp) for arr_temp in input().strip().split(' ')]

a = np.array(a)
b = np.array(b)

if a.shape == b.shape:
    equal = np.allclose(a, b)
    print(equal)
else:
    print("Wrong input")
