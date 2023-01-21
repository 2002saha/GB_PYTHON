import random

print("Добро пожаловать в конфетную игру!\n")
player1 = input("Игрок 1, пожалуйста, введите свое имя: ")
player2 = "AI"

candies = 100
turn = random.choice([player1, player2])
print(f"\nИгрок: {turn} выиграл жеребьевку и сделает первый ход.\n")

while candies > 0:
    if turn == player2:
        if candies <= 28:
            move = candies
        else:
            move = 1 + candies % 28
        print(f"{turn} берет {move} конфет.")
    else:
        print(f"{turn} ходит.")
        move = int(input("Сколько конфет вы хотите взять (до 28)? "))
        while move > 28 or move > candies or move==0:
            move = int(input("Неверный ход. Пожалуйста, введите число от 1 до 28: "))
    candies -= move
    print(f"{turn} берет {move} конфет. {candies} конфеты осталось на столе.\n")
    if candies == 0:
        print(f"{turn} выиграл игру! Поздравляем!")
        break
    if turn == player1:
        turn = player2
    else:
        turn = player1
