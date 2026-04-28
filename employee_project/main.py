from tkinter import *
from tkinter import messagebox
import database

database.create_table()

selected_item = None

def get_selected(event):
    global selected_item
    try:
        index = listbox.curselection()[0]
        selected_item = listbox.get(index)

        entry_name.delete(0, END)
        entry_name.insert(END, selected_item[1])

        entry_age.delete(0, END)
        entry_age.insert(END, selected_item[2])

        entry_dept.delete(0, END)
        entry_dept.insert(END, selected_item[3])

        entry_salary.delete(0, END)
        entry_salary.insert(END, selected_item[4])
    except:
        pass

def view_command():
    listbox.delete(0, END)
    for row in database.fetch():
        listbox.insert(END, row)

def add_command():
    if entry_name.get() == "":
        messagebox.showerror("Error", "Name is required")
        return

    database.insert(
        entry_name.get(),
        entry_age.get(),
        entry_dept.get(),
        entry_salary.get()
    )
    view_command()

def update_command():
    if selected_item:
        database.update(
            selected_item[0],
            entry_name.get(),
            entry_age.get(),
            entry_dept.get(),
            entry_salary.get()
        )
        view_command()

def delete_command():
    if selected_item:
        database.delete(selected_item[0])
        view_command()

def search_command():
    listbox.delete(0, END)
    for row in database.search(entry_name.get()):
        listbox.insert(END, row)

window = Tk()
window.title("Employee Management System")
window.geometry("600x400")

Label(window, text="Name").grid(row=0, column=0)
Label(window, text="Age").grid(row=0, column=2)
Label(window, text="Department").grid(row=1, column=0)
Label(window, text="Salary").grid(row=1, column=2)

entry_name = Entry(window)
entry_name.grid(row=0, column=1)

entry_age = Entry(window)
entry_age.grid(row=0, column=3)

entry_dept = Entry(window)
entry_dept.grid(row=1, column=1)

entry_salary = Entry(window)
entry_salary.grid(row=1, column=3)

listbox = Listbox(window, height=10, width=50)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

listbox.bind('<<ListboxSelect>>', get_selected)

Button(window, text="View All", width=12, command=view_command).grid(row=2, column=3)
Button(window, text="Search", width=12, command=search_command).grid(row=3, column=3)
Button(window, text="Add", width=12, command=add_command).grid(row=4, column=3)
Button(window, text="Update", width=12, command=update_command).grid(row=5, column=3)
Button(window, text="Delete", width=12, command=delete_command).grid(row=6, column=3)
Button(window, text="Close", width=12, command=window.quit).grid(row=7, column=3)

window.mainloop()
