import numpy as np

N = int(input().strip())

arr = np.arange(N)

arr = np.percentile(arr, 50)

print(arr)
