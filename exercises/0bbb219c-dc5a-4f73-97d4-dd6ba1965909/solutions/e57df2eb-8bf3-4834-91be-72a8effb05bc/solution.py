import numpy as np
import ast
from scipy.linalg import eig

A = (np.array(ast.literal_eval(input())))

eigenvalues, eigenvectors = eig(A)

print(eigenvectors)
