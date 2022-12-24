import random

numbers = [random.randint(1, 100) for _ in range(10)]

print(f'Сгенерированный список: {numbers}')

result = [numbers[i] * numbers[-i - 1] for i in range(len(numbers) // 2)]

print(f"Список произведения пар: {result}")