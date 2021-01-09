# Recipe Wizard
# Program by Troy

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Separator
import sqlite3

class Recipe:
    def __init__(self, rName):
        self.rName = rName
    
    def getRecipeName(self):
        return self.rName

def clearMainFrame(mainFrame):
    for child in mainFrame.winfo_children():
        child.destroy()

recipeList=[]

weight_units = [
    ["gram", 1],
    ["kilogram", 0.001],
    ["ounce", 0.035274],
    ["pound", 0.00220462]
]

volume_units = [
    ["millilitre", 1],
    ["litre", 0.001],
    ["decilitre", 0.01],
    ["cup", 1/237],
    ["teaspoon", 1/4.929],
    ["tablespoon", 1/14.781],
    ["pint", 1/473],
    ["quart", 1/946],
    ["gallon", 1/3785]
]

inputUnit = "unit"
outputUnit = "unit"

# input: recipe name
# output: index of recipe
def createRecipe(rName):
    recipeList.append(Recipe(rName))
    return len(recipeList)-1

def newRecipe():
    Label(mainFrame, text="Create a New Recipe").pack()
    Label(mainFrame, text="Enter recipe name: ").pack()
    Entry(mainFrame).pack()

def inputToEntry(inpEntry, num):
    cur=inpEntry.get()
    inpEntry.delete(0, END)
    inpEntry.insert(0, str(cur) + str(num))

def chooseInputUnit(calcWindow, wait_var, inpLabel):
    calcWindow.wait_variable(wait_var)
    global inputUnit
    if(wait_var.get()==1):
        inputUnit = "gram"
        inpLabel.config(text="gram(s)")
    elif(wait_var.get()==2):
        inputUnit = "kilogram"
        inpLabel.config(text="kilogram(s)")
    elif(wait_var.get()==3):
        inputUnit = "ounce"
        inpLabel.config(text="ounce(s)")
    elif(wait_var.get()==4):
        inputUnit = "pound"
        inpLabel.config(text="pound(s)")

def chooseOutputUnit(calcWindow, wait_var, outLabel):
    calcWindow.wait_variable(wait_var)
    global outputUnit
    if(wait_var.get()==1):
        outputUnit = "gram"
        outLabel.config(text="gram(s)")
    elif(wait_var.get()==2):
        outputUnit
        outputUnit = "kilogram"
        outLabel.config(text="kilogram(s)")
    elif(wait_var.get()==3):
        outputUnit = "ounce"
        outLabel.config(text="ounce(s)")
    elif(wait_var.get()==4):
        outputUnit = "pound"
        outLabel.config(text="pound(s)")

def convert(iVal, oEntry):
    factor = 0.0
    for u in weight_units:
        if(u[0] == inputUnit):
            factor = float(weight_units[weight_units.index(u)][1])
            break
    nSTDunit = float(iVal) * factor
    for u in weight_units:
        print(u)
        print(outputUnit)
        if(u[0] == outputUnit):
            factor = float(weight_units[weight_units.index(u)][1])
            print(factor)
            break
    ans = nSTDunit * factor
    oEntry.delete(0, END)
    oEntry.insert(0, ans)

def openCalc():
    calcWindow = tk.Toplevel(height=500, width=500)
    calcWindow.title("Measurement Converter")
    displayFrame = tk.Frame(calcWindow)
    inpEntry = Entry(displayFrame)
    inpEntry.grid(row=0, column=0)
    inpLabel = Label(displayFrame, text="unit(s)")
    inpLabel.grid(row=0, column=1)
    Label(displayFrame, text="--->").grid(row=0, column=2)
    outEntry = Entry(displayFrame)
    outEntry.grid(row=0, column=3)
    outLabel = Label(displayFrame, text="unit(s)")
    outLabel.grid(row=0, column=4)
    wait_var = IntVar()
    iButton = Button(displayFrame, text="Choose input unit", command=lambda: chooseInputUnit(calcWindow, wait_var, inpLabel)).grid(row=1, column=1)
    oButton = Button(displayFrame, text="Choose output unit", command=lambda: chooseOutputUnit(calcWindow, wait_var, outLabel)).grid(row=1, column=4)
    convertButton = Button(displayFrame, text="Convert", command=lambda: convert(inpEntry.get(), outEntry))
    convertButton.grid(row=2, column=2)
    numFrame = tk.Frame(calcWindow)
    # define buttons
    b_1 = Button(numFrame, text="1", command=lambda: inputToEntry(inpEntry, 1))
    b_2 = Button(numFrame, text="2", command=lambda: inputToEntry(inpEntry, 2))
    b_3 = Button(numFrame, text="3", command=lambda: inputToEntry(inpEntry, 3))
    b_4 = Button(numFrame, text="4", command=lambda: inputToEntry(inpEntry, 4))
    b_5 = Button(numFrame, text="5", command=lambda: inputToEntry(inpEntry, 5))
    b_6 = Button(numFrame, text="6", command=lambda: inputToEntry(inpEntry, 6))
    b_7 = Button(numFrame, text="7", command=lambda: inputToEntry(inpEntry, 7))
    b_8 = Button(numFrame, text="8", command=lambda: inputToEntry(inpEntry, 8))
    b_9 = Button(numFrame, text="9", command=lambda: inputToEntry(inpEntry, 9))
    # display buttons
    b_1.grid(row=0, column=0)
    b_2.grid(row=0, column=1)
    b_3.grid(row=0, column=2)
    b_4.grid(row=1, column=0)
    b_5.grid(row=1, column=1)
    b_6.grid(row=1, column=2)
    b_7.grid(row=2, column=0)
    b_8.grid(row=2, column=1)
    b_9.grid(row=2, column=2)
    w_unitFrame = Frame(calcWindow)
    # define weight buttons
    wb_1 = Button(w_unitFrame, text="gram", command=lambda: wait_var.set(1))
    wb_2 = Button(w_unitFrame, text="kilogram", command=lambda: wait_var.set(2))
    wb_3 = Button(w_unitFrame, text="ounce", command=lambda: wait_var.set(3))
    wb_4 = Button(w_unitFrame, text="pound", command=lambda: wait_var.set(4))
    # display weight buttons
    wb_1.grid(row=0, column=0)
    wb_2.grid(row=0, column=1)
    wb_3.grid(row=1, column=0)
    wb_4.grid(row=1, column=1)
    displayFrame.grid(row=0, column=0)
    numFrame.grid(row=1, column=0, sticky="w")
    w_unitFrame.grid(row=1, column=1, sticky="s")

# initializing root window
root = tk.Tk()
root.title("Recipe Wizard")

# setting up root window grid
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

mainFrame = tk.Frame(root)
bttnsFrame = tk.Frame(root)

btn_newRc = tk.Button(bttnsFrame, text="New Recipe", command=newRecipe).grid(row=0, column=0, pady=2.5, sticky="ew")
btn_saveRc = tk.Button(bttnsFrame, text="Save").grid(row=1, column=0, sticky="ew", pady=2.5)
btn_clr = tk.Button(bttnsFrame, text="Clear", command=lambda: clearMainFrame(mainFrame)).grid(row=2, column=0, sticky="ew", pady=2.5)
btn_calc = tk.Button(bttnsFrame, text="Open Calculator", command=openCalc).grid(row=3, column=0, pady=2.5, sticky="ew")
mainFrame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
bttnsFrame.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

root.mainloop()