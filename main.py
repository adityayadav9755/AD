# Importing
import functions
from tkinter import *

# Setup & Variables
func = functions.Function()
root = Tk()
root.geometry("1000x800")
root.title("AD")

# Functions
def record():
    cmnd = func.recognize()
    func.process(cmnd, func)
    cmnd = []

# Images
bg = PhotoImage(file="Background.png")
Mic = PhotoImage(file="Mic.png")

# Frames
frame1 = Frame(root, bg="black", borderwidth=5)
frame1.grid(row=0, column=0)

# Labels
l1 = Label(frame1, text='''Hi! AD this side.\n 
What can I do for you today?''', bg="black", font="ComicSansMS 10 italic", fg="white")
l1.grid(row=0, column=0)
l1.grid_location(0,0)
l2 = Label(root, image=bg)
l2.grid(row=0, column=10)
l2.grid_location(15,0)

# Buttons
b1 = Button(frame1, image=Mic, command=record, borderwidth=0, relief=FLAT)
b1.grid(row=2, column=0)

root.mainloop()
