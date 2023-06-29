from tkinter import *
import time

class Ball():
    def __init__(self, canvas, color, platform):
        self.platform = platform
        self.canvas = canvas
        self.v = 2
        self.x = self.v
        self.y = self.v
        self.oval = self.canvas.create_oval(250, 200, 265, 215, fill=color)
        self.gameover = False

    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rectangle)
        if platform_pos[1] <= ball_pos[3] <= platform_pos[3]:
            if ball_pos[0] < platform_pos[2] and ball_pos[2] > platform_pos[0]:
                return True
        return False


    def draw(self):
        self.canvas.move(self.oval,self.x,self.y)
        pos = self.canvas.coords(self.oval)
        if self.touch_platform(pos) == True:
            self.y = -self.v
        if pos[0] <=0:
            self.x = self.v
        if pos[2] >=500:
            self.x = -self.v
        if pos[1] <=0:
            self.y = self.v
        if pos[3] >= 400:
            self.y = -self.v
            self.gameover = True


class Platform():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.v = 3
        self.x = 0
        self.rectangle = canvas.create_rectangle(250, 350, 300, 360, fill = color)
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)
        self.canvas.bind_all("<KeyRelease>", self.stop)
    def stop(self, event):
        self.x = 0
    def draw(self):
        self.canvas.move(self.rectangle, self.x, 0)
        pos =self.canvas.coords(self.rectangle)
        if pos[0] <=0:
            self.x = -self.x
        if pos[2] >=500:
            self.x = -self.x
    def left(self, event):
        self.x = -self.v
    def right(self, event):
        self.x = self.v
class Rectangle():
    pass







window = Tk()
window.title('Arcanoid')
window.resizable(0, 0)

canvas = Canvas(window, width = 500, height = 400)
canvas.pack()
platform = Platform(canvas, 'green')
ball = Ball(canvas, 'red', platform)



while True:
    if ball.gameover == True:
        break
    else:
        platform.draw()
        ball.draw()
        window.update()
        time.sleep(0.01)