def matrix_input():
    print("Введите ширину и высоту матрицы")
    x, y = map(int, input().split())
    matrix = []
    for i in range(y):
        line = list(map(int, input().split()))
        while len(line) < x:
            print("Данная строка меньше указанного значения. Повторите попытку ввода")
            line = list(map(int, input().split()))
        matrix.append(line)
    return matrix
