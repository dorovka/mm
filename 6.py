from tkinter import *

window = Tk()
window.geometry("800x600")
window.title("кубики")
canvas = Canvas(window, width = 800, height = 600, background = "black")
canvas.pack()
"""
canvas.create_rectangle(150, 150, 300, 300, fill="wheat4", outline = "")
canvas.create_rectangle(200, 200, 250, 250, fill="CadetBlue3", outline = "")
canvas.create_polygon(140, 150, 225, 110, 310, 150, fill = "tomato3", outline = "")"""


class House:
    def __init__(self, w_color, r_color, height, width):
        self.w_color = w_color
        self.r_color = r_color
        self.height = height
        self.width = width

    def Build_house(self, x, y):
        h = self.height
        w = self.width
        canvas.create_rectangle(x-h/3, y+h/3, x+h/3, y+h, fill=self.w_color, outline="")

        canvas.create_polygon(x-w/2, y+h/3, x, y, x+w/2, y+h/3, fill=self.r_color, outline="")
house = House("cyan", "brown", 150, 100)
house2 = House("green", "brown", 100, 150)
house.Build_house(150, 150)
house2.Build_house(440, 350)
window.mainloop()