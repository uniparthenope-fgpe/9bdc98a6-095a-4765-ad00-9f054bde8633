import numpy as np

N = int(input().strip())

stride_len = 2
window_len = 4

a = np.arange(N)

n_strides = ((a.size-window_len)//stride_len) + 1

res = np.array([a[s:(s+window_len)] for s in np.arange(0, n_strides*stride_len, stride_len)])

print(res)
