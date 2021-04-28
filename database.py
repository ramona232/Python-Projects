from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Address Book')
root.iconbitmap('Database.ico')
root.geometry("320x500")
root.configure(bg="lightblue")

#Database
#Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#Create a cursor
c = conn.cursor()

#Create Table
'''
c.execute(""" CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""") 
'''

#Create Submit Function
def submit():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()
    #Insert into table
    c.execute('INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)',
            {
              "f_name": f_name.get(),
              "l_name": l_name.get(),
              "address": address.get(),
              "city": city.get(),
              "state": state.get(),
              "zipcode": zipcode.get()  
            })
    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()

    #Clear the Text Boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)


#Create Query Function
def query():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()

    #Query th Database
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    print(records)

    #Loop thru results
    print_records = ""
    for record in records:
        print_records += str(record[0]) +"  "+ str(record[1]) +"  "+ str(record[2]) +"  "+ str(record[3]) +"  "+ str(record[4]) +"  "+ str(record[5]) +"  "+"\t" +str(record[6]) + "\n"

    query_label = Label(root, text=print_records, bg="lightblue")
    query_label.grid(row=12, column=0, columnspan=2 )

    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()


#Create Delete Record Function
def delete():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()

    #Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())
    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()

#Create Save function    
def save():
    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()
   
    record_id = delete_box.get()
    c.execute(""" UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {'first': f_name_editor.get(),
         'last' : l_name_editor.get(),
         'address': address_editor.get(),
         'city' : city_editor.get(),
         'zipcode' : zipcode_editor.get(),
         'oid': record_id
        })
    #Commit Changes
    conn.commit()
    #Close Connection
    conn.close()   

#Create Edit Function
def edit():
    editor = Tk()
    editor.title(' Edit Record ')
    editor.iconbitmap('Database.ico')
    editor.geometry("320x500")
    editor.configure(bg="lightblue")

    #Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create a cursor
    c = conn.cursor()
    #Query th Database
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = c.fetchall()

    #Create Global Variable for text box name
    global  f_name_editor
    global  l_name_editor
    global  address_editor
    global  city_editor
    global  state_editor
    global  zipcode_editor
    
    #Create Text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=30, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    #Create  TextBox Labels
    f_name_label = Label(editor, text="First Name", bg="lightblue")
    f_name_label.grid(row=0, column=0, pady=(10, 0),padx=10)
    l_name_label = Label(editor, text="Last Name", bg="lightblue")
    l_name_label.grid(row=1, column=0 )
    address_label = Label(editor, text="Address", bg="lightblue")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City", bg="lightblue")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State", bg="lightblue")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode", bg="lightblue")
    zipcode_label.grid(row=5, column=0)

     #Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    #Create a Save Button to save edited record
    save_btn = Button(editor, text="Save Record", command=save, bg="darkgreen", fg='white')
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=105)

   
#Create Text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1,pady=5 )

#Create  TextBox Labels
f_name_label = Label(root, text="First Name", bg="lightblue")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name", bg="lightblue")
l_name_label.grid(row=1, column=0 )
address_label = Label(root, text="Address", bg="lightblue")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City", bg="lightblue")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State", bg="lightblue")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode", bg="lightblue")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID",bg="lightblue" )
delete_box_label.grid(row=9, column=0, pady=5)

#Create Submit Buttons
submit_btn = Button(root, text='Add Record to DataBase', command=submit, bg="darkgreen", fg='white')
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=80)

#Create a Query Button
query_btn = Button(root, text="Show Records", command=query, bg="orange")
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=107)

#Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete, bg="red", fg='white')
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=107)

#Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit, bg="royalblue4", fg='white')
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=114)




#Commit Changes
conn.commit()

#Close Connection
conn.close()


root.mainloop()
