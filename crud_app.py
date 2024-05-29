import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Function to connect to the MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your MySQL username
        password="",  # replace with your MySQL password
        database="test01"  # replace with your MySQL database name
    )

# Create the main window
root = Tk()
root.title('Simple CRUD App')
root.geometry('600x600')

# Define functions for CRUD operations
def submit():
    try:
        int(id_entry.get())
        int(zipcode.get())
    except ValueError:
        messagebox.showerror("Error", "ID and Zipcode must be valid integers.")
        return

    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO addresses (id, first_name, last_name, address, city, state, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s)",
              (id_entry.get(), first_name.get(), last_name.get(), address.get(), city.get(), state.get(), zipcode.get()))
    conn.commit()
    conn.close()
    clear_entries()
    messagebox.showinfo("Info", "Record added successfully!")
    query()

def query():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM addresses")
    records = c.fetchall()
    for i in tree.get_children():
        tree.delete(i)
    for record in records:
        tree.insert("", "end", values=record)
    conn.close()

def delete():
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM addresses WHERE id = %s", (delete_box.get(),))
    conn.commit()
    conn.close()
    delete_box.delete(0, END)
    messagebox.showinfo("Info", "Record deleted successfully!")
    query()

def update():
    try:
        int(zipcode_editor.get())
    except ValueError:
        messagebox.showerror("Error", "Zipcode must be a valid integer.")
        return

    conn = connect_db()
    c = conn.cursor()
    c.execute("""UPDATE addresses SET
        first_name = %s,
        last_name = %s,
        address = %s,
        city = %s,
        state = %s,
        zipcode = %s
        WHERE id = %s""",
              (first_name_editor.get(), last_name_editor.get(), address_editor.get(), city_editor.get(), state_editor.get(), zipcode_editor.get(), id_editor.get()))
    conn.commit()
    conn.close()
    editor.destroy()
    messagebox.showinfo("Info", "Record updated successfully!")
    query()

def edit():
    global editor
    editor = Toplevel()
    editor.title('Update A Record')
    editor.geometry('400x300')
    
    global id_editor, first_name_editor, last_name_editor, address_editor, city_editor, state_editor, zipcode_editor

    selected = tree.focus()
    values = tree.item(selected, 'values')

    id_editor = Entry(editor, state='readonly')
    id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    id_editor.insert(0, values[0])

    first_name_editor = Entry(editor)
    first_name_editor.grid(row=1, column=1)
    first_name_editor.insert(0, values[1])

    last_name_editor = Entry(editor)
    last_name_editor.grid(row=2, column=1)
    last_name_editor.insert(0, values[2])

    address_editor = Entry(editor)
    address_editor.grid(row=3, column=1)
    address_editor.insert(0, values[3])

    city_editor = Entry(editor)
    city_editor.grid(row=4, column=1)
    city_editor.insert(0, values[4])

    state_editor = Entry(editor)
    state_editor.grid(row=5, column=1)
    state_editor.insert(0, values[5])

    zipcode_editor = Entry(editor)
    zipcode_editor.grid(row=6, column=1)
    zipcode_editor.insert(0, values[6])

    id_editor_label = Label(editor, text="ID")
    id_editor_label.grid(row=0, column=0, pady=(10, 0))
    first_name_editor_label = Label(editor, text="First Name")
    first_name_editor_label.grid(row=1, column=0)
    last_name_editor_label = Label(editor, text="Last Name")
    last_name_editor_label.grid(row=2, column=0)
    address_editor_label = Label(editor, text="Address")
    address_editor_label.grid(row=3, column=0)
    city_editor_label = Label(editor, text="City")
    city_editor_label.grid(row=4, column=0)
    state_editor_label = Label(editor, text="State")
    state_editor_label.grid(row=5, column=0)
    zipcode_editor_label = Label(editor, text="Zipcode")
    zipcode_editor_label.grid(row=6, column=0)

    save_button = Button(editor, text="Save Record", command=update)
    save_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

def clear_entries():
    id_entry.delete(0, END)
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create entry boxes
id_entry = Entry(root, width=30)
id_entry.grid(row=0, column=1, padx=20, pady=(10, 0))
first_name = Entry(root, width=30)
first_name.grid(row=1, column=1)
last_name = Entry(root, width=30)
last_name.grid(row=2, column=1)
address = Entry(root, width=30)
address.grid(row=3, column=1)
city = Entry(root, width=30)
city.grid(row=4, column=1)
state = Entry(root, width=30)
state.grid(row=5, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=6, column=1)

# Create entry box labels
id_label = Label(root, text="ID")
id_label.grid(row=0, column=0, pady=(10, 0))
first_name_label = Label(root, text="First Name")
first_name_label.grid(row=1, column=0)
last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=2, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=3, column=0)
city_label = Label(root, text="City")
city_label.grid(row=4, column=0)
state_label = Label(root, text="State")
state_label.grid(row=5, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=6, column=0)

# Create Submit Button
submit_button = Button(root, text="Add Record To Database", command=submit)
submit_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_label = Label(root, text="Select ID")
delete_label.grid(row=9, column=0)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
update_label = Label(root, text="Select ID")
update_label.grid(row=11, column=0)
update_box = Entry(root, width=30)
update_box.grid(row=11, column=1)
update_button = Button(root, text="Edit Record", command=edit)
update_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# Create a Treeview to display query results
columns = ('id', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode')
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.grid(row=13, column=0, columnspan=2, pady=10, padx=10)

# Run the main loop
root.mainloop()
