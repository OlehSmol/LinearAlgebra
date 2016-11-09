import numpy as np

class Matrix():
    def __init__(self, matrix):
        self.matrix = np.array(matrix, dtype="float64")
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.steps = []

    def parse_matrix(self, matrix):
        pass

    def display(self):
        Matrix.display_matrix(self.matrix)

    def display_matrix(matrix):
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                print(str(matrix[row][column]), end=" ")
            print()
        print("\n")

    def string_matrix(self):
        pass

    def u_factorization(self):
        upper = self.matrix
        self.steps.append(np.copy(upper))
        for pivot in range(self.m - 1):
            pivot_row = pivot
            while not upper[pivot_row][pivot] and pivot_row < self.m - 1:
                pivot_row += 1
            if not upper[pivot_row][pivot]:
                continue
            temp = np.copy(upper[pivot])
            upper[pivot] = upper[pivot_row]
            upper[pivot_row] =temp
            divide_pivot = upper[pivot]/upper[pivot][pivot]
            for row in range(pivot + 1, self.m):
                if(upper[pivot][pivot] != 0):
                    upper[row] -= divide_pivot*upper[row][pivot]
            self.steps.append(np.copy(upper))

        return upper

    def determinant(self):
        upper = self.u_factorization()
        det = 1
        for i in range(self.m):
            det *= upper[i][i]

        return det

    def is_consistent(self):
        matrix = self.u_factorization()
        is_consistent = True
        for row in range(self.m):
            is_zero = True
            for column in range(self.m):
                if matrix[row][column] != 0:
                    is_zero = False
                    break
            if is_zero and matrix[row][-1] != 0:
                is_consistent = False
                break

        return is_consistent

    def get_steps(self):
        return [i.tolist() for i in self.steps]

m = Matrix([[1, 2], [3, 4]])
print(m.is_consistent())
print(m.get_steps())