def input_matrix(rows, cols):
    matrix = []
    print(f"Введите элементы матрицы {rows}x{cols}")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Введите элемент [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix


def add_matrix(matrix_1, matrix_2):
    result = []
    for i in range(len(matrix_1)):
        row = []
        for j in range(len(matrix_1[0])):
            element_sum = matrix_1[i][j] + matrix_2[i][j]
            row.append(element_sum)
        result.append(row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


my_rows = int(input("Введите колличество строк: "))
my_cols = int(input("Введите колличество столбцов: "))

my_matrix_1 = input_matrix(my_rows, my_cols)
my_matrix_2 = input_matrix(my_rows, my_cols)
result_matrix = add_matrix(my_matrix_1, my_matrix_2)

print("Результат: ")
print_matrix(result_matrix)
