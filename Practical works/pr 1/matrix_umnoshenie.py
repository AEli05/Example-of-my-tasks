matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

def matrix_multiplication(matrix1: list[list[float]], matrix2: list[list[float]]):  # Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице, не забудьте проверить это
    new_matrix1 = []
    new_matrix2 = []
    new_matrix1 = matrix1

    for i in range(len(matrix1)):
      for j in range(len(matrix1)):
        result_2 = matrix2[j][i]
        new_matrix2.append(result_2)
    new_matrix2 = [new_matrix2[i:i+3] for i in range(0, len(new_matrix2), 3)]


    return new_matrix1, new_matrix2


matrix_multiplication(matrix1, matrix2)
