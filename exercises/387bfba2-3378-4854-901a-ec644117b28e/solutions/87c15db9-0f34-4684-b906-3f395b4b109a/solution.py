from scipy.linalg import solve
import numpy as np
import ast

A = (np.array(ast.literal_eval(input())))
b = (np.array(ast.literal_eval(input())))

x = solve(A, b)
print(x)
