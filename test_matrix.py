import numpy as np
from unittest import TestCase
from matrix import Matrix


class TestMatrix(TestCase):
    def test_is_consistent1(self):
        n = Matrix(np.array([[1, 2, 3], [1, 4, 2]], dtype='float64'))
        expected = True
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent2(self):
        n = Matrix(np.array([[0, 0, 4], [1, 4, 2]], dtype='float64'))
        expected = False
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent3(self):
        n = Matrix(np.array([[1, 1, 1], [1, 1, 1]], dtype='float64'))
        expected = True
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent4(self):
        n = Matrix(np.array([[1, 2, 3, 9], [1, 4, 2, 4],  [4, 2, 0, 2]], dtype='float64'))
        expected = True
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent5(self):
        n = Matrix(np.array([[1, 2, 3, 1], [0, 0, 0, 1],  [4, 3, 2, 4]], dtype='float64'))
        expected = False
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent6(self):
        n = Matrix(np.array([[1, -1, 1, 3], [1, 1, -1, 5], [-2, 4, -4, 1]], dtype='float64'))
        expected = False
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent7(self):
        n = Matrix(np.array([[4, 2, 3, 3, 8], [5, 2, 3, 9, 3], [9, 0, 3, 6, 1], [9, 3, 1, 4, 3], ], dtype='float64'))
        expected = True
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent8(self):
        n = Matrix(np.array([[0, 0, 0, 0, 2], [9, 2, 1, 4, 0], [2, 1, 7, 5, 2], [1, 4, 2, 5, 9]], dtype='float64'))
        expected = False
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent9(self):
        n = Matrix(np.array([[1, 4, -1, 0, -2], [1, 4, -1, 0, 9], [9, -1, 7, -5, 2], [-1, -4, -2, -5, -9]], dtype='float64'))
        expected = False
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent10(self):
        n = Matrix(np.array([[9, 0, 4, 7, 2, 4], [2, 8, 2, 5, 2, 3], [1, 8, 0, 5, 4, 2], [9, 4, 3, 2, 1, 7], [4, 1, 7, 6, 3, 5]], dtype='float64'))
        expected = True
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent11(self):
        n = Matrix(np.array([[9, 0, 4, 7, 2, 5], [9, 4, 0, 5, 1, 4], [1, 2, 9, 5, 1, 3], [0, 0, 0, 0, 0, 7], [1, 7, 3, 4, 5, 9]], dtype='float64'))
        expected = False
        actual = n.is_consistent()
        self.assertEquals(expected, actual)

    def test_is_consistent12(self):
        n = Matrix(np.array([[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]], dtype='float64'))
        expected = True
        actual = n.is_consistent()
        self.assertEquals(expected, actual)