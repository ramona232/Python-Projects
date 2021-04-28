from tkinter import*
from PIL import ImageTk, Image


root = Tk()
root.title("Codemy")
root.iconbitmap("codemy.ico")
root.geometry("400x400")

#Drop Down Boxes
def show():
    my_Label = Label(root, text=clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options )
drop.pack()

my_Button = Button(root, text=" Show selection ", command=show).pack()




root.mainloop()