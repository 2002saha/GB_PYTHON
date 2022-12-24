import random

numbers = [random.randint(1, 100) for _ in range(10)]

print(f"Сгенерированный список из 10 случайных чисел: {numbers}")

print()

odd_numbers = []

for i in range(len(numbers)):

    if i % 2 == 1:

        odd_numbers.append(numbers[i])


print(f"Список чисел с нечетным индексом: {odd_numbers}")
print()
sum = 0

for number in odd_numbers:

    sum += number

print(f"Сумма элементов списка c нечетным индексом: {sum}")
