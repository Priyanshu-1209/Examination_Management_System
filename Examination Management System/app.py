import tkinter as tk
from tkinter import messagebox
import os


def student():
    root.destroy()
    filename = 'st_login.py'
    os.system(filename) #Open file [Same as Right-click Open]
    # os.system('notepad '+filename) #Open in notepad

def admin():
    root.destroy()
    filename = 'ad_login.py'
    os.system(filename)

def teacher():
    root.destroy()
    filename = 'teacher_login.py'
    os.system(filename)

def register():
    root.destroy()
    filename = 'register.py'
    os.system(filename)


# Main window
root = tk.Tk()
root.title("Homepage")
root.geometry("400x350+550+200")
root.resizable(False,False)
root.config(bg="lightgray")
root.iconbitmap(r'images/logo.ico')

# Title label
title_label = tk.Label(root, text="Welcome to the Homepage",bg="lightgray", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

# Buttons for logins
student_button = tk.Button(root, text="Student Login",width=20,bg="#77957E",font=(10),fg="white",cursor="hand2",relief="ridge", command=student)
student_button.pack(pady=10)

admin_button = tk.Button(root, text="Admin Login", width=20,bg="#D9D4F2",font=(10),fg="red",cursor="hand2",relief="ridge", command=admin)
admin_button.pack(pady=10)

teacher_button = tk.Button(root, text="Teacher Login", width=20,bg="#F4E9F0",font=(10),fg="blue",cursor="hand2",relief="ridge", command=teacher)
teacher_button.pack(pady=10)

register_button = tk.Button(root, text="Register Here", width=20,bg="#f3b105",font=(10),fg="#ffefbc",cursor="hand2",relief="ridge", command=register)
register_button.pack(pady=10)

# Run the main loop
root.mainloop()