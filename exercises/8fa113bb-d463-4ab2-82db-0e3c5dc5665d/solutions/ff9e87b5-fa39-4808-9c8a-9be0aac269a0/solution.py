import numpy as np
import ast


def swap_rows(x, row_index1, row_index2):
    x[[row_index1, row_index2]] = x[[row_index2, row_index1]]


arr = (input())
arr = np.array(ast.literal_eval(arr))

indexes = [int(arr_temp) for arr_temp in input().strip().split(' ')]

idx1 = indexes[0]
idx2 = indexes[1]

swap_rows(arr, idx1, idx2)
print(arr)
