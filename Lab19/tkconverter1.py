from Tkinter import *

class TempConverter:
    """
    A simple app for converting from Fahrenheit to Celsius
    """
    def __init__(self,parent):
        self.celsius_val = Label(parent, text="", width=20)
        self.celsius_val.grid(column=1,row=1)
        self.celsius_label = Label(parent, text="Celcius", width=20)
        self.celsius_label.grid(column=1, row=0)

        self.fahr_input = Entry(parent)
        self.fahr_input.grid(column=0,row=1)
        self.fahr_label = Label(parent, text="Fahrenheit")
        self.fahr_label.grid(column=0, row=0)

        self.convert_button = Button(parent, text="Convert", command=self.convert)
        self.convert_button.grid(row=2, column=0)

        self.quit_button = Button(parent, text="Quit", command=parent.destroy)
        self.quit_button.grid(row=2, column=1)

        self.forward_button = Checkbutton(parent, text="do forward conversion", command=self.toggle_convert)
        self.forward_button.grid(column=0,row=3)

        self.x = 0

    def convert(self):
        # get the fahrenheit value from the widget and convert it from
        # a string to a float number
        dfahr = float(self.fahr_input.get())
        forwardConvert = self.toggle_convert()
        if self.forwardConvert == True:
            celsius = self.convert_f_to_c(dfahr)
        else:
            celsius = self.ctof(dfahr)
        self.celsius_val.configure(text = str(celsius))

        
    def convert_f_to_c(self, fahr):
        """
        Convert from fahrenheit to celsius. The variable self is the object parameter.
        >>> testConvert = TempConverter(Tk())
        >>> c = testConvert.convert_f_to_c(-40)
        >>> abs(c+40.0)<1e-8
        True
        >>> c = testConvert.convert_f_to_c(100)
        >>> abs(c-37.7777777777)<1e-8
        True
        """
        c = (fahr-32)*5.0/9.0
        return c

    def ctof(self, cel):
        """
        >>> testconvert = TempConverter(Tk())
        >>> f = testconvert.ctof(0)
        >>> abs(f-32)<1e-8
        True
        >>> f = testconvert.ctof(37.7777777777777)
        >>> abs(f-100)<1e-8
        True
        """
        f = (cel*9.0/5.0)+32
        return f

    def toggle_convert(self):
        forwardConvert = self.forward_button()
        return forwardConvert


root = Tk()
app = TempConverter(root)
import doctest
doctest.testmod()
root.mainloop()
