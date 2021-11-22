#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            j = 0
            last_idx = len(row) - 1
            while j <= last_idx:
                if j == last_idx:
                    print('{:d}'.format(row[j]))
                else:
                    print('{:d}'.format(row[j]), end=' ')
                j += 1
