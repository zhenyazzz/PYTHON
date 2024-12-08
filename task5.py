toys = {
    'Тедди': ['мех, синтепон', 50, 5],
    'Мяч': ['резина', 30, 10],
    'Кубики': ['пластик', 15, 7],
    'Машинка': ['пластик, металл', 120, 3],
    'Кукла': ['пластик, ткань', 80, 4]
}


def show_menu():
    print("\nМеню магазина:")
    print("1. Просмотр описания игрушек")
    print("2. Просмотр цены игрушек")
    print("3. Просмотр количества игрушек")
    print("4. Вся информация об игрушках")
    print("5. Покупка игрушек")
    print("6. Выход из программы")


def view_description():
    for toy, info in toys.items():
        print(f"{toy} – состав: {info[0]}")


def view_price():
    for toy, info in toys.items():
        print(f"{toy} – цена: {info[1]} руб.")


def view_quantity():
    for toy, info in toys.items():
        print(f"{toy} – количество: {info[2]} шт.")


def view_all_info():
    for toy, info in toys.items():
        print(f"{toy}: состав: {info[0]}, цена: {info[1]} руб., количество: {info[2]} шт.")


def buy_toys():
    total_cost = 0
    purchases = []
    while True:
        toy_name = input("\nВведите название игрушки для покупки (или 'n' для выхода): ")
        if toy_name == 'n':
            break
        if toy_name not in toys:
            print("Такой игрушки нет в магазине.")
            continue

        try:
            quantity = int(input("Введите количество для покупки: "))
        except ValueError:
            print("Некорректное количество. Попробуйте снова.")
            continue

        if quantity > toys[toy_name][2]:
            print(f"Недостаточно товара на складе. Доступно только {toys[toy_name][2]} шт.")
        else:
            cost = quantity * toys[toy_name][1]
            total_cost += cost
            toys[toy_name][2] -= quantity
            purchases.append((toy_name, quantity, toys[toy_name][1], cost))
            print(f"Товар {toy_name} добавлен в корзину в количестве {quantity} шт. на сумму {cost} руб.")
    if purchases:
        print("\n" + "=" * 30)
        print("         ЧЕК ПОКУПКИ         ")
        print("=" * 30)
        print(f"{'Наименование':<15} {'Кол-во':<8} {'Цена/шт':<10} {'Сумма':<10}")
        print("-" * 30)

        for toy_name, quantity, price, cost in purchases:
            print(f"{toy_name:<15} {quantity:<8} {price:<10} {cost:<10}")

        print("-" * 30)
        print(f"{'Итого':<25} {total_cost} руб.")
        print("=" * 30)
        print("Спасибо за покупку!")
    else:
        print("Вы не совершили покупок.")


def toy_store():
    while True:
        try:
            show_menu()
            choice = input("\nВыберите пункт меню (1-6): ")

            if choice == '1':
                view_description()
            elif choice == '2':
                view_price()
            elif choice == '3':
                view_quantity()
            elif choice == '4':
                view_all_info()
            elif choice == '5':
                buy_toys()
            elif choice == '6':
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор, попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла неизвестная ошибка: {e}.")

toy_store()
