from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Unit Converter")
        self.geometry("900x300")
        self.configure(padx=10, pady=10)
        # variable define
        self.showLeftTemp  = StringVar(value="\"Select temperature unit.\"")
        self.showRightTemp = StringVar(value="\"Select temperature unit.\"")
        self.tempList = ["Celsius", "Fahrenheit", "Kelvin", "Romer"]
        self.numLeft = DoubleVar()
        self.numRight = DoubleVar()
        
        self.create_widgets() # create widgets
        
    def create_widgets(self):
        lb1 = ttk.Label(self, text="Temperatur Unit Converter", font=("Helvetica",25))
        # frame 1 2 row 2 column ##########
        frame1 = Frame(self)
        # combobox ######
        self.cb_left = ttk.Combobox(frame1, values=self.tempList, state="readonly", width=10, textvariable=self.showLeftTemp, font=("Helvetica",25))
        self.cb_right = ttk.Combobox(frame1, values=self.tempList, state="readonly", width=10, textvariable=self.showRightTemp, font=("Helvetica",25))
        # if focus
        self.cb_left.config(validate="focus", validatecommand=self.isSelectUnit)
        self.cb_right.config(validate="focus", validatecommand=self.isSelectUnit)
        #############
        lb_left = ttk.Label(frame1, textvariable=self.showLeftTemp, font=("Helvetica",25)) # show unit convert from
        lb_right = ttk.Label(frame1, textvariable=self.showRightTemp, font=("Helvetica",25)) # show unit convert to
        self.entLeft = ttk.Entry(frame1, textvariable=self.numLeft, style="TEntry", font=("Helvetica", 25)) # entry value 
        self.entRight = ttk.Entry(frame1, textvariable=self.numRight, state="readonly", font=("Helvetica",25)) # show value after converte
        # frame1 grid
        self.cb_left.grid(row=0,column=0)
        ttk.Label(frame1, text="to", font=("Helvetica",25)).grid(row=0,column=1)
        self.cb_right.grid(row=0,column=2)
        lb_left.grid(row=1, column=0)
        lb_right.grid(row=1,column=2)
        self.entLeft.grid(row=2,column=0)
        self.entRight.grid(row=2,column=2)
        ###################################

        # self.widget pack
        lb1.pack(expand=True)
        frame1.pack(expand=True)
        # mouse move detect
        self.bind("<Enter>", self.getFromCombobox)
    
    # show a message when both is not a temperature unit.
    def isSelectUnit(self):
        self.thisUnit = self.cb_left.get()
        self.toUnit = self.cb_right.get()
        # if some of them does not select and other does
        if (self.thisUnit != "\"Select temperature unit.\"" and self.toUnit == "\"Select temperature unit.\"") or (self.thisUnit == "\"Select temperature unit.\"" and self.toUnit != "\"Select temperature unit.\""):
            messagebox.showwarning("Warning", "Please select a unit to convert")
    
    # take values from temperature unit from comboboxes and values from entries
    def getFromCombobox(self, event):
        self.thisUnit = self.cb_left.get()
        self.toUnit = self.cb_right.get()
        if self.thisUnit == "Celsius": # convert from celsius
            self.celFunc()
        elif self.thisUnit == "Fahrenheit": # convert from fahrenheit
            self.faFunc()
        elif self.thisUnit == "Kelvin": # convert from kelvin
            self.kelFunc()
        elif self.thisUnit == "Romer": # convert from romer
            self.roFunc()
    
    # convert from celsius
    def celFunc(self):
        if self.toUnit == "Celsius": # to celsius
            self.numRight.set(self.numLeft.get())
        elif self.toUnit == "Fahrenheit": # to fahrenheit
            c = self.numLeft.get()
            f = (9 * c / 5) + 32
            f = round(f, 2)
            self.numRight.set(f)
        elif self.toUnit == "Kelvin": # to kelvin
            c = self.numLeft.get()
            k = c + 273
            k = round(k, 2)
            self.numRight.set(k)
        elif self.toUnit == "Romer": # to romer
            c = self.numLeft.get()
            r = 4 * c / 5
            r = round(r, 2)
            self.numRight.set(r)
    
    # convert from fahrenheit
    def faFunc(self):
        if self.toUnit == "Celsius": # to celsius
            f = self.numLeft.get()
            c = (5 * (f -32)) / 9
            c = round(c, 2)
            self.numRight.set(c)
        elif self.toUnit == "Fahrenheit": # to fahrenheit
            self.numRight.set(self.numLeft.get())
        elif self.toUnit == "Kelvin": # to kelvin
            f = self.numLeft.get()
            k = (5 * (f - 32) / 9) + 273
            k = round(k, 2)
            self.numRight.set(k)
        elif self.toUnit == "Romer": # to romer
            f = self.numLeft.get()
            r = (4 * (f - 32)) / 9
            r = round(r, 2)
            self.numRight.set(r)
    
    # convert from kelvin
    def kelFunc(self):
        if self.toUnit == "Celsius": # to celsius
            k = self.numLeft.get()
            c = k - 273
            c = round(c, 2)
            self.numRight.set(c)
        elif self.toUnit == "Fahrenheit": # to fahrenheit
            k = self.numLeft.get()
            f = (9 * (k - 273)) / 5
            f = round(f, 2)
            self.numRight.set(f)
        elif self.toUnit == "Kelvin": # to kelvin
            self.numRight.set(self.numLeft.get()) # to romer
        elif self.toUnit == "Romer":
            k = self.numLeft.get()
            r = (4 * (k - 273)) / 5
            r = round(r, 2)
            self.numRight.set(r)
    
    # convert from romer
    def roFunc(self):
        if self.toUnit == "Celsius": # to celsius
            r = self.numLeft.get()
            c = 5 * r / 4
            c = round(c, 2)
            self.numRight.set(c)
        elif self.toUnit == "Fahrenheit": # to fahrenheit
            r = self.numLeft.get()
            f = (9 * r / 4) + 32
            f = round(f, 2)
            self.numRight.set(f)
        elif self.toUnit == "Kelvin": # to kelvin
            r = self.numLeft.get()
            k = (5 * r / 4) + 273
            k = round(k, 2)
            self.numRight.set(k)
        elif self.toUnit == "Romer": # to romer
            self.numRight.set(self.numLeft.get())
            
if __name__ == "__main__":
    app = App()
    app.mainloop()