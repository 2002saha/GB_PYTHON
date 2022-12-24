# Получаем вещественное число введенное пользователем
number = input("Введите вещественное число: ")

# Инициализируем переменную для хранения суммы цифр
sum = 0

# Перебираем каждую цифру в числе
for digit in number:
    # Проверяем, является ли символ цифрой
    if digit.isdigit():
        # Если это цифра, то добавляем ее в сумму
        sum += int(digit)
    else:
        print("Этот символ не число")

# Выводим результат
print(f"Сумма цифр числа равна {sum}")
