from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To Code")
root.iconbitmap("codemy.ico")

frame = LabelFrame(root, padx=5, pady=5)
frame.pack(padx=10, pady=10) 

b = Button(frame, text="Don't Clik Here!")
b2 =Button(frame, text="... or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)





root.mainloop()
