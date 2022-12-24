k = int(input("Введите число K: "))


def fibonacci(n):
    if n < 0:
        return fibonacci(n+2) - fibonacci(n+1)
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci_list = []
for i in range(-k, k+1):
    fibonacci_list.append(fibonacci(i))

print(f"Для k={k} список Фибоначчи будет выглядеть так: {fibonacci_list}")
