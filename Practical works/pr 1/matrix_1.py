matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()
print_matrix(matrix)