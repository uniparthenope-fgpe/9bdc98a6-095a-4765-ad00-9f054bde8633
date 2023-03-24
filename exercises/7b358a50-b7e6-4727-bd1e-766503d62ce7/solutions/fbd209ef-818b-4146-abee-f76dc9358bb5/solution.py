import numpy as np
import scipy.stats as stats


def t_test(x, y):
    """
    Perform a two-sample t-test on two arrays of data.
    """
    t, p = stats.ttest_ind(x, y)
    return t, p


A = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])
B = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])

print(t_test(A, B))
