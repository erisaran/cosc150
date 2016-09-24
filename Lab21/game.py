from Tkinter import *
import random
from math import sqrt

class CatchGame:
    def __init__(self,parent,width=200,height=200,ball_size=20,wait_time=20,
                 mitt_size=20):
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

        #mitt stuff
        self.mittx = width-30
        self.mitty = height/2
        self.mitt_size = mitt_size
        self.mitt = self.canvas.create_oval(self.mittx, self.mitty,
                                            self.mittx+self.mitt_size,
                                            self.mitty+self.mitt_size,fill="red")
        parent.bind("k",self.move_mitt)
        parent.bind("j",self.move_mitt)

        self.scores = Label(parent,text="Computer 0: Player 0")
        self.scores.grid(column-0,row=1)
        self.computer_score = 0
        self.player_score = 0
        
    def restart(self):
        self.x = 0
        self.y = random.randint(0,self.canvas.winfo_height()-self.ball_size)
        self.dy = random.randint(-5,5)
        self.canvas.after(self.wait_time*10,self.move)

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
        ball_centre_x = self.x + self.ball_size/2.0
        ball_centre_y = self.y + self.ball_size/2.0
        mitt_centre_x = self.mittx + self.mitt_size/2.0
        mitt_centre_y = self.mitty + self.mitt_size/2.0
        distance = sqrt((ball_centre_x-mitt_centre_x)**2+
                        (ball_centre_y-mitt_centre_y)**2)
        #caught?
        if distance<=(self.ball_size+self.mitt_size)/2.0:
            print "Good Catch"
            self.restart()
        #missed
        elif self.x>self.canvas.winfo_width():
            print "You missed"
            self.restart()
        #not reached
        else:
            #call again
            self.canvas.after(self.wait_time,self.move)

    def move_mitt(self,event):
        if event.char=="j":
            self.mitty = self.mitty+10
        elif event.char=="k":
            self.mitty = self.mitty-10
        self.canvas.coords(self.mitt,self.mittx,self.mitty,
                           self.mittx+self.mitt_size,self.mitty+self.mitt_size)
    def restart(self):
        self.x = 0
        self.y = random.randint(0,self.canvas.winfo_height()-self.ball_size)
        self.dy = random.randint(-5,5)
        self.canvas.after(self.wait_time*10,self.move)

root = Tk()
game = CatchGame(root,width=400,height=400,ball_size=5,wait_time=10)
root.mainloop()
