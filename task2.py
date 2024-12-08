while True:
    try:
        s = input("Введите строку текста: ")
        print(s.swapcase())
        print(max(s.split(), key = len))
        print(sum(int(element) for element in s if element.isdigit()))
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте еще раз.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}.")