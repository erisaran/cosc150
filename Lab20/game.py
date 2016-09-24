from Tkinter import *
import random
from math import sqrt

class CatchGame:
    def __init__(self,parent,width=200,height=200,ball_size=20,wait_time=20):
        self.canvas = Canvas(parent, width=width,height=height)
        self.canvas.grid(column=0,row=0)
        self.canvas.wait_visibility()

        #ball stuff
        self.ball_size = ball_size
        self.wait_time = wait_time
        self.x = 10
        self.y = random.randint(10,height-ball_size)
        self.dx = 2
        self.dy = random.randint(-5,5)
        self.ball = self.canvas.create_oval(self.x,self.y,
                                            self.x+ball_size,self.y+ball_size,
                                            fill="blue")
        self.canvas.after(wait_time, self.move)

    def move(self):
        self.x = self.x+self.dx
        self.y = self.y+self.dy
        if self.y<0:
            self.y = 0
            self.dy = -self.dy
        elif self.y>self.canvas.winfo_height()-self.ball_size:
            self.y = self.canvas.winfo_height()-self.ball_size
            self.dy = -self.dy
        self.canvas.coords(self.ball, self.x, self.y,
                           self.x+self.ball_size, self.y+self.ball_size)
        self.canvas.after(self.wait_time, self.move)

root = Tk()
game = CatchGame(root,width=400,height=400,ball_size=5,wait_time=10)
root.mainloop()
