def matrix_determinant(matrix):
    y_size = len(matrix)
    x_size = len(matrix[0])
    if x_size != y_size:
        print("Невозможная операция с данной матрицей")
        return

    def get_matrix_cofactor(m, i, j):
        return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]

    if (len(matrix) == 2):
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value
    det = 0
    for current_column in range(len(matrix)):
        sign = (-1) ** (current_column)
        sub_det = matrix_determinant(get_matrix_cofactor(matrix, 0, current_column))
        det += (sign * matrix[0][current_column] * sub_det)

    return det
