from tkinter import *
from tkinter import ttk
from tkinter import messagebox,filedialog
import pymysql
import os 


class student:
        
        def callback(self):
                root.destroy()
                filename = 'reg_cl_data.py'
                os.system(filename) #Open file [Same as Right-click Open]

        def __init__(self,root):
                self.root=root
                self.root.title("Manage College Detail")
                self.root.geometry("1500x785+0+0")
                self.root.iconbitmap(r'images/logo.ico')


                title=Label(self.root,text="Manage College Detail",bd=5,relief=GROOVE,font=("times new roman",40,"bold"),bg="lightblue",fg="red")
                title.pack(side=TOP,fill=X)

                self.cl_var=StringVar()

                # ========= Manage Frame ==================
                mf=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
                mf.place(x=20,y=75,width=480,height=200)

                m_title=Label(mf,text="Manage Data",bg="wheat",fg="black",font=("times new roman",20,"bold"))
                m_title.grid(row=0,columnspan=2,pady=10)
                lbl_college=Label(mf,text="College",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_college.grid(row=1,column=0,pady=10,padx=10,sticky="w")

                txt_college=Entry(mf,textvariable=self.cl_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_college.grid(row=1,column=1,pady=10,padx=10,sticky="w")

                # ==================== Button Frame =========================

                btn_frame=Frame(mf,bg="lightgray")
                btn_frame.place(x=12,y=120,width=260)

              
                # updatebtn=Button(btn_frame,text="Update",width=6,bg="lightyellow",font=(5)).grid(row=0,column=0,padx=5)
                deletebtn=Button(btn_frame,text="Delete",width=6,bg="red",font=(5),command=self.delete_data).grid(row=0,column=1,padx=5)
                backbtn=Button(btn_frame,text="Back",width=6,bg="lightblue",font=(5) ,command=self.callback).grid(row=0,column=2,padx=5)

                # ===================================================================
                df=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
                df.place(x=520,y=75,width=950,height=700)
                



        # ======================== Table Frame =============

                tf=Frame(df,bd=4,relief=RIDGE,bg="lightgray")
                tf.place(x=5,width=935,height=685)

                scroll_x=Scrollbar(tf,orient=HORIZONTAL)
                scroll_y=Scrollbar(tf,orient=VERTICAL)

                self.college_table=ttk.Treeview(tf,columns=("clname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.college_table.xview)

                self.college_table.heading("clname",text="College Name")
                self.college_table['show']='headings'
                self.college_table.column("clname",width=200)
                self.college_table.pack(fill=BOTH,expand=1)
                self.college_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()

        def fetch_data(self):
                try:
                        conn=pymysql.connect(host="localhost",user="root",password="",database="college")
                        cursor = conn.cursor()
                        cursor.execute("select * from institutes")
                        rows=cursor.fetchall()
                        if len(rows)!=0:
                                self.college_table.delete(*self.college_table.get_children())
                                for row in rows :
                                        self.college_table.insert('',END,values=row)
                                conn.commit()
                                # self.search_clear()
                                conn.close()
                except pymysql.connect.Error as err:
                                messagebox.showerror("Database Error", f"Error: {err}")

        def delete_data(self):
                try:
                        if self.cl_var.get()=="":
                                messagebox.showerror("Alert", "Field Empty...!")

                        else:
                                conn=pymysql.connect(host="localhost",user="root",password="",database="college")
                                cursor = conn.cursor()
                                cursor.execute("delete from institutes where clname=%s",self.cl_var.get())
                                messagebox.showinfo("Success", "Data Deleted successfully!")
                
                       
                except pymysql.connect.Error as err:
                        messagebox.showerror("Database Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.commit()
                        conn.close()
                        self.clear()
                        self.fetch_data()

        def clear(self):
                self.cl_var.set("")    
                

        def get_cursor(self,ev):
                cursor_row=self.college_table.focus()
                contents=self.college_table.item(cursor_row)
                row=contents['values']
                # print(row)
                self.cl_var.set(row[0])
                               

root=Tk()
ob=student(root)

root.mainloop()                