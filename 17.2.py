from random import randint
class Tank:
    def __init__(self, model, min_damage, max_damage, armor, health, miss):
        self.model = model
        self.damage = randint(min_damage, max_damage)
        self.armor = armor
        self.health = health
        self.miss = miss

    def info(self):
        print(f"{self.model} имеет броню {self.armor}мм при {self.health}ед. здоровья и уроне в {self.damage} ед.")

    def shot(self, enemy):
        if randint(1,100) <= self.miss:
            print(f"\n{self.model}: ПРОМАХНУЛСЯ")
        else:
            enemy.health -= round(self.damage - self.damage * enemy.armor / 100)
            print(f"\n{self.model}:")
            print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")

tank1 = Tank("T-34", 85, 90, 15, 630, 30)
tank2 = Tank("КВ-2", 70, 105, 30, 400, 15)

tank1.info()
tank2.info()


while True:
    if tank1.health<=0 and tank2.health <=0:
        print("Ничья!")
        break
    elif tank1.health <=0:
        print('Выиграл ', tank2.model)
        break
    elif tank2.health <= 0:
        print("Выиграл ", tank1.model)
        break
    tank1.shot(enemy = tank2)
    tank2.shot(enemy = tank1)



