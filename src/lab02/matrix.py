from testing import test

def is_rect(mat: list[list[float | int]]):
    '''
    Проверяет матрицу на прямоугольность
    '''
    if len(mat) == 0:
        return True
    l = len(mat[0])

    for i in range(len(mat)):
        if len(mat[i]) != l:
            return False
    return True

def transpose(mat: list[list[float | int]]):
    '''
    Транспонирует матрицу
    '''
    if not is_rect(mat):
        raise ValueError
    if len(mat) == 0:
        return mat
    transposed = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            transposed[j][i] = mat[i][j]
    return transposed

def row_sums(mat: list[list[float | int]]):
    '''
    Возвращает суммы рядов матрицы. Требуется прямоугольность
    '''
    if not is_rect(mat):
        raise ValueError
    if len(mat) == 0:
        return mat

    sums = []
    for r in mat:
        sums.append(sum(r))

    return sums

def col_sums(mat: list[list[float | int]]):
    '''
    Возвращает суммы столбцов матрицы. Требуется прямоугольность
    '''
    if not is_rect(mat):
        raise ValueError
    if len(mat) == 0:
        return mat

    return row_sums(transpose(mat))

transpose_test = [
    [[1, 2, 3]],
    [[1], [2], [3]],
    [[1, 2], [3, 4]],
    [],
    [[1, 2], [3]]
]

row_sums_test = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]

col_sums_test = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]

print('==TRANSPOSE==')
test(transpose, transpose_test)
print('\n==ROW_SUMS==')
test(row_sums, row_sums_test)
print('\n==COL_SUMS==')
test(col_sums, col_sums_test)