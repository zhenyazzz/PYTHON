#натуральноее число сумма четных цифр этого числа или 0 если четных цифр в записи нет
while True:
    try:
        # Вводим числоапро
        a = int(input("Введите натуральное число: "))
        if a <= 0:
            raise ValueError("Число должно быть натуральным (положительным).")
        print("Сумма четных цифр натурального числа равна: " + str(sum(int(digit) for digit in str(a) if int(digit) % 2 == 0)))
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте еще раз.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}.")
