import numpy as np


def first_half(x):
    length = len(x)
    first_half = length // 2
    middle_number = np.median(x)
    middle_int_number = int(middle_number)
    middle_index_number = np.where(x == middle_int_number)
    int_middle_index_number = middle_index_number[0]
    number = int_middle_index_number[0]
    if length % 2 == 0:
        return x[:first_half]
    else:
        return x[:number]


x = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])
print(first_half(x))
