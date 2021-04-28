from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code")
root.iconbitmap("codemy.ico")

my_image1 = ImageTk.PhotoImage(Image.open("images/Om.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("images/img1.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("images/img2.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("images/img3.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("images/img4.jpg"))

image_list = [my_image1, my_image2, my_image3, my_image4, my_image5]

my_label = Label(image=my_image1)
my_label.grid(row=0,column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label =Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)




def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label =Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)




button_back = Button(root, text="<<", command= back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command= lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1,column=2)





root.mainloop()