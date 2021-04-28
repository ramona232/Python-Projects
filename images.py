from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Image viewer")
root.iconbitmap("Photo.ico")

my_image = ImageTk.PhotoImage(Image.open("images/Om.jpg"))
my_label = Label(image=my_image)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()




root.mainloop()