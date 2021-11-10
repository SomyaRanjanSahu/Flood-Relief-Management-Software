from tkinter import *
# from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Current Status')
root.geometry("400x500")

#Database

# Create a database or connect to one
conn = sqlite3.connect('record_book.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE record (
          state text,
          relief_centers integer,
          deaths integer,
          donation integer
        )""")
'''

# Create function to delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('record_book.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM record WHERE oid=" + delete_box.get())

    # commit changes
    conn.commit()
    # close connection
    conn.close()

# Create submit fucntion for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('record_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO record VALUES (:state, :r_center, :deaths, :donation)",
            {
                'state': state.get(),
                'r_center': r_center.get(),
                'deaths': deaths.get(),
                'donation': donation.get()
            })

    # commit changes
    conn.commit()
    # close connection
    conn.close()

    # Clear the text boxes
    state.delete(0, END)
    r_center.delete(0, END)
    deaths.delete(0, END)
    donation.delete(0, END)

# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('record_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM record ")
    records = c.fetchall()
    #print(records)

    # Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2]) + "\t" + str(record[3]) + "\t" + str(record[4]) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)

    # commit changes
    conn.commit()
    # close connection
    conn.close()

Label(root, text="Current Status", font="comicsansms 18 bold", justify=CENTER, pady=15, padx=20).grid(row=0, column=1)

# Create Text Boxes
state = Entry(root, width=30)
state.grid(row=1, column=1, padx=10, pady=(20,0))
r_center = Entry(root, width=30)
r_center.grid(row=2, column=1, pady=(10,0))
deaths = Entry(root, width=30)
deaths.grid(row=3, column=1, pady=(10,0))
donation = Entry(root, width=30)
donation.grid(row=4, column=1, pady=(10,0))

delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1)

# Create Text Box labels
state_label = Label(root, text="State")
state_label.grid(row=1, column=0, pady=(20,0))
r_center_label = Label(root, text="Relief Centers")
r_center_label.grid(row=2, column=0, pady=(10,0))
deaths_label = Label(root, text="Deaths")
deaths_label.grid(row=3, column=0, pady=(10,0))
donation_label = Label(root, text="Total Donation")
donation_label.grid(row=4, column=0, pady=(10,0))

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=8, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", fg="#ffffff", bg="#3F3351", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=20, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", fg="#ffffff", bg="#3F3351", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=126)

# Create a delete button
delete_btn = Button(root, text="Delete Record", fg="#ffffff", bg="#3F3351", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=126)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()