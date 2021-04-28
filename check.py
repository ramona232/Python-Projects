from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Codemy")
root.iconbitmap("codemy.ico")
root.geometry("400x400")


def show():
    my_Label = Label(root, text=var.get()).pack()

var = StringVar()

c =Checkbutton(root, text="Would you like to SuperSize your order? Check here!", variable=var, onvalue="Supersize", offvalue="Regularsize")
c.deselect()
c.pack()



my_Button = Button(root, text="Show Selection", command=show).pack()




root.mainloop()