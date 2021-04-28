from tkinter import*

root = Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.configure(bg="black")

e = Entry(root, width=35, borderwidth=5, bg="white")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
 

def button_click(number):
    curret = e.get()
    e.delete(0, END)
    e.insert(0, str(curret) + str(number))

def button_C():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math= "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, f_num + int(second_number ))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number ))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number ))
    if math == "division":
        e.insert(0, f_num / int(second_number ))
    
        

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math= "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math= "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math= "division"
    f_num = int(first_number)
    e.delete(0, END)
    



#Define Buttons

button_1 = Button(root, text="1", foreground=("white"), padx=40, pady=20, command=lambda: button_click(1), bg="black")
button_2 = Button(root, text="2", foreground=("white"), padx=40, pady=20, command=lambda: button_click(2), bg="black")
button_3 = Button(root, text="3", foreground=("white"), padx=40, pady=20, command=lambda: button_click(3), bg="black")
button_4 = Button(root, text="4", foreground=("white"), padx=40, pady=20, command=lambda: button_click(4), bg="black")
button_5 = Button(root, text="5",foreground=("white"), padx=40, pady=20, command=lambda: button_click(5), bg="black")
button_6 = Button(root, text="6",foreground=("white"), padx=40, pady=20, command=lambda: button_click(6), bg="black")
button_7 = Button(root, text="7",foreground=("white"), padx=40, pady=20, command=lambda: button_click(7), bg="black")
button_8 = Button(root, text="8",foreground=("white"), padx=40, pady=20, command=lambda: button_click(8), bg="black")
button_9 = Button(root, text="9",foreground=("white"), padx=40, pady=20, command=lambda: button_click(9), bg="black")
button_0 = Button(root, text="0",foreground=("white"), padx=40, pady=20, command=lambda: button_click(0), bg="black")
button_add = Button(root, text="+", foreground=("white"), padx=39, pady=20, command=button_add, bg="grey")
button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal, bg="darkorange")
button_C = Button(root, text="C", foreground=("white"), padx=88, pady=20, command=button_C, bg="darkred")

button_subtract = Button(root, text="-", foreground=("white"), padx=41, pady=20, command=button_subtract, bg="grey")
button_multiply = Button(root, text="*", foreground=("white"), padx=41, pady=20, command=button_multiply, bg="grey")
button_divide = Button(root, text="/", foreground=("white"), padx=41, pady=20, command=button_divide, bg="grey")


#Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4,column=0)
button_C.grid(row=4,column=1, columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()





