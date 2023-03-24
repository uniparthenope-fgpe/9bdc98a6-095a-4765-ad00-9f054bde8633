import numpy as np
import scipy.stats as stats


def linear_regression(x, y):
    """
    Fit a linear regression model to two arrays of data.
    """
    slope, intercept, r_value, _, _ = stats.linregress(x, y)
    return slope, intercept, r_value


A = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])
B = np.array([int(arr_temp) for arr_temp in input().strip().split(' ')])

print(linear_regression(A, B))
