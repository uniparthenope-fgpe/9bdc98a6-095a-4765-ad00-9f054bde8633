import numpy as np
import ast


def copy_row_k_times(x, row_index, num_copies):
    return x[[row_index] * num_copies]


arr = (input())
arr = np.array(ast.literal_eval(arr))

values = [int(arr_temp) for arr_temp in input().strip().split(' ')]

r = values[0]
n = values[1]

row_k_times = copy_row_k_times(arr, r, n)
print(row_k_times)
