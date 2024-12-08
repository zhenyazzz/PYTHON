from collections import Counter
from curses.ascii import isdigit


def process_list(data):
    data = [i for i in data if i != 0]
    even_sum = sum(i for i in data if isinstance(i, (int, float)) and i % 2 == 0)
    print(f"Сумма четных чисел: {even_sum}")
    print(f"Список без нулей: {data}")


def process_set(data):
    if data:
        max_elem = max(data)
        data.remove(max_elem)
        print(f"Множество без максимального элемента ({max_elem}): {data}")
    else:
        print("Множество пусто")


def process_data(data_input):
    if data_input.startswith('[') and data_input.endswith(']'):
        try:
            data = data_input[1:-1].split(',')
            data = [int(i.strip()) if i.strip().isdigit() else float(i.strip()) for i in data]
            process_list(data)
        except ValueError:
            print("Ошибка: некорректный список.")
            return

    elif data_input.startswith('{') and data_input.endswith('}'):
        try:
            data = data_input[1:-1].split(',')
            data = {int(i.strip()) if i.strip().isdigit() else float(i.strip()) for i in data}
            process_set(data)
        except ValueError:
            print("Ошибка: некорректное множество.")
            return

    try:
        data = int(data_input)
        print(f"Введено целое число: {data}")

        if data > 1:
            for i in range(2, int(data ** 0.5) + 1):
                if data % i == 0:
                    print(f"Число {data} не является простым")
                    break
            else:
                print(f"Число {data} является простым")
        else:
            print(f"Число {data} не является простым (должно быть больше 1)")

    except ValueError:
        try:
            data_  = float(data_input)
            print("Является числом с точкой")
        except ValueError:
            print("Не является числом")
            if data_input:
                counter = Counter(data_input)

                most_common_char, col = counter.most_common(1)[0]
                print(f"Наиболее часто встречающийся символ: {most_common_char} встретился {col} раз")
            else:
                print("Пустая строка")
while (True):
    user_input = input("Введите данные: ")
    if(user_input == "exit"):
        break
    process_data(user_input)
