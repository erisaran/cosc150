import Tkinter
import ScrolledText
import tkFileDialog

class TextEdit:
    """
    A simple text editor using a ScrolledText widget.
    """
    def __init__(self, parent):
        self.parent = parent
        self.commandBar = Tkinter.Frame(parent)
        self.commandBar.grid(row=0, column=0)
        self.openButton = Tkinter.Button(self.commandBar, text="Open",
                                         command=self.open_command)
        self.saveButton = Tkinter.Button(self.commandBar, text="Save",
                                         command=self.save_command)
        self.exitButton = Tkinter.Button(self.commandBar, text="Exit",
                                          command=self.exit_program)
        self.openButton.grid(row=0,column=0)
        self.saveButton.grid(row=0,column=1)
        self.exitButton.grid(row=0,column=2)
        
        self.textWidget = ScrolledText.ScrolledText(parent, width=80, height=50)
        self.textWidget.grid(row=1, column=0)

        self.menuBar = Tkinter.Menu(parent, tearoff=0)
        self.fileMenu = Tkinter.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Open", command=self.open_command)
        self.fileMenu.add_command(label="Save", command=self.save_command)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Quit", command=self.exit_program)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        parent.config(menu=self.menuBar)

    def open_command(self):
        file = tkFileDialog.askopenfile()
        if file != None:
            contents = file.read()
            self.textWidget.delete("1.0", Tkinter.END)
            self.textWidget.insert(Tkinter.END, contents)

    def save_command(self):
        file = tkFileDialog.asksaveasfile()
        if file != None:
            contents = self.textWidget.get("1.0", Tkinter.END)[:-1]
            file.write(contents)
            file.close()

    def exit_program(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = Tkinter.Tk()
    textApp = TextEdit(root)
    root.mainloop()
