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
        self.encryptMenu = Tkinter.Menu(self.menuBar, tearoff = 0)
        self.encryptMenu.add_command(label="Encrypt", command=self.encrypt_command)
        self.encryptMenu.add_command(label="Decrypt", command=self.decrypt_command)
        self.encryptMenu.add_command(label="Decypher", command=self.decypher_command)
        self.menuBar.add_cascade(label="Encrypt", menu=self.encryptMenu)
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

    def ceasarEncrypt(self,char,rotateBy):
        return chr((ord(char)+rotateBy)%126+1)

    def ceasarDecrypt(self,char,rotateBy):
        return chr((ord(char)- rotateBy-1)%126)

    def encrypt(self, inString, password):
        outString = ""
        index = 0
        for ch in inString:
            ch = self.ceasarEncrypt(ch, ord(password[index]))
            outString= outString +ch
            index = (index+1)%len(password)
        return outString

    def decrypt(self, inString, password):
        outString = ""
        index = 0
        for ch in inString:
            ch = self.caesarDecrypt(ch,ord(password[index]))
            outString = outString + ch
            index = (index+1)%len(password)
            return outString

    def encrypt_command(self):
        password = tkSimpleDialog.askstring("Password", "Please enter your Password")
        if password != None:
            contents = self.textWidget.get("1.0", Tkinter.END)[:-1]
            encrypted = self.encrypt(contents, password)
            self.textWidget.delete("1.0", Tkinter.END)
            self.textWidget.insert(Tkinter.END, encrypted)

    def decrypt_command(self):
        password = tkSimpleDialog.askstring("Password", "Please enter your Password")
        if password != None:
            contents = self.textWidget.get("1.0", Tkinter.END)[:-1]
            encrypted = self.decrypt(contents, password)
            self.textWidget.delete("1.0", Tkinter.END)
            self.textWidget.insert(Tkinter.END, encrypted)

    def decypher(self, contents):
        outstring = ""
        for char in contents:
            x = chr((ord(char))%126+1)
            outstring += x
        return outstring

    def decypher_command(self):
        contents = self.textWidget.get("1.0", Tkinter.END)[:-1]
        decyphered = self.decypher(contents)
        self.textWidget.delete("1.0", Tkinter.END)
        self.textWidget.insert(Tkinter.END, decyphered)

    

if __name__ == "__main__":
    root = Tkinter.Tk()
    textApp = TextEdit(root)
    root.mainloop()
