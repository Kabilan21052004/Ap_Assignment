class DimensionMismatchException(Exception):
    pass

def printMat(matrix_list, rows, cols):
    if len(matrix_list) != rows * cols:
        raise DimensionMismatchException("The number of elements does not match the specified dimensions.")
    
    for i in range(rows):
        row = matrix_list[i * cols:(i + 1) * cols]
        print("\t".join(map(str, row)))


printMat([1, 2, 0, 4, 0, 5, 0, 7, 9], 3, 3)