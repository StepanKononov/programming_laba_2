from prettytable import PrettyTable
import ssss as mat_s
import numpy as np
import random


matrix_size = 100
matrix = [[random.randint(10, 100) for i in range(matrix_size)] for j in range(matrix_size)]
origin_np_matrix = np.array(matrix)





np.linalg.matrix_power(origin_np_matrix, 2)


origin_np_matrix = mat_s.Matrix(matrix)
print(origin_np_matrix.matrix_determinant(origin_np_matrix.matrix))