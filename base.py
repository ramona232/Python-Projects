from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Image Viewer!")
root.iconbitmap("Photo.ico")

def open():
    global my_image   
    top = Toplevel()
    top.title("My second window!")
    top.iconbitmap("Photo.ico")
    my_image = ImageTk.PhotoImage(Image.open("images/Om.jpg"))
    my_label = Label(top, image=my_image).pack()
    btn2 = Button(top, text ="close window", command=top.destroy).pack()

btn = Button(root, text="Open second wondow!", command=open).pack()






mainloop()