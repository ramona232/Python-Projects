from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To Code")
root.iconbitmap("codemy.ico")

#r = IntVar()
#r.set("2")

TOPPINGS = [
    ("Peperoni", "Peperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Peperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#my_label = Label(root, text=pizza.get())
#my_label.pack()

my_button = Button(root, text="Click me", command= lambda: clicked(pizza.get()))
my_button.pack()



root.mainloop()