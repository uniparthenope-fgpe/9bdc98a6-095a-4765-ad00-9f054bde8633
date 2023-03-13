import numpy as np
import ast


def swap_cols(x, col_index1, col_index2):
    x[:, [col_index1, col_index2]] = x[:, [col_index2, col_index1]]


arr = (input())
arr = np.array(ast.literal_eval(arr))

indexes = [int(arr_temp) for arr_temp in input().strip().split(' ')]

idx1 = indexes[0]
idx2 = indexes[1]

swap_cols(arr, idx1, idx2)
print(arr)
