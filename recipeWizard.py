# Recipe Wizard
# Program by Troy

from tkinter import *

class Recipe:
    

# matrix for unit conversions
row, col = 3, 3
conversionMatrix = [[0 for i in range(col)] for i in range(row)]
print(conversionMatrix)

# setting up matrix
for row in range(len(conversionMatrix)):
    for col in range(len(conversionMatrix[row])):
        if(row==col):
            conversionMatrix[row][col]=1
        elif(row<col):
            if(row==0 and col==1):
                conversionMatrix[row][col]=0.001
            elif(row==0 and col==2):
                conversionMatrix[row][col]=3.281
            elif(row==1 and col==2):
                conversionMatrix[row][col]=3281
        elif(row>col):
            conversionMatrix[row][col]=1/conversionMatrix[col][row]

# menu for units
options = [
    "Metres",
    "Kilometres",
    "Feet"
]

# debugging
print(conversionMatrix)

# initializing root window
root = Tk()
root.title("Recipe Wizard")

# function to calculate conversion
def calculate(input, iUnit, oUnit, ansBox):
    print(iUnit)
    print(oUnit)

# Entry for amount
amountLabel = Label(root, text="Enter an amount: ").grid(row=0, column=0)
amtEntry = Entry(root, width=25)
amtEntry.grid(row=0, column=1)

# option for amount unit
amtUnitName = StringVar()
amtUnitDrop = OptionMenu(root, amtUnitName, "Metres", "Kilometres", "Feet").grid(row=0, column=2, columnspan=2)

# option for unit to convert to
amountLabel = Label(root, text="Choose a unit to convert: ").grid(row=1, column=0)
cUnitName = StringVar()
cUnitDrop = OptionMenu(root, cUnitName, "Metres", "Kilometres", "Feet").grid(row=1, column=1, columnspan=2)

# answer box
ansBox = Entry(root, width=25).grid(row=2, column=1)
ansButton = Button(root, text="Convert", command=lambda: calculate(amtEntry.get(), amtUnitName, cUnitName, ansBox)).grid(row=2, column=0)

root.mainloop()