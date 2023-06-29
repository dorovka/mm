import random
from tkinter import *
window = Tk()
h = 600
w = 600
window.geometry(f"{w}x{h}")

canvas = Canvas(window, width=w,height = h)
canvas.place(in_=window, x=0, y=0)

bg_photo = PhotoImage(file="bg_2.png")




class Knight:
    def __init__(self):
        self.x = 70
        self.y = h//2
        self.v = 0
        self.v2 = 0
        self.photo = PhotoImage(file = "knight.png")



    def up(self, event):
        self.v = -5

    def down(self, event):
        self.v = +5

    def right(self, event):
        self.v2 = +5

    def left(self, event):
        self.v2 = -5

    def stop(self, event):
        self.v = 0
        self.v2 = 0




class Dragons:
    def __init__(self):
        self.x = random.randint(750, 1500)
        self.y = random.randint(100, 500)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file = "dragon.png")


knight = Knight()
dragons = []

for i in range(10):
    dragons.append(Dragons())


def game():
    canvas.delete("all")
    canvas.create_image(w // 2, h // 2, image=bg_photo)
    knight.y += knight.v
    knight.x += knight.v2
    canvas.create_image(knight.x, knight.y, image = knight.photo)
    if knight.x < 30:
        knight.x = 30
    if knight.x > w-30:
        knight.x = w-30

    if knight.y < 30:
        knight.y = 30
    if knight.y > h-30:
        knight.y = h-30

    kill_dragon = -1
    for i,dragon in enumerate(dragons):
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

        if (dragon.x - knight.x)**2 + (dragon.y - knight.y)**2 <= 110**2:
          kill_dragon = i

        if dragon.x <0:
            canvas.delete("all")
            canvas.create_text(w // 2, h // 2, text="Вы проиграли!", font="Verdana 42", fill="red")
            break

    if kill_dragon > -1:
        del dragons[kill_dragon]

    if len(dragons) == 0:
        canvas.delete("all")
        canvas.create_text(w//2, h//2, text = "Вы выиграли!", font = "Verdana 42", fill = "green")
    window.after(5, game)

game()


window.bind("<Key-Up>", knight.up)
window.bind("<w>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind("<s>", knight.down)

window.bind("<Key-Left>", knight.up)
window.bind("<a>", knight.left)
window.bind("<Key-Right>", knight.down)
window.bind("<d>", knight.right)

window.bind("<KeyRelease>", knight.stop)

window.mainloop()