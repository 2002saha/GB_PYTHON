import random

random_list = []
for i in range(10):
  random_list.append(random.uniform(0,10))

print(f"Случайный список из вещественных чисел: {random_list}")


# инициализируем минимальное и максимальное значение дробной части
min_fractional = float("inf")
max_fractional = float("-inf")

# итерируемся по элементам списка
for number in random_list:
    # если число имеет дробную часть, отличную от 0
    if number % 1 != 0:
        # обновляем минимальное и максимальное значение дробной части
        min_fractional = min(min_fractional, number % 1)
        max_fractional = max(max_fractional, number % 1)

# выводим разницу между максимальным и минимальным значением дробной части
print("Разница между максимальным и минимальным значением дробной части:")
print(round(max_fractional - min_fractional, 2))