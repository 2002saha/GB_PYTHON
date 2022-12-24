
decimal = int(input("Введите десятичное число: "))

# Преобразовать десятичное число в двоичное
binary = bin(decimal)

binary = binary[2:]

print(f"Двоичное представление числа {decimal}: {binary}")