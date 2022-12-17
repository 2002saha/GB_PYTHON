print ("\033[2;31;43m !Вводите только цифры, буквы приведут к крашу программы! \033[0;0m")
x = float(input("Введите номер четверти: "))
print()

if x == 0:
    print("Четверти 0 не существует")
elif x > 4:
    print("Такой четверти не существует (их всего 4 как бы)")
elif x == 1:
    print("x > 0, y > 0")
elif x == 2:
    print("x < 0, y > 0")
elif x == 3:
    print("x < 0, y < 0")
elif x == 4:
    print("x > 0, y < 0")

input()
import os
os.system('cls')