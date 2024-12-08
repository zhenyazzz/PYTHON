import random

def sum_of_columns_without_negatives(cols, rows, matrix):

    total_sum = 0
    column_sums = {}
    for col in range(cols):
        has_negative = False
        column_sum = 0

        for row in range(rows):
            if matrix[row][col] < 0:
                has_negative = True
                break
            column_sum += matrix[row][col]

        if not has_negative:
            total_sum += column_sum
            column_sums[col + 1] = column_sum
    return total_sum, column_sums

def generate_random_matrix(rows, cols, min_value=-10, max_value=10):
    matrix = [[random.randint(min_value, max_value) for i in range(cols)] for i in range(rows)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(f"{elem:5}", end=" ")
        print()



while True:
    try:
        a = int(input("Введите количество строк: "))
        b = int(input("Введите количество столбцов: "))
        print("Успешный ввод чисел")
        break
    except ValueError:
        print("Ошибка: Некорректный ввод числа. Попробуйте снова.")
        continue

matrix = generate_random_matrix(a, b)
print_matrix(matrix)
total, column_sums = sum_of_columns_without_negatives(b,a,matrix)
print(f"Сумма элементов в столбцах без отрицательных чисел: {total}")
print("Суммы по столбцам:", column_sums)