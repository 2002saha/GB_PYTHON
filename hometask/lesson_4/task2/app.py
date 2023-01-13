import random
import os

def write_random_polynomial(file_name, degree):
    """Записываем случайный многочлен в файл."""
    with open(file_name, 'w') as f:
        for i in range(degree+1):
            coefficient = random.randint(-10, 10)
            f.write(f'{coefficient} {i}\n')

dir_path = os.path.dirname(os.path.realpath(__file__))
write_random_polynomial(f'{dir_path}/polynomial1.txt', 3)
write_random_polynomial(f'{dir_path}/polynomial2.txt', 4)

def read_polynomial(file_name):
    """Считываем многочлен из файла и возвращает его в виде словаря."""
    with open(file_name, 'r') as f:
        polynomial = {}
        for line in f:
            degree, coefficient = line.strip().split()
            polynomial[int(degree)] = int(coefficient)
    return polynomial

def write_polynomial(file_name, polynomial):
    """Записываем многочлен в файл."""
    with open(file_name, 'w') as f:
        for degree in sorted(polynomial.keys(), reverse=True):
            f.write(f'{polynomial[degree]} {degree}\n')


polynomial1 = read_polynomial(f'{dir_path}/polynomial1.txt')
polynomial2 = read_polynomial(f'{dir_path}/polynomial2.txt')


result = {}
for degree in polynomial1.keys():
    if degree in result:
        result[degree] += polynomial1[degree]
    else:
        result[degree] = polynomial1[degree]

for degree in polynomial2.keys():
    if degree in result:
        result[degree] += polynomial2[degree]
    else:
        result[degree] = polynomial2[degree]


write_polynomial(f'{dir_path}/result.txt', result)
os.system('cls' if os.name == 'nt' else 'clear')