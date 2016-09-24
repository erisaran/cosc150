from Tkinter import *

class House:
    def __init__(self, parent, x=0, y=0, colour="white",width=100,height=100):
        self.canvas = Canvas(parent, width=400, height=400)
        self.canvas.grid(column=0,row=0)
        a=100
        mx=width/100.0
        my=height/100.0
        self.house = self.canvas.create_rectangle(x+a,y+a,(x+width+a),(y+width+a),fill=colour)
        self.door = self.canvas.create_rectangle(x+35+a,y+55+a,(a+x+65)*mx,height+a+y,fill="white")
        self.window1 = self.canvas.create_rectangle((a+x+15)*mx,(a+y+15)*my, (a+x+40)*mx, (a+y+40)*my,fill="white")
        self.window2 = self.canvas.create_rectangle((a+x+60)*mx,(a+y+15)*my,(a+x+85)*mx,(a+y+40)*my,fill="white")
        self.roof = self.canvas.create_line(x+a,y+a,(a+x+50)*mx,(a+y-35)*my,(a+x+100)*mx,(a+y)*my,)




root = Tk()
app = House(root)
House(root,100,100,"blue")
root.mainloop()
