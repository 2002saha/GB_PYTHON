import random
import os

def write_random_polynomial(file_name, degree):
    """Записываем случайный многочлен в файл."""
    with open(file_name, 'w') as f:
        coefficients = [random.randint(-10, 10) for _ in range(degree+1)]
        f.write('\n'.join([f'{c} {i}' for i, c in enumerate(coefficients)]))

dir_path = os.path.dirname(os.path.realpath(__file__))
write_random_polynomial(f'{dir_path}/polynomial1.txt', 3)
write_random_polynomial(f'{dir_path}/polynomial2.txt', 4)

def read_polynomial(file_name):
    """Считываем многочлен из файла и возвращает его в виде словаря."""
    with open(file_name, 'r') as f:
        return {int(degree): int(coefficient) for coefficient, degree in (line.strip().split() for line in f)}

def write_polynomial(file_name, polynomial):
    """Записываем многочлен в файл."""
    with open(file_name, 'w') as f:
        f.write('\n'.join([f'{polynomial[degree]} {degree}' for degree in sorted(polynomial.keys(), reverse=True)]))


polynomial1 = read_polynomial(f'{dir_path}/polynomial1.txt')
polynomial2 = read_polynomial(f'{dir_path}/polynomial2.txt')


result = {d: polynomial1.get(d, 0) + polynomial2.get(d, 0) for d in set(polynomial1) | set(polynomial2)}


write_polynomial(f'{dir_path}/result.txt', result)
os.system('cls' if os.name == 'nt' else 'clear')
