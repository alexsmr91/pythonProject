from typing import List


class Matrix:

    def __init__(self, matrix: List[List[int]]):
        for i, row in enumerate(matrix):
            if i == 0:
                col_count = len(row)
            elif col_count != len(row):
                raise ValueError('fail initialization matrix')
        self.matrix = matrix

    def __str__(self):
        msg = '|'
        for row in self.matrix:
            for el in row:
                msg = f'{msg} {str(el)} '
            msg = f'{msg}|\n|'
        return msg[:-2]

    def rows_count(self):
        return len(self.matrix)

    def colums_count(self):
        return len(self.matrix[0])

    def __eq__(self, other):
        return self.rows_count() == other.rows_count() and self.colums_count() == other.colums_count()

    def __add__(self, other):
        res_matrix = []
        if self == other:
            for i, row in enumerate(self.matrix):
                res_row = []
                for j, el in enumerate(row):
                    res_row.append(el + other.matrix[i][j])
                res_matrix.append(res_row)
        else:
            raise ValueError('Разный размер матриц')
        return Matrix(res_matrix)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    #fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
