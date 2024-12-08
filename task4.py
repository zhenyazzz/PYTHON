def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        return None
    except TypeError:
        print("Ошибка: оба аргумента должны быть числами!")
        return None
    else:
        print(f"Результат деления {a} на {b} равен {result}")
        return result
    finally:
        print("Завершение операции деления.")

def get_integer_input():
    while True:
        try:
            number = int(input("Введите целое число: "))
            return number
        except ValueError:
            print("Ошибка: введено нецелое число. Пожалуйста, попробуйте снова.")
            continue
        finally:
            print("Обработка ввода завершена.")

a = get_integer_input()
b = get_integer_input()
divide_numbers(a,b)