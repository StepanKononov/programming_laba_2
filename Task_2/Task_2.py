import numpy as np
import random

size = 50
origin_data = [[random.randint(1, 30) for i in range(size)] for j in range(size)]
delete_elems_data = [row[:] for row in origin_data]

elem_counter = 0
while elem_counter != 10:
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    if delete_elems_data[y][x] is not None:
        delete_elems_data[y][x] = None
        elem_counter += 1

def linear_approximation(data):
    for i in range(len(data)):
        if data[i] is None:
            temp = i
            prev_elem = None
            next_elem = None
            while prev_elem is None:
                temp -= 1
                prev_elem = data[temp]
            temp = i
            while next_elem is None:
                temp = (temp + 1) % len(data)
                next_elem = data[temp]
            data[i] = np.mean([prev_elem, next_elem])
    return data

def correlation(data):
    correlation_lines = [dict() for i in data]

    for i in range(len(data)):
        for j in range(len(data)):
            if j == i:
                continue
            ar_1 = [0 if data[i][t] is None else data[i][t] for t in range(len(data[i]))]
            ar_2 = [0 if data[j][t] is None else data[j][t] for t in range(len(data[j]))]
            correlation_lines[i][j] = np.correlate(ar_1, ar_2)[0]

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] is None:
                best_cor = -10 ** 10
                best_key = None
                for key in correlation_lines[i].keys():
                    if correlation_lines[i][key] > best_cor:
                        if data[key][j] is not None:
                            best_cor = correlation_lines[i][key]
                            best_key = key
                data[i][j] = data[best_key][j]
    return data

def similarity_calculation(or_ar, cor_ar, lin_ar):
    delta_cor = 0
    delta_lin = 0
    for i in range(len(or_ar)):
        delta_cor += abs(or_ar[i] - cor_ar[i])
        delta_lin += abs(or_ar[i] - lin_ar[i])
    return delta_cor, delta_lin

def make_2d(ar):
    temp = []
    for row in ar:
        for elem in row:
            temp.append(elem)
    return temp


linear_approximation_data = linear_approximation(make_2d(delete_elems_data))
correlation_data = correlation(delete_elems_data)

print(similarity_calculation(make_2d(origin_data), make_2d(correlation_data), linear_approximation_data))

