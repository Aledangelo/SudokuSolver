import gurobipy as gp
from gurobipy import GRB
import numpy as np


def main():
    #    matrix = np.array([[0, 0, 8, 0, 1, 0, 0, 0, 9],
    #                       [6, 0, 1, 0, 9, 0, 3, 2, 0],
    #                       [0, 4, 0, 0, 3, 7, 0, 0, 5],
    #                       [0, 3, 5, 0, 0, 8, 2, 0, 0],
    #                       [0, 0, 2, 6, 5, 0, 8, 0, 0],
    #                       [0, 0, 4, 0, 0, 1, 7, 5, 0],
    #                       [5, 0, 0, 3, 4, 0, 0, 8, 0],
    #                       [0, 9, 7, 0, 8, 0, 5, 0, 6],
    #                       [1, 0, 0, 0, 6, 0, 9, 0, 0]])

    name = input('Enter the path of the .dat file containing the sudoku puzzle: ')
    col = input('Enter the number of columns: ')
    row = input('Enter the number of rows: ')

    if int(col) != int(row):
        print('[ERROR] The matrix containing the sudoku must be a square matrix')
        quit(1)

    file = open(str(name))
    matrix = np.zeros(int(row))
    lines = file.readlines()
    for i in range(int(row)):
        riga = lines[i].split(" ")
        for j in range(int(col)):
            matrix[i, j] = int(riga[j])

    mod = gp.Model('Sudoku')
    xvar = mod.addVars(9, 9, 9, vtype=GRB.BINARY, name="x")

    for i in range(int(row)):
        for j in range(int(col)):
            if matrix[i, j] != 0:
                k = int(matrix[i, j]) - 1
                xvar[i, j, k].LB = 1

    mod.addConstrs((xvar.sum(i, j, '*') == 1 for i in range(9) for j in range(9)), name="Cell")
    mod.addConstrs((xvar.sum(i, '*', k) == 1 for i in range(9) for k in range(9)), name="Row")
    mod.addConstrs((xvar.sum('*', j, k) == 1 for j in range(9) for k in range(9)), name="Col")
    mod.addConstrs((gp.quicksum(vars[i, j, k] for i in range(i0 * 3, (i0 + 1) * 3)
                                for j in range(j0 * 3, (j0 + 1) * 3)) == 1
                    for k in range(9)
                    for i0 in range(3)
                    for j0 in range(3)), name="Riq")

    mod.write('Sudoku.lp')

    mod.optimize()

    sol = np.zeros((9, 9))

    solution = mod.getAttr('x', vars)

    for i in range(9):
        for j in range(9):
            for k in range(9):
                if solution[i, j, k] > 0.5:
                    sol[i, j] = int(k + 1)
    print(sol)


if __name__ == "__main__":
    main()