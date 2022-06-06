#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for s in range(len(matrix)):
        for t in range(len(matrix[s])):
            print("{:d}".format(matrix[s][t], end=""))
            if t != (len(matrix[s])-1):
                print("", end="")
                print("")
