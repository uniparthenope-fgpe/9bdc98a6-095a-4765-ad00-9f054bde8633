import numpy as np

N = int(input().strip())

if N % 2 == 0:
    arr = np.arange(N)
    arr = arr.reshape(2, -1)

    print(arr)
else:
    print("Wrong input")
