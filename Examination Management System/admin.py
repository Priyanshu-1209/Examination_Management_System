import tkinter as tk
from tkinter import messagebox
import os 
from PIL import ImageTk
from tkinter import *

def callback():
    admin_window.destroy()
    filename = 'app.py'
    os.system(filename) #Open file [Same as Right-click Open]
    # os.system('notepad '+filename) #Open in notepad

def reg_cl():
    admin_window.destroy()
    filename = 'reg_cl_data.py'
    os.system(filename) 

def student():
    admin_window.destroy()
    filename = 'student.py'
    os.system(filename) 



admin_window = tk.Tk() 
admin_window.title("Admin Login")
# admin_window.geometry("300x200")
admin_window.geometry("1000x670+200+20")
admin_window.config(bg="#ffefbc")
admin_window.iconbitmap(r'images/logo.ico')

tk.Label(admin_window, text="Welcome to Admin Page", font=("Arial", 14),bg="#ffefbc").pack(pady=20)
# Button(admin_window,text="Click").pack(padx=10)

rg_cl_frame=Frame(admin_window,bg="#e9e4da")
rg_cl_frame.place(x=50,y=80,width=200,height=100)
tk.Label(rg_cl_frame, text="Add College Detail", font=("Arial", 14),bg="#e9e4da").pack(pady=10)
# Button(rg_cl_frame,text="Click").pack(pady=10)

btn_frame=Frame(rg_cl_frame,bg="#e9e4da")
btn_frame.place(y=45,width=250)
btn_frame.config(bg="#e9e4da")
click=Button(btn_frame,text="Click",width=5,bg="lightyellow",font=(10),cursor="hand2",command=reg_cl).grid(row=0,column=0,padx=60)

student_frame=Frame(admin_window,bg="#e9e4da")
student_frame.place(x=270,y=80,width=200,height=100)
tk.Label(student_frame, text="Manage Student Detail", font=("Arial", 14),bg="#e9e4da").pack(pady=10)
# Button(rg_cl_frame,text="Click").pack(pady=10)
btn_frame=Frame(student_frame,bg="#e9e4da")
btn_frame.place(y=45,width=250)
btn_frame.config(bg="#e9e4da")
click=Button(btn_frame,text="Click",width=5,bg="lightyellow",font=(10),cursor="hand2",command=student).grid(row=0,column=0,padx=60)


btn_frame=Frame(admin_window,bg="#e9e4da")
btn_frame.place(y=0,width=65)
btn_frame.config(bg="#e9e4da")
back=Button(btn_frame,text="Back",width=5,bg="lightyellow",font=(10),cursor="hand2",command=callback).grid(row=0,column=0)
# studdent_button.pack(pady=10)
admin_window.mainloop()