from time import time
def pause(secs):
    init_time = time.time()
    while time.time() < init_time+secs: pass
from tkinter import *
from random import randint
import time



window = Tk()
window.geometry('750x600+300+100')
window.title("Драки")
window.resizable(width=False, height=False)
canvas = Canvas(window, width = 800, height = 600, background = "grey94")
canvas.pack()


class Pusher:
    def __init__(self, model, min_damage, max_damage, health, miss, weapon):
        self.model = model
        self.damage = randint(min_damage, max_damage)
        self.health = health
        self.miss = miss
        self.weapon = weapon

    def info(self):
        lb = Label(text = f"{self.model} имеет {self.health}ед. здоровья и урон {self.damage} ед. Бьёт {self.weapon}")
        lb.place(x = 10, y = 160)
    def shot(self, enemy):
        if enemy == hero:
            if randint(1,100) <= self.miss:
                lb1 = Label(text = f"\n{self.model}: ПРОМАХНУЛСЯ", background = "IndianRed1")
                lb1.place(x = 325, y=350)
                lb1.after(5000, lambda: lb1.destroy())
            else:
                enemy.health -=self.damage
                lb = Label(text = f"\n{self.model}:", background = "IndianRed1")
                lb.place(x=325, y=250)
                lb2 = Label(text = f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")
                lb2.place(x=325, y = 300)
                lb.after(5000, lambda: lb.destroy())
                lb2.after(5000, lambda: lb2.destroy())
        elif enemy == antihero:
            if randint(1,100) <= self.miss:
                lb1 = Label(text = f"\n{self.model}: ПРОМАХНУЛСЯ", background = "SeaGreen1")
                lb1.place(x = 325, y=500)
                lb1.after(5000, lambda: lb1.destroy())
            else:
                enemy.health -=self.damage
                lb = Label(text = f"\n{self.model}:", background = "SeaGreen1")
                lb.place(x=325, y=450)
                lb2 = Label(text = f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")
                lb2.place(x=325, y = 500)
                lb.after(5000, lambda: lb.destroy())
                lb2.after(5000, lambda: lb2.destroy())

user = Pusher("Боец", 85, 90, 630, 30, "палкой")
def user1():
    global hero
    hero = user
    hero.info()
    game()
    gde_udar()
def Mag1():
    global hero
    hero = Mag
    hero.info()
    game()
    gde_udar()
def Tank1():
    global hero
    hero = Tank
    hero.info()
    game()
    gde_udar()
def Arrow1():
    global hero
    hero = Arrow
    hero.info()
    game()
    gde_udar()
Tank = Pusher("Воин", 110, 145, 550, 45, "клинком")
Arrow = Pusher("Лучник", 45, 275, 350, 20, "луком со стрелами")
Mag = Pusher("Волшебник", 80, 105, 400, 15, "магией")
hero = user
antihero = Pusher("Злодей злой", 55, 140, 400, 8, "арматурой")

def game():
    if hero.health <= 0 and antihero.health <= 0:
        lb = Label(text="Ничья!", background = "sky blue")
        lb.place(x=50, y=270)
        window.after(5100, window.destroy)
    elif hero.health <= 0:
        lb = Label(text=f'Выиграл  {antihero.model}', background = "red")
        lb.place(x=50, y=270)
        window.after(5100, window.destroy)
    elif antihero.health <= 0:
        lb = Label(text=f"Выиграл {hero.model}",background = "green2")
        lb.place(x=50, y=270)
        window.after(5100, window.destroy)
    window.after(1000, game)


img = PhotoImage(file='Walk1.png')
logo = Label(window, image = img)
logo.place(y=10, x=10)
img1 = PhotoImage(file='Attack_2.png')
logo1 = Label(window, image=img1)
logo1.place(y=1200, x=1300)


imgev = PhotoImage(file='Dead.png')
logoev = Label(window, image = imgev)
logoev.place(y=10, x=275)
imgev2 = PhotoImage(file='Dead1.png')
logoev2 = Label(window, image = imgev2)
logoev2.place(y=1200, x=1300)


def gde_udar():
    def udar():
        btn11.place(y=1200, x=1300)
        logo.place(y=1200, x=1300)
        logo.after(5100, lambda: logo.place(y=10, x=10))
        logo1.place(y=10,x=10)
        logo1.after(5100, lambda: logo1.place(y=1200, x=1300))

        logoev.place(y=1200, x=1300)
        logoev.after(5100, lambda: logoev.place(y=10, x=275))
        logoev2.place(y=10, x=275)
        logoev2.after(5100, lambda: logoev2.place(y=1200, x=1300))
        hero.shot(enemy=antihero)
        antihero.shot(enemy=hero)
        btn11.after(5100, lambda: btn11.place(y=485, x=25))

    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn.destroy()
    btn11= Button(window, text = "Атаковать!", activeforeground = "green",activebackground = "pink",width = 25, height = 5, command = udar)
    btn11.place(y=485, x=25)

btn= Button(window, text = "боец", activeforeground = "green",activebackground = "pink",width = 10, height = 10, command = user1)
btn.place(y=380, x=5)
btn1= Button(window, text = "волшебник", activeforeground = "green",activebackground = "pink",width = 10, height = 10, command = Mag1)
btn1.place(y=180, x=5)
btn2= Button(window, text = "лучник", activeforeground = "green",activebackground = "pink",width = 10, height = 10, command = Arrow1)
btn2.place(y=380, x=90)
btn3= Button(window, text = "воин", activeforeground = "green",activebackground = "pink",width = 10, height = 10, command = Tank1)
btn3.place(y=180, x=90)




window.mainloop()