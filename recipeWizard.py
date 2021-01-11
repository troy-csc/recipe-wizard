# Recipe Wizard
# Program by Troy

# A python tkinter desktop app to store recipes
# and convert between measurement units easily

# github link to my account: https://github.com/troy-csc
# github link to this program: https://github.com/troy-csc/recipe-wizard

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Separator
import sqlite3

# class for a recipe
class Recipe:
    # constructor
    def __init__(self, rName):
        self.rName = rName
    
    # method to get recipe name
    def getRecipeName(self):
        return self.rName

# clears main frame on the main window
def clearMainFrame(mainFrame):
    for child in mainFrame.winfo_children():
        child.destroy()

# list to store recipes
recipeList=[]

# list of units relating to weights
# conversions are stored relative to a gram
weight_units = [
    ["gram", 1],
    ["kilogram", 0.001],
    ["ounce", 0.035274],
    ["pound", 0.00220462]
]

# list of units relating to volume
# conversions are stored relative to a millilitre
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

# global variables for measurement calculator
inputUnit = "unit"
outputUnit = "unit"
unitLock=False

# function to create a recipe
# input: recipe name
# output: index of recipe
def createRecipe(rName):
    recipeList.append(Recipe(rName))
    return len(recipeList)-1

# new recipe button to display the form in the the main window
def newRecipe():
    Label(mainFrame, text="Create a New Recipe").pack()
    Label(mainFrame, text="Enter recipe name:").pack()
    Entry(mainFrame).pack()

# adding numbers to the value entry box
def inputToEntry(inpEntry, num):
    cur=inpEntry.get()
    inpEntry.delete(0, END)
    inpEntry.insert(0, str(cur) + str(num))

# choosing input unit
# click button and then click a unit
def chooseInputUnit(calcWindow, wait_var, inpLabel):
    calcWindow.wait_variable(wait_var)
    global inputUnit
    global unitLock
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
    elif(wait_var.get()>4):
        unitLock=True
        if(wait_var.get()==5):
            inputUnit = "millilitre"
            inpLabel.config(text="ml(s)")
        elif(wait_var.get()==6):
            inputUnit = "litre"
            inpLabel.config(text="litre(s)")
        elif(wait_var.get()==7):
            inputUnit = "decilitre"
            inpLabel.config(text="decilitre(s)")
        elif(wait_var.get()==8):
            inputUnit = "cup"
            inpLabel.config(text="cup(s)")
        elif(wait_var.get()==9):
            inputUnit = "teaspoon"
            inpLabel.config(text="teaspoon(s)")
        elif(wait_var.get()==10):
            inputUnit = "tablespoon"
            inpLabel.config(text="tablespoon(s)")
        elif(wait_var.get()==11):
            inputUnit = "pint"
            inpLabel.config(text="pint(s)")
        elif(wait_var.get()==12):
            inputUnit = "quart"
            inpLabel.config(text="quart(s)")
        elif(wait_var.get()==13):
            inputUnit = "gallon"
            inpLabel.config(text="gallon(s)")

# choosing output unit
# click button and then click a unit
def chooseOutputUnit(calcWindow, wait_var, outLabel):
    calcWindow.wait_variable(wait_var)
    global outputUnit
    global unitLock
    if(unitLock==False):
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
    else:
        if(wait_var.get()==5):
            outputUnit = "millilitre"
            outLabel.config(text="ml(s)")
        elif(wait_var.get()==6):
            outputUnit = "litre"
            outLabel.config(text="litre(s)")
        elif(wait_var.get()==7):
            outputUnit = "decilitre"
            outLabel.config(text="decilitre(s)")
        elif(wait_var.get()==8):
            outputUnit = "cup"
            outLabel.config(text="cup(s)")
        elif(wait_var.get()==9):
            outputUnit = "teaspoon"
            outLabel.config(text="teaspoon(s)")
        elif(wait_var.get()==10):
            outputUnit = "tablespoon"
            outLabel.config(text="tablespoon(s)")
        elif(wait_var.get()==11):
            outputUnit = "pint"
            outLabel.config(text="pint(s)")
        elif(wait_var.get()==12):
            outputUnit = "quart"
            outLabel.config(text="quart(s)")
        elif(wait_var.get()==13):
            outputUnit = "gallon"
            outLabel.config(text="gallon(s)")

# convert button function
# converts input to grams
# converts grams to output unit
def convert(iVal, oEntry):
    factor = 0.0
    # loop through units
    if(unitLock==False):
        for u in weight_units:
            # find factor to convert input unit to grams
            if(u[0] == inputUnit):
                factor = float(weight_units[weight_units.index(u)][1])
                break
        if(inputUnit!="gram"):
            factor=1/factor
        nSTDunit = float(iVal) * factor # number of grams in x number of input units
        for u in weight_units:
            if(u[0] == outputUnit):
                factor = float(weight_units[weight_units.index(u)][1])
                break
        ans = nSTDunit * factor
    else:
        for u in volume_units:
            # find factor to convert input unit to ml
            print(u)
            if(u[0] == inputUnit):
                factor = float(volume_units[volume_units.index(u)][1])
                break
        if(inputUnit!="millilitre"):
            factor=1/factor
        nSTDunit = float(iVal) * factor # number of ml in x number of input units
        for u in volume_units:
            print(u)
            print(outputUnit)
            if(u[0] == outputUnit):
                factor = float(volume_units[volume_units.index(u)][1])
                break
        ans = nSTDunit * factor
    oEntry.delete(0, END)
    oEntry.insert(0, ans)

# creating the measurement calculator window
# and setting up buttons
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
    # volume units
    volUnitFrame = Frame(calcWindow)
    # define volume buttons
    vb_1 = Button(volUnitFrame, text="ml", command=lambda: wait_var.set(5))
    vb_2 = Button(volUnitFrame, text="litre", command=lambda: wait_var.set(6))
    vb_3 = Button(volUnitFrame, text="decilitre", command=lambda: wait_var.set(7))
    vb_4 = Button(volUnitFrame, text="cup", command=lambda: wait_var.set(8))
    vb_5 = Button(volUnitFrame, text="teaspoon", command=lambda: wait_var.set(9))
    vb_6 = Button(volUnitFrame, text="tablespoon", command=lambda: wait_var.set(10))
    vb_7 = Button(volUnitFrame, text="pint", command=lambda: wait_var.set(11))
    vb_8 = Button(volUnitFrame, text="quart", command=lambda: wait_var.set(12))
    vb_9 = Button(volUnitFrame, text="gallon", command=lambda: wait_var.set(13))
    # display volume buttons
    vb_1.grid(row=0, column=0)
    vb_2.grid(row=0, column=1)
    vb_3.grid(row=0, column=2)
    vb_4.grid(row=1, column=0)
    vb_5.grid(row=1, column=1)
    vb_6.grid(row=1, column=2)
    vb_7.grid(row=2, column=0)
    vb_8.grid(row=2, column=1)
    vb_9.grid(row=2, column=2)
    # displaying frames
    displayFrame.grid(row=0, column=0)
    numFrame.grid(row=1, column=0, sticky="w")
    w_unitFrame.grid(row=1, column=0, sticky="s")
    volUnitFrame.grid(row=1, column=0, sticky="e")

# initializing root window
root = tk.Tk()
root.title("Recipe Wizard")

# setting up root window grid
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

# creating frames
mainFrame = tk.Frame(root)
bttnsFrame = tk.Frame(root)

# placing buttons are frames on the window using tkinter grid
btn_newRc = tk.Button(bttnsFrame, text="New Recipe", command=newRecipe).grid(row=0, column=0, pady=2.5, sticky="ew")
btn_saveRc = tk.Button(bttnsFrame, text="Save").grid(row=1, column=0, sticky="ew", pady=2.5)
btn_clr = tk.Button(bttnsFrame, text="Clear", command=lambda: clearMainFrame(mainFrame)).grid(row=2, column=0, sticky="ew", pady=2.5)
btn_calc = tk.Button(bttnsFrame, text="Open Calculator", command=openCalc).grid(row=3, column=0, pady=2.5, sticky="ew")
mainFrame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
bttnsFrame.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

# main window loop
root.mainloop()