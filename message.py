from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn to code")
root.iconbitmap("codemy.ico")


#showinfo, showwarning, showerror, askquestion,askokcancel, askyesno
def popup():
    respons= messagebox.showinfo("This is my Popup!", "Hello World!") 
    Label(root, text=respons).pack()
    #if respons=="yes":
        #Label(root, text="You clicked Yes!").pack()
    #else:
        #Label(root, text="You clicked No!").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()