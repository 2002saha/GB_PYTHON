import random
import os

def generate_polynomial(k):
    coefficients = [random.randint(0, 100) for _ in range(k + 1)]
    polynomial = " + ".join([f"{coefficient}*x^{i}" if i > 1 else f"{coefficient}*x" if i == 1 else f"{coefficient}" for i, coefficient in enumerate(coefficients)])
    return polynomial

k = int(input("Введите степень многочлена: "))
polynomial = generate_polynomial(k)
print(polynomial)

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'polynomial.txt')
with open(file_path, "w") as f:
    f.write(polynomial)
input()
os.system('cls' if os.name == 'nt' else 'clear')