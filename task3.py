while True:
    try:
        n = int(input("Введите натуральное число: "))
        divisors = [i for i in range(1, n + 1) if n % i == 0]
        min_divisor = min(divisors)
        max_divisor = max(divisors)
        print("Список делителей числа:", divisors)
        print("Минимальный делитель:", min_divisor)
        print("Максимальный делитель:", max_divisor)
        break
    except ValueError as e:
        print(f"Ошибка: {e}. Попробуйте еще раз.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}.")