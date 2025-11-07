import tkinter as tk
from tkinter import messagebox
import mysql.connector
import os

def teacher():
    root.destroy()
    filename = 'teacher.py'
    os.system(filename)

def login_user():
    username = enrollment_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "All fields are mandatory!")
        return

    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this if you have a different MySQL username
            password='',  # Change this if you have a password set for MySQL
            database='teacher_data'
        )
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute("SELECT * FROM teacher WHERE username = %s AND password = %s",
                       (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            teacher()  # Open the new window
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()
        conn.close()



# Create the main window
root = tk.Tk()
root.title("Teacher's Login Page")
root.iconbitmap(r'images/logo.ico')


# Create and place the labels and entries
tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
enrollment_entry = tk.Entry(root)
enrollment_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login_user)
login_button.grid(row=2, columnspan=2, pady=10)

# Start the GUI main loop
root.mainloop()