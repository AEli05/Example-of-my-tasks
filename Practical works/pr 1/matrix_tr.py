matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def matrix_transposition(matrix: list[list[float]]) -> list[list[float]]:
    for i in range(len(matrix)):
      for j in range(len(matrix)):
        print(matrix[j][i], end=" ")
      print()

matrix_transposition(matrix1)