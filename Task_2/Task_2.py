from prettytable import PrettyTable
import random

size = 5

matrix = [[random.randint(1, 30) for j in range(size)] for i in range(size)]


expected_table = PrettyTable()
expected_table.title = "Математическое ожиданиe"
expected_table.field_names = ["Ряд", " Значение "]

expected_values = []

for j in range(size):
    expected_value = 0
    for i in range(size):
        expected_value += matrix[j][i] * (1 / 30)
    expected_table.add_row([j + 1, round(expected_value, 2)])
    expected_values.append(round(expected_value, 2))



despersion_table = PrettyTable()
despersion_table.title = "Дисперсия"
despersion_table.field_names = ["Ряд", "Значение"]

for j in range(size):
    despersion = 0
    for i in range(size):
        despersion += matrix[j][i] ** 2 * (1 / 30)
    despersion -= expected_values[j] ** 2

    despersion_table.add_row([j + 1, round(despersion, 2)])


print(expected_table)
print(despersion_table)
