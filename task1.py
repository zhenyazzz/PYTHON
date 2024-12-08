def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Ошибка: Деление на ноль")
    return a / b

def calculator():
    while True:
        print("\nВведите операцию (+, -, *, /) или 0 для завершения: ")
        operation = input().strip()

        if operation == '0':
            print("Программа завершена.")
            break

        if operation not in ['+', '-', '*', '/']:
            print("Некорректная операция. Попробуйте снова.")
            continue

        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Некорректный ввод числа. Попробуйте снова.")
            continue

        try:
            if operation == '+':
                result = add(a, b)
            elif operation == '-':
                result = subtract(a, b)
            elif operation == '*':
                result = multiply(a, b)
            elif operation == '/':
                result = divide(a, b)

            print(f"Результат: {result}")
        except ValueError as e:
            print(e)
        finally:
            print("Операция завершена")
calculator()
