import numpy as np
import ast
from scipy.linalg import inv

A = (np.array(ast.literal_eval(input())))
A_inv = inv(A)

print(A_inv)
