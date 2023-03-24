import scipy.stats as stats
import numpy as np


def pearson_corr(x, y):
    """
    Compute the Pearson correlation coefficient between two arrays of data.
    """
    r, _ = stats.pearsonr(x, y)
    return r


A = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])
B = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])

print(pearson_corr(A, B))
