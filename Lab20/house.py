from Tkinter import *



def draw_house(x, y, colour):
    houseCanvas = Canvas(root, width=400, height=400)
    houseCanvas.grid(row=0, column=0)

    houseCanvas.create_rectangle(x+20, y+380, x+120, y+280, fill=colour) # the house
    houseCanvas.create_rectangle(x+55, y+380, x+85, y+330, fill="white") # the door
    houseCanvas.create_rectangle(x+40, y+320, x+60, y+300, fill="white") # left window
    houseCanvas.create_rectangle(x+80, y+320, x+100, y+300,fill="white") # right window
    houseCanvas.create_line(x+20, y+280, x+70, y+240, x+120, y+280) # the roof

root = Tk()
draw_house(0, 0, "blue")
draw_house(50,-50,"red")
draw_house(150,-150,"green")
root.mainloop()
