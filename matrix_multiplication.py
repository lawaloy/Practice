def matrix_multiplication(matrix1, matrix2):
    
    # Edge case
    if not matrix1 and not matrix2:
        return []

    rows, cols = len(matrix1), len(matrix2[0])
    # Initialization of result matrix
    result = [[0 for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            for k in range(len(matrix2[0])):
                result[row][col] += matrix1[row][k] * matrix2[k][col]

    return result

print(matrix_multiplication([[1,2,3],[4,2,1],[9,0,4]], [[5,6],[4,7],[1,3]]))
