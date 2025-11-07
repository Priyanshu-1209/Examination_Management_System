import tkinter as tk
from tkinter import messagebox
import os 

def callback():
    teacher_window.destroy()
    filename = 'app.py'
    os.system(filename) #Open file [Same as Right-click Open]
    # os.system('notepad '+filename) #Open in notepad

# teacher_window = tk.Toplevel()



teacher_window = tk.Tk() 
teacher_window.title("Teacher Login")
teacher_window.geometry("300x200")
teacher_window.iconbitmap(r'images/logo.ico')
tk.Label(teacher_window, text="Welcome to Teacher Login", font=("Arial", 14)).pack(pady=20)
tk.Button(teacher_window, text="Close", command=teacher_window.destroy).pack(pady=10)
tk.Button(teacher_window, text="Back", command=callback).pack(pady=10)

# studdent_button.pack(pady=10)
teacher_window.mainloop()