#!/usr/bin/python3

def squared(el):
    return el*el


def square_matrix_simple(matrix=[]):
    squared_matrix = [list(map(squared, row)) for row in matrix]
    return squared_matrix
