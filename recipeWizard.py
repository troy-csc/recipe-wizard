# Recipe Wizard
# Program by Troy

import tkinter as tk
from tkinter import *

class Recipe:
    def __init__(self, rName):
        self.rName = rName
    
    def getRecipeName(self):
        return self.rName

def clearMainFrame(mainFrame):
    for child in mainFrame.winfo_children():
        child.destroy()

recipeList=[]

# input: recipe name
# output: index of recipe
def createRecipe(rName):
    recipeList.append(Recipe(rName))
    return len(recipeList)-1

# initializing root window
root = tk.Tk()
root.title("Recipe Wizard")

# setting up root window grid
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

mainFrame = tk.Frame(root)
bttnsFrame = tk.Frame(root)

btn_newRc = tk.Button(bttnsFrame, text="New Recipe").grid(row=0, column=0, pady=2.5, sticky="ew")
btn_saveRc = tk.Button(bttnsFrame, text="Save").grid(row=1, column=0, sticky="ew", pady=2.5)
btn_clr = tk.Button(bttnsFrame, text="Clear", command=lambda: clearMainFrame(mainFrame)).grid(row=2, column=0, sticky="ew", pady=2.5)

mainFrame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
bttnsFrame.grid(row=0, column=0, sticky="ns", padx=5, pady=5)



root.mainloop()