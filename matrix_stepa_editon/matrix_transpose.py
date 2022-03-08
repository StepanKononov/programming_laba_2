def matrix_transpose(matrix):
    x_size = len(matrix[0])
    y_size = len(matrix)

    temp = [[0] * y_size for i in range(x_size)]

    for y in range(x_size):
        for x in range(y_size):
            temp[y][x] = matrix[x][y]

    return temp