import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import mysql.connector as mysql

# im going to create simple inventory management system using tkinter and mysql

def conDB():
    conn = mysql.connect(host='localhost', user='root', password='', database='inventory')
    cursor = conn.cursor()
    return conn, cursor

def main():
    def addStudent():
        # create new window for adding student and hide main window using withdraw() insert to table
        def add():
            con, cur = conDB()
            cur.execute('INSERT INTO tblstudents VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s)', (ent_name.get(), ent_sex.get(), ent_contact.get(), ent_quantity.get(), ent_price.get(), combo_year.get(), combo_section.get(), combo_size.get()))
            con.commit()
            mb.showinfo('Success', 'Student added successfully')
            con.close()
            addWindow.destroy()
            root.deiconify()

        def cancel():
            addWindow.destroy()
            root.deiconify()

        root.withdraw()
        addWindow = tk.Toplevel()
        addWindow.title('Add Student')
        addWindow.geometry('400x700')
        addWindow.resizable(False, False)

        # create label and entry and center them
        lbl_name = ttk.Label(addWindow, text='Name: ')
        lbl_name.place(x=50, y=50)
        ent_name = ttk.Entry(addWindow, width=30)
        ent_name.place(x=150, y=50)
        lbl_sex = ttk.Label(addWindow, text='Sex: ')
        lbl_sex.place(x=50, y=100)
        ent_sex = ttk.Entry(addWindow, width=30)
        ent_sex.place(x=150, y=100)
        lbl_contact = ttk.Label(addWindow, text='Contact No: ')
        lbl_contact.place(x=50, y=150)
        ent_contact = ttk.Entry(addWindow, width=30)
        ent_contact.place(x=150, y=150)
        lbl_quantity = ttk.Label(addWindow, text='Quantity: ')
        lbl_quantity.place(x=50, y=200)
        ent_quantity = ttk.Entry(addWindow, width=30)
        ent_quantity.place(x=150, y=200)
        lbl_price = ttk.Label(addWindow, text='Price: ')
        lbl_price.place(x=50, y=250)
        ent_price = ttk.Entry(addWindow, width=30)
        ent_price.place(x=150, y=250)
        lbl_year = ttk.Label(addWindow, text='Year: ')
        lbl_year.place(x=50, y=300)
        combo_year = ttk.Combobox(addWindow, width=27, state='readonly')
        combo_year['values'] = ('1st Year', '2nd Year', '3rd Year', '4th Year')
        combo_year.current(0)
        combo_year.place(x=150, y=300)
        lbl_section = ttk.Label(addWindow, text='Section: ')
        lbl_section.place(x=50, y=350)
        combo_section = ttk.Combobox(addWindow, width=27, state='readonly')
        combo_section['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N')
        combo_section.current(0)
        combo_section.place(x=150, y=350)
        lbl_size = ttk.Label(addWindow, text='Size: ')
        lbl_size.place(x=50, y=400)
        combo_size = ttk.Combobox(addWindow, width=27, state='readonly')
        combo_size['values'] = ('Extra Small', 'Small', 'Medium', 'Large', 'Extra Large', 'XXL', 'XXXL')
        combo_size.current(0)
        combo_size.place(x=150, y=400)

        # create button and center them
        btn_add = ttk.Button(addWindow, text='Add', command=add)
        btn_add.place(x=150, y=450)
        btn_cancel = ttk.Button(addWindow, text='Cancel', command=cancel)
        btn_cancel.place(x=250, y=450)

        addWindow.mainloop()

    def editStudent():
        # get the selected row on treeview and get values
        selected = tree.selection()[0]
        values = tree.item(selected, 'values')
        # get the values from entry and combobox and update to table
        def edit():
            con, cur = conDB()
            edit = ('''
                UPDATE tblstudents SET name = %s, sex = %s, contactno = %s, quantity = %s, price = %s, yearid = %s, sectionid = %s, sizeid = %s WHERE studentid = %s
            ''')
            # data to be updated to table and get the id of selected row
            data = (ent_name.get(), ent_sex.get(), ent_contact.get(), ent_quantity.get(), ent_price.get(), combo_year.get(), combo_section.get(), combo_size.get(), values[0])
            cur.execute(edit, data)
            con.commit()
            mb.showinfo('Success', 'Student updated successfully')
            con.close()
            editWindow.destroy()
            root.deiconify()
            refresh()
        def cancel():
            editWindow.destroy()
            root.deiconify()

        root.withdraw()
        editWindow = tk.Toplevel()
        editWindow.title('Edit Student')
        editWindow.geometry('400x700')
        editWindow.resizable(False, False)

        # create label and entry enter values from selected row and center them
        lbl_name = ttk.Label(editWindow, text='Name: ')
        lbl_name.place(x=50, y=50)
        ent_name = ttk.Entry(editWindow, width=30)
        ent_name.insert(0, values[1])
        ent_name.place(x=150, y=50)
        lbl_sex = ttk.Label(editWindow, text='Sex: ')
        lbl_sex.place(x=50, y=100)
        ent_sex = ttk.Entry(editWindow, width=30)
        ent_sex.place(x=150, y=100)
        ent_sex.insert(0, values[2])
        lbl_contact = ttk.Label(editWindow, text='Contact No: ')
        lbl_contact.place(x=50, y=150)
        ent_contact = ttk.Entry(editWindow, width=30)
        ent_contact.insert(0, values[3])
        ent_contact.place(x=150, y=150)
        lbl_quantity = ttk.Label(editWindow, text='Quantity: ')
        lbl_quantity.place(x=50, y=200)
        ent_quantity = ttk.Entry(editWindow, width=30)
        ent_quantity.insert(0, values[4])
        ent_quantity.place(x=150, y=200)
        lbl_price = ttk.Label(editWindow, text='Price: ')
        lbl_price.place(x=50, y=250)
        ent_price = ttk.Entry(editWindow, width=30)
        ent_price.insert(0, values[5])
        ent_price.place(x=150, y=250)
        lbl_year = ttk.Label(editWindow, text='Year: ')
        lbl_year.place(x=50, y=300)
        combo_year = ttk.Combobox(editWindow, width=27, state='readonly')
        combo_year['values'] = ('1st Year', '2nd Year', '3rd Year', '4th Year')
        # get the selected value from combobox and set it to the selected row value
        combo_year.current(combo_year['values'].index(values[6]))
        combo_year.place(x=150, y=300)
        lbl_section = ttk.Label(editWindow, text='Section: ')
        lbl_section.place(x=50, y=350)
        combo_section = ttk.Combobox(editWindow, width=27, state='readonly')
        combo_section['values'] = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N')
        combo_section.current(combo_section['values'].index(values[7]))
        combo_section.place(x=150, y=350)
        lbl_size = ttk.Label(editWindow, text='Size: ')
        lbl_size.place(x=50, y=400)
        combo_size = ttk.Combobox(editWindow, width=27, state='readonly')
        combo_size['values'] = ('Extra Small', 'Small', 'Medium', 'Large', 'Extra Large', 'XXL', 'XXXL')
        combo_size.current(combo_size['values'].index(values[8]))
        combo_size.place(x=150, y=400)

        # create button and center them
        btn_edit = ttk.Button(editWindow, text='Edit', command=edit)
        btn_edit.place(x=150, y=450)
        btn_cancel = ttk.Button(editWindow, text='Cancel', command=cancel)
        btn_cancel.place(x=250, y=450)

        editWindow.mainloop()

    def refresh():
        # refresh treeview
        con, cur = conDB()
        cur.execute('SELECT * FROM tblstudents')
        rows = cur.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert('', tk.END, values=row)
        con.close()

    # create new winodw ask if user the id of the student to be deleted
    def deleteStudent():
        selected = tree.selection()[0]
        values = tree.item(selected, 'values')
        def delete():
            con, cur = conDB()
            delete = ('''
                DELETE FROM tblstudents WHERE studentid = %s
            ''')
            data = (values[0],)
            cur.execute(delete, data)
            con.commit()
            mb.showinfo('Success', 'Student deleted successfully')
            con.close()
            deleteWindow.destroy()
            root.deiconify()
            refresh()
        def cancel():
            deleteWindow.destroy()
            root.deiconify()

        root.withdraw()
        deleteWindow = tk.Toplevel()
        deleteWindow.title('Delete Student')
        deleteWindow.geometry('400x200')
        deleteWindow.resizable(False, False)

        lbl_delete = ttk.Label(deleteWindow, text='Are you sure you want to delete this student?')
        lbl_delete.place(x=50, y=50)
        btn_delete = ttk.Button(deleteWindow, text='Delete', command=delete)
        btn_delete.place(x=150, y=100)
        btn_cancel = ttk.Button(deleteWindow, text='Cancel', command=cancel)
        btn_cancel.place(x=250, y=100)

        deleteWindow.mainloop()



    createTable_tblstudents()
    root = tk.Tk()
    root.title('Inventory Management System')
    root.state('zoomed')
    root.resizable(False, False)

    # create menubar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # create submenu for menubar add, edit, delete, logout
    submenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Product', menu=submenu)
    submenu.add_command(label='Add', command=addStudent)
    submenu.add_command(label='Edit', command=editStudent)
    submenu.add_command(label='Delete', command=deleteStudent)
    submenu.add_separator()
    submenu.add_command(label='Logout', command=root.destroy)

    # get data from database and display as treeview on center
    con, cur = conDB()
    cur.execute('SELECT * FROM tblstudents')
    rows = cur.fetchall()

    # create treeview
    tree = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show='headings', height='10')
    tree.pack(pady=20)

    # create scrollbar
    scroll = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    scroll.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scroll.set)

    # create treeview columns and center them and set width to 100
    tree.heading(1, text='ID')
    tree.column(1, anchor='center', width=100)
    tree.heading(2, text='Name')
    tree.column(2, anchor='center', width=100)
    tree.heading
    tree.heading(3, text='Sex')
    tree.column(3, anchor='center', width=100)
    tree.heading(4, text='Contact No')
    tree.column(4, anchor='center', width=100)
    tree.heading(5, text='Quantity')
    tree.column(5, anchor='center', width=100)
    tree.heading(6, text='Price')
    tree.column(6, anchor='center', width=100)
    tree.heading(7, text='Year')
    tree.column(7, anchor='center', width=100)
    tree.heading(8, text='Section')
    tree.column(8, anchor='center', width=100)
    tree.heading(9, text='Size')
    tree.column(9, anchor='center', width=100)

    # insert data to treeview
    for row in rows:
        tree.insert('', 'end', values=row)

    # create refresh button
    btn_refresh = tk.Button(root, text='Refresh', command=refresh)
    btn_refresh.pack(pady=10)


    root.mainloop()

def createtable_tblusers():
    con, cur = conDB()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tblusers(
            userid INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL)
    ''')
    con.commit()
    mb.showinfo('Success', 'Table created successfully')
    con.close()

# verify login credentials connect database
def verifyLogin():
    con, cur = conDB()
    cur.execute('SELECT * FROM tblusers WHERE username = %s AND password = %s', (ent_username.get(), ent_password.get()))
    if cur.fetchone() is not None:
        mb.showinfo('Success', 'Login successful')
        root.destroy()
        main()
    else:
        mb.showerror('Error', 'Invalid username or password')
    con.close()

def createadminacc():
    con, cur = conDB()
    cur.execute('INSERT INTO tblusers VALUES(NULL, %s, %s)', ("admin", "admin"))
    con.commit()
    mb.showinfo('Success', 'Admin account created')
    con.close()

# create table
def createTable_tblstudents():
    con, cur = conDB()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS tblstudents(
        studentid INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        sex VARCHAR(10) NOT NULL,
        contactno VARCHAR(20) NOT NULL,
        quantity VARCHAR(20) NOT NULL,
        price VARCHAR(20) NOT NULL,
        yearid VARCHAR(20) NOT NULL,
        sectionid VARCHAR(20) NOT NULL,
        sizeid VARCHAR(20) NOT NULL);
    ''')
    con.commit()
    mb.showinfo('Success', 'Table created successfully')
    con.close()

# create main window
root = tk.Tk()
root.title('Login Interface')
root.geometry('800x600')
root.resizable(False, False)

# create interface for login form center it on the screen
frm_login = ttk.Frame(root, padding=10)
frm_login.place(relx=0.5, rely=0.5, anchor='center')

# create label and entry for username
lbl_username = ttk.Label(frm_login, text='Username')
lbl_username.grid(row=0, column=0, padx=5, pady=5, sticky='e')
ent_username = ttk.Entry(frm_login, width=30)
ent_username.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# create label and entry for password
lbl_password = ttk.Label(frm_login, text='Password')
lbl_password.grid(row=1, column=0, padx=5, pady=5, sticky='e')
ent_password = ttk.Entry(frm_login, width=30, show='*')
ent_password.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# create button for login
btn_login = ttk.Button(frm_login, text='Login', command=verifyLogin)
btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

