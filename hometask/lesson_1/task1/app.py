day = int(input ("Введите число обозначающее день недели: "))
lastday = 7

if day > lastday:
    print ("В неделе 7 дней, ты не знал?")
elif (day == 6) or (day == 7):
    print ("Этот день выходной")
else:
    print ("Этот день не выходной")