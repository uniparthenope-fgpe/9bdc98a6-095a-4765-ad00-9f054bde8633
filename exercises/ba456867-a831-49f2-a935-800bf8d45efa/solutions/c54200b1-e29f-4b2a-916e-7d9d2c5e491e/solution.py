import numpy as np

a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = np.array(a)

doublediff = np.diff(np.sign(np.diff(a)))
peak_locations = np.where(doublediff == -2)[0] + 1

print(peak_locations)
