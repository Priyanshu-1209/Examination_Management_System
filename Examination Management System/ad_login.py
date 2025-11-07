import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk
from tkinter import *
import os

def callback():
    root.destroy()
    filename = 'app.py'
    os.system(filename)

def admin():
    root.destroy()
    filename = 'admin.py'
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
            database='ad_data'
        )
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s",
                       (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            admin()  # Open the new window
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()
        conn.close()



# Create the main window
root = tk.Tk()
root.title("Admin Login Page")
root.geometry("500x300+500+200")
root.resizable(False,False)
root.iconbitmap(r'images/logo.ico')

background=ImageTk.PhotoImage(file='images/admin.jpg')
bg_lbl=Label(root,image=background)
bg_lbl.place(x=0,y=0)
# Create and place the labels and entries
tk.Label(root, text="Username",font=("Arial",18,"bold"),bg="#011226",padx=10,fg="#E99157").grid(row=0, column=0, padx=10, pady=10)
enrollment_entry = tk.Entry(root,font=("times new roman",17,"bold"),bd=5,relief=RIDGE,fg='blue')
enrollment_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password",font=("Arial",18,"bold"),bg="#011226",padx=10,fg="#E99157").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show='#',font=("times new roman",17,"bold"),bd=5,relief=RIDGE,fg='blue')
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button

btn_frame=Frame(root,bg="#011226")
btn_frame.place(x=10,y=120,width=400)

addbtn=Button(btn_frame,text="Login",width=10,bg="lightgreen",font=(10),cursor="hand2",command=login_user).grid(row=0,column=0,padx=10)
backbtn=Button(btn_frame,text="Back",width=10,bg="lightyellow",font=(10),cursor="hand2",command=callback).grid(row=0,column=1,padx=10)


# Start the GUI main loop
root.mainloop()