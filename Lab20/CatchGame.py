from Tkinter import *

class CatchGame:
    def __init__(self,parent):
        self.canvas = Canvas(parent, width=200, height=200)
        self.canvas.grid(column=0, row=0)
        self.ball = self.canvas.create_oval(90,90,110,110,fill="blue")

    def move(self):
        self.canvas.coords(self.ball, 150, 150, 170, 170)


root = Tk()
app = CatchGame(root)
root.mainloop()
