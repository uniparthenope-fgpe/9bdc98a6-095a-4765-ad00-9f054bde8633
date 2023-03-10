import numpy as np

length = int(input().strip())
start = int(input().strip())
step = int(input().strip())

end = start + (step*length)
arr = np.arange(start, end, step)

print(arr)
