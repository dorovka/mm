import random
hp1 = 100
hp2 = 100
while hp1 > 0 and hp2 >0:
    who = random.randint(1,2)
    if who == 1:
        hp2 -= 20
        print("Перый боец ударил! У второго осталось ",hp2," здоровья.")
    if who == 2:
        hp1 -= 20
        print("Второй боец ударил! У первого осталось ",hp1," здоровья.")
winner = max(hp1, hp2)
if winner == hp1:
    winner = "первый боец!"
else:
    winner = "второй боец!"
print("Победитель боя это", winner)