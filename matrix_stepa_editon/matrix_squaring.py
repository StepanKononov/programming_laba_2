def matrix_squaring(matrix):
    y_size = len(matrix)
    x_size = len(matrix[0])
    if x_size != y_size:
        print("Невозможная операция с данной матрицей")
        return

    temp = [[None] * y_size for __ in range(y_size)]

    for i in range(y_size):
        for j in range(x_size):
            temp[i][j] = sum(matrix[i][kk] * matrix[kk][j] for kk in range(y_size))
    return temp