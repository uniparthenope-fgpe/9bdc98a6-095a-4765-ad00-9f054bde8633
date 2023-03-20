import numpy as np
import ast
from scipy import linalg

A = (np.array(ast.literal_eval(input())))
det = linalg.det(A)
print(det)
