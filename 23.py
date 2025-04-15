class DimensionMismatchException(Exception):
    pass

def reshape(lst, rows, cols):
    return [lst[i * cols:(i + 1) * cols] for i in range(rows)]

def matMul(mat1, mat2):
    import math

    len1 = len(mat1)
    len2 = len(mat2)
    size1 = int(math.sqrt(len1))
    size2 = int(math.sqrt(len2))

    if size1 * size1 != len1 or size2 * size2 != len2:
        raise DimensionMismatchException("One of the lists is not a square matrix.")
    if size1 != size2:
        raise DimensionMismatchException("Matrix dimensions are not compatible for multiplication.")

    A = reshape(mat1, size1, size1)
    B = reshape(mat2, size1, size1)
    result = [[0]*size1 for _ in range(size1)]
    for i in range(size1):
        for j in range(size1):
            for k in range(size1):
                result[i][j] += A[i][k] * B[k][j]
    return [elem for row in result for elem in row]
res = matMul([1, 2, 0, 4, 0, 5, 0, 7, 9], [1, 2, 0, 4, 0, 5, 0, 7, 9])
print(res)