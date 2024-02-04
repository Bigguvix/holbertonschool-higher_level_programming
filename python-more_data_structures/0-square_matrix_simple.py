#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []

    if len(matrix) > 0:
        for elems in matrix[:]:
            new.append(list(map(lambda x: x ** 2, elems)))

    return new