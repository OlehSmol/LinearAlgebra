import numpy as np

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])

    def parseMatrix(self, matrix):
        pass

    def display(self):
        self.displayMatrix(self.matrix)

    def displayMatrix(self, matrix):
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                print(str(matrix[row][column]), end=" ")
            print()
        print("\n")

    def stringMatrix(self):
        pass

    def UFactorization(self):
        upper = self.matrix
        for pivot in range(self.m - 1):
            divide_pivot = self.matrix[pivot]/upper[pivot][pivot]
            for row in range(pivot + 1, self.n):
                if(upper[pivot][pivot] != 0):
                    upper[row] -= divide_pivot*upper[row][pivot]
        return upper

    def determinant(self):
        upper = self.UFactorization()
        det = 1
        for i in range(self.m):
            det *= upper[i][i]

        return det
