from tkinter import *

window = Tk()
window.geometry("800x600")
window.title("Рыбалка")
canvas = Canvas(window, width = 800, height = 600, background = "black")
canvas.pack()
"""
canvas.create_rectangle(150, 150, 300, 300, fill="wheat4", outline = "")
canvas.create_rectangle(200, 200, 250, 250, fill="CadetBlue3", outline = "")
canvas.create_polygon(140, 150, 225, 110, 310, 150, fill = "tomato3", outline = "")"""


class Fish:
    def __init__(self, w_color, r_color, height, width):
        self.w_color = w_color
        self.r_color = r_color
        self.height = height
        self.width = width

    def Put_fish(self, x, y):
        h = self.height
        w = self.width
        canvas.create_rectangle(x, y, x+w, y+h, fill=self.w_color, outline="")

        canvas.create_polygon(x+w, y, x+w*1.5, y+h/2, x+w, y+h, fill=self.r_color, outline="")
        canvas.create_polygon(x - w, y, x, y + h / 2, x - w, y + h, fill=self.r_color, outline="")
house = Fish("cyan", "brown", 150, 100)
house2 = Fish("green", "brown", 100, 150)
house.Put_fish(150, 150)
house2.Put_fish(440, 350)
window.mainloop()