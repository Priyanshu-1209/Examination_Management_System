import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os


class register:

        def callback(self):
                root.destroy()
                filename = 'app.py'
                os.system(filename)

        # def show(self):
        #         root.destroy()
        #         filename = 'show_cl_data.py'
        #         os.system(filename)
        

        def __init__(self,root):
                self.root=root
                self.root.title("Student Management System")
                self.root.geometry("500x500+500+100")
                self.root.iconbitmap(r'images/logo.ico')
                
                # ================= All variables ==========
                
                self.user_var=StringVar()
                self.pass_var=StringVar()

                # ========= Manage Frame ==================
                mf=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
                mf.place(x=20,y=75,width=450,height=300)

                m_title=Label(mf,text="Register Here",bg="wheat",fg="black",font=("times new roman",20,"bold"))
                m_title.grid(row=0,columnspan=2,pady=10)
                
                lbl_username=Label(mf,text="Username",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_username.grid(row=1,column=0,pady=10,padx=10,sticky="w")

                txt_user=Entry(mf,textvariable=self.user_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_user.grid(row=1,column=1,pady=10,padx=10,sticky="w")                

                lbl_pass=Label(mf,text="Password",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_pass.grid(row=2,column=0,pady=10,padx=10,sticky="w")

                txt_pass=Entry(mf,textvariable=self.pass_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_pass.grid(row=2,column=1,pady=10,padx=10,sticky="w")                
               
               # ==================== Button Frame =========================

                btn_frame=Frame(mf,bg="lightgray")
                btn_frame.place(x=40,y=200,width=365)

              
                adminbtn=Button(btn_frame,text="Admin",width=6,bg="lightyellow",font=(5),command=self.admin).grid(row=0,column=0,padx=5)
                teacherbtn=Button(btn_frame,text="Teacher",width=6,bg="wheat",font=(5),command=self.teacher_data).grid(row=0,column=1,padx=5)
                studentbtn=Button(btn_frame,text="Student",width=6,bg="lightblue",font=(5),command=self.student ).grid(row=0,column=2,padx=5)
                backbtn=Button(btn_frame,text="Back",width=6,bg="lightgreen",font=(5),command=self.callback).grid(row=0,column=3,padx=5)

        #      ============================== Adding Admin =================
        def clear(self):
                self.user_var.set("")
                self.pass_var.set("")

        def admin(self):
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='ad_data'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Insert student data
                        if self.user_var.get()=="" or self.pass_var.get()=="":
                                messagebox.showerror("Alert", "Enter Detail....!")
                        else:
                                cursor.execute("INSERT INTO admin VALUES(%s,%s)",(self.user_var.get().strip().lower(),self.pass_var.get(),))
                                conn.commit()
                                
                                messagebox.showinfo("Success", "Admin Added Successfully!")

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()
                        self.clear()

        def teacher(self):
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='teacher_data'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Insert student data
                        if self.user_var.get()=="" or self.pass_var.get()=="":
                                messagebox.showerror("Alert", "Enter Detail....!")
                        else:
                                cursor.execute("INSERT INTO teacher VALUES(%s,%s)",(self.user_var.get().strip().lower(),self.pass_var.get(),))
                                conn.commit()
                                
                                messagebox.showinfo("Success", "Teacher Added Successfully!")

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()
                        self.clear()

        def student(self):
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='st_data'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Insert student data
                        if self.user_var.get()=="" or self.pass_var.get()=="":
                                messagebox.showerror("Alert", "Enter Detail....!")
                        else:
                                cursor.execute("INSERT INTO user VALUES(%s,%s)",(self.user_var.get().strip().lower(),self.pass_var.get(),))
                                conn.commit()
                                
                                messagebox.showinfo("Success", "Student Added Successfully!")

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()
                        self.clear()

        def teacher_data(self):
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='teacher_data'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Insert student data
                        if self.user_var.get()=="" or self.pass_var.get()=="":
                                messagebox.showerror("Alert", "Enter Detail....!")
                        else:
                                cursor.execute("INSERT INTO teacher VALUES(%s,%s)",(self.user_var.get().strip().lower(),self.pass_var.get(),))
                                conn.commit()
                                
                                messagebox.showinfo("Success", "Teacher Added Successfully!")

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()
                        self.clear()

# Create the main window




root=Tk()
ob=register(root)

root.mainloop()