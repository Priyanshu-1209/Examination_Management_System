import tkinter as tk
from tkinter import messagebox
from tkinter import *

import mysql.connector
from PIL import ImageTk
import os

def callback():
    root.destroy()
    filename = 'app.py'
    os.system(filename)


def student():
    root.destroy()
    filename = 'student.py'
    os.system(filename)

def login_user():
    enrollment_number = enrollment_entry.get()
    password = password_entry.get()

    if not enrollment_number or not password:
        messagebox.showerror("Error", "All fields are mandatory!")
        return

    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this if you have a different MySQL username
            password='',  # Change this if you have a password set for MySQL
            database='st_data'
        )
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute("SELECT * FROM user WHERE enrollment_number = %s AND password = %s",
                       (enrollment_number, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            student()  # Open the new window
        else:
            messagebox.showerror("Error", "Invalid enrollment number or password!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()
        conn.close()



# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("1000x670+200+20")
root.iconbitmap(r'images/logo.ico')

root.resizable(False,False)
background=ImageTk.PhotoImage(file='images/st1.webp')
bg_lbl=Label(root,image=background)
bg_lbl.place(x=0,y=0)
mf=Frame(root,relief=RIDGE,bg="#e9e4da")
mf.place(x=480,y=205,width=500,height=250)

# Create and place the labels and entries
title=Label(root,text="Student Login Here",bd=3,relief=RIDGE,font=("times new roman",30,"bold"),bg="lightblue",fg="red")
title.pack(side=TOP,fill=X)

tk.Label(mf, text="Enrollment Number",font=("times new roman",18,"bold"),bg="#e9e4da").grid(row=0, column=0, padx=10, pady=10)
enrollment_entry = tk.Entry(mf,font=("times new roman",17,"bold"),bd=5,relief=GROOVE,fg='red')
enrollment_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(mf, text="Password",font=("times new roman",18,"bold"),bg="#e9e4da").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(mf, show='*',font=("times new roman",17,"bold"),bd=5,relief=GROOVE,fg='red')
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button

btn_frame=Frame(mf,bg="#e9e4da")
btn_frame.place(x=100,y=130,width=300)

addbtn=Button(btn_frame,text="Back",width=10,bg="lightyellow",font=(10),cursor="hand2",command=callback).grid(row=0,column=0,padx=10)
backbtn=Button(btn_frame,text="Login",width=10,bg="lightblue",font=(10),cursor="hand2",command=login_user).grid(row=0,column=1,padx=10)
# Start the GUI main loop
root.mainloop()