from prettytable import PrettyTable
from time import perf_counter
import matrix_stepa as mat_s
import numpy as np
import random


matrix_size = 10
matrix = [[random.randint(10, 100) for i in range(matrix_size)] for j in range(matrix_size)]


squaring = "matrix squaring"
transpose = "matrix transpose"
determinant = "determinant"

time_data_np = {squaring: 0, transpose: 0, determinant: 0}
time_data_stepa = {squaring: 0, transpose: 0, determinant: 0}

origin_np_matrix = np.array(matrix)

t_start = perf_counter()
np.linalg.matrix_power(origin_np_matrix, 2)
time_data_np[squaring] = perf_counter() - t_start

t_start = perf_counter()
np.transpose(origin_np_matrix)
time_data_np[transpose] = perf_counter() - t_start


t_start = perf_counter()
np.linalg.det(origin_np_matrix)
time_data_np[determinant] = perf_counter() - t_start



origin_matrix = mat_s.Matrix(matrix)

t_start = perf_counter()
origin_matrix.matrix_squaring()
time_data_stepa[squaring] = perf_counter() - t_start

t_start = perf_counter()
origin_matrix.matrix_transpose()
time_data_stepa[transpose] = perf_counter() - t_start


t_start = perf_counter()
origin_matrix.matrix_determinant(origin_matrix.data)
time_data_stepa[determinant] = perf_counter() - t_start




table = PrettyTable()

table.field_names = ["Тип вычисления", "NumPy", "Stepa"]
table.add_row([squaring, time_data_np[squaring], time_data_stepa[squaring]])
table.add_row([transpose, time_data_np[transpose], time_data_stepa[transpose]])
table.add_row([determinant, time_data_np[determinant], time_data_stepa[determinant]])

print(table)
