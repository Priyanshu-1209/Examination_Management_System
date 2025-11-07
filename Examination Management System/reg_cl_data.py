from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
import os
from tkinter import messagebox,filedialog


class reg_cl_data:

        def callback(self):
                root.destroy()
                filename = 'admin.py'
                os.system(filename)

        def show_cl(self):
                root.destroy()
                filename = 'show_cl_data.py'
                os.system(filename)

        def show_br(self):
                root.destroy()
                filename = 'show_br_data.py'
                os.system(filename)

        def show_yr(self):
                root.destroy()
                filename = 'show_yr_data.py'
                os.system(filename)
        

        def __init__(self,root):
                self.root=root
                self.root.title("Student Management System")
                self.root.geometry("1500x785+0+0")
                self.root.iconbitmap(r'images/logo.ico')

                title=Label(self.root,text="Add Detail",bd=5,relief=GROOVE,font=("times new roman",40,"bold"),bg="lightblue",fg="red")
                title.pack(side=TOP,fill=X)

                btn_frame=Frame(self.root)
                btn_frame.place(x=10,y=15,width=70)
                btn_frame.config(bg="#e9e4da")
                back=Button(btn_frame,text="Back",width=5,bg="lightblue",font=(10),cursor="hand2",command=self.callback).grid(row=0,column=0)
                # ================= All variables ==========
                
                self.clname_var=StringVar()
                self.year_var=StringVar()
                self.sub_var=StringVar()
                self.branch_var=StringVar()



        # ========= College Add Frame ==================
                mf1=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
                mf1.place(x=50,y=75,width=400,height=180)

                m_title=Label(mf1,text="Add College",bg="wheat",fg="black",font=("times new roman",20,"bold"))
                m_title.grid(row=0,columnspan=2,pady=10)

                lbl_college=Label(mf1,text="College",font=("times new roman",18,"bold"),bg="lightgray")
                lbl_college.grid(row=1,column=0,pady=10,padx=10,sticky="w")

                txt_college=Entry(mf1,textvariable=self.clname_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_college.grid(row=1,column=1,pady=10,padx=10,sticky="w")

                cl_btn_frame=Frame(mf1,bg="lightgray")
                cl_btn_frame.place(x=150,y=120,width=200)


                addbtn=Button(cl_btn_frame,text="Add",width=6,bg="lightgreen",font=(5),command=self.add_cl,cursor="hand2").grid(row=0,column=0)
                showbtn=Button(cl_btn_frame,text="Show All",width=8,bg="lightgreen",font=(5),command=self.show_cl,cursor="hand2").grid(row=0,column=1,padx=10)

                # ============================== Branch Add Frame ============================
                mf2=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
                mf2.place(x=550,y=75,width=400,height=180)

                m_title=Label(mf2,text="Add Branch",bg="wheat",fg="black",font=("times new roman",20,"bold"))
                m_title.grid(row=0,columnspan=2,pady=10)
                lbl_branch=Label(mf2,text="Branch",font=("times new roman",18,"bold"),bg="lightgray")
                lbl_branch.grid(row=1,column=0,pady=10,padx=10,sticky="w")

                txt_branch=Entry(mf2,textvariable=self.branch_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_branch.grid(row=1,column=1,pady=10,padx=10,sticky="w")

                branch_btn_frame=Frame(mf2,bg="lightgray")
                branch_btn_frame.place(x=150,y=120,width=200)


                addbtn=Button(branch_btn_frame,text="Add",width=6,bg="lightgreen",font=(5),command=self.add_branch,cursor="hand2").grid(row=0,column=0)
                showbtn=Button(branch_btn_frame,text="Show All",width=8,bg="lightgreen",font=(5),command=self.show_br,cursor="hand2").grid(row=0,column=1,padx=10)


                # addbtn=Button(mf2,text="Add",width=6,bg="lightgreen",font=(5),command=self.add_branch).grid(row=2,column=1,padx=5)

                # ============================== Year Add Frame ============================
                mf3=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
                mf3.place(x=1050,y=75,width=400,height=180)

                m_title=Label(mf3,text="Add Year",bg="wheat",fg="black",font=("times new roman",20,"bold"))
                m_title.grid(row=0,columnspan=2,pady=10)

                lbl_year=Label(mf3,text="Year",font=("times new roman",18,"bold"),bg="lightgray")
                lbl_year.grid(row=1,column=0,pady=10,padx=10,sticky="w")
                txt_year=Entry(mf3,textvariable=self.year_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_year.grid(row=1,column=1,pady=10,padx=10,sticky="w")

                year_btn_frame=Frame(mf3,bg="lightgray")
                year_btn_frame.place(x=150,y=120,width=200)


                addbtn=Button(year_btn_frame,text="Add",width=6,bg="lightgreen",font=(5),command=self.add_year,cursor="hand2").grid(row=0,column=0)
                showbtn=Button(year_btn_frame,text="Show All",width=8,bg="lightgreen",font=(5),command=self.show_yr,cursor="hand2").grid(row=0,column=1,padx=10)


                # ============================== Paper Add Frame ============================
                mf4=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
                mf4.place(x=50,y=300,width=400,height=180)

                m_title=Label(mf4,text="Add Subjects ",bg="wheat",fg="black",font=("times new roman",20,"bold"))
                m_title.grid(row=0,columnspan=2,pady=10)

                lbl_paper=Label(mf4,text="Subjects",font=("times new roman",18,"bold"),bg="lightgray")
                lbl_paper.grid(row=1,column=0,pady=10,padx=10,sticky="w")

                txt_paper=Entry(mf4,textvariable=self.sub_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_paper.grid(row=1,column=1,pady=10,padx=10,sticky="w")

                paper_btn_frame=Frame(mf4,bg="lightgray")
                paper_btn_frame.place(x=150,y=120,width=200)


                addbtn=Button(paper_btn_frame,text="Add",width=6,bg="lightgreen",font=(5),command=self.add_sub,cursor="hand2").grid(row=0,column=0)
                showbtn=Button(paper_btn_frame,text="Show All",width=8,bg="lightgreen",font=(5),command=self.add_cl,cursor="hand2").grid(row=0,column=1,padx=10)

        
#      ============================== Adding college function =================

        def add_cl(self):
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='college'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Insert student data
                        if self.clname_var.get()=="":
                                messagebox.showerror("Alert", "Enter College Name!")
                        else:
                                cursor.execute("INSERT INTO institutes VALUES(%s)",(self.clname_var.get().strip().upper(),))
                                conn.commit()
                                
                                messagebox.showinfo("Success", "Data inserted successfully!")

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()

#      ============================== Adding Branch function =================

        def add_branch(self):
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='college'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Insert branch data
                        if self.branch_var.get()=="":
                                messagebox.showerror("Alert", "Enter Branch Name!")
                        else:
                                cursor.execute("INSERT INTO branches VALUES(%s)",(self.branch_var.get().strip().upper(),))
                                conn.commit()
                        
                                messagebox.showinfo("Success", "Data inserted successfully!") 
                        

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()

#      ============================== Adding Subjects function =================

        def add_sub(self):
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='college'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Insert paper data
                        if self.sub_var.get()=="":
                                messagebox.showerror("Alert", "Enter Paper Name!")
                        else:
                                cursor.execute("INSERT INTO subject VALUES(%s)",(self.sub_var.get().strip().upper(),))
                                conn.commit()       
                                messagebox.showinfo("Success", "Data inserted successfully!")

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()

#      ============================== Adding Year function =================

        def add_year(self):
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='college'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Insert year data
                        if self.year_var.get()=="":
                                messagebox.showerror("Alert", "Enter Year Name!")
                        else:
                                cursor.execute("INSERT INTO years VALUES(%s)",(self.year_var.get(),))
                                conn.commit()
                                
                                messagebox.showinfo("Success", "Data inserted successfully!")

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()



        



root=Tk()
ob=reg_cl_data(root)

root.mainloop()