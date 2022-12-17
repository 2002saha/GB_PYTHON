
print ("\033[2;31;43m !Вводите только цифры, буквы приведут к крашу программы! \033[0;0m")
x = float(input("Введите x = "))
y = float(input("Введите y = "))
print()

if x*y == 0:
    print("Координата не должно быть равна 0")
elif x*y > 0:
    if x > 0:
        n = 1
        print(n, 'четверть')

    else:
        n = 3
        print(n, 'четверть')

else:
    if x > 0:
        n = 4
        print(n, 'четверть')
    else:
        n = 2
        print(n, 'четверть')