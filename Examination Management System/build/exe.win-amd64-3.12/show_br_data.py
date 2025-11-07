from tkinter import *
from tkinter import ttk
from tkinter import messagebox,filedialog
import pymysql
import os 


class branch:
        
        def callback(self):
                root.destroy()
                filename = 'reg_cl_data.py'
                os.system(filename) #Open file [Same as Right-click Open]

        def __init__(self,root):
                self.root=root
                self.root.title("Manage Branch Detail")
                self.root.iconbitmap(r'images/logo.ico')
                self.root.geometry("1500x785+0+0")

                title=Label(self.root,text="Manage Branch Detail",bd=5,relief=GROOVE,font=("times new roman",40,"bold"),bg="lightblue",fg="red")
                title.pack(side=TOP,fill=X)

                self.br_var=StringVar()

                # ========= Manage Frame ==================
                mf=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
                mf.place(x=20,y=75,width=480,height=200)

                m_title=Label(mf,text="Manage Data",bg="wheat",fg="black",font=("times new roman",20,"bold"))
                m_title.grid(row=0,columnspan=2,pady=10)
                lbl_branch=Label(mf,text="Branch",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_branch.grid(row=1,column=0,pady=10,padx=10,sticky="w")

                txt_branch=Entry(mf,textvariable=self.br_var,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
                txt_branch.grid(row=1,column=1,pady=10,padx=10,sticky="w")

                # ==================== Button Frame =========================

                btn_frame=Frame(mf,bg="lightgray")
                btn_frame.place(x=12,y=120,width=260)

              
                # updatebtn=Button(btn_frame,text="Update",width=6,bg="lightyellow",font=(5)).grid(row=0,column=0,padx=5)
                deletebtn=Button(btn_frame,text="Delete",width=6,bg="red",font=(5),command=self.delete_data,cursor="hand2").grid(row=0,column=1,padx=5)
                backbtn=Button(btn_frame,text="Back",width=6,bg="lightblue",font=(5) ,command=self.callback,cursor="hand2").grid(row=0,column=2,padx=5)

                # ===================================================================
                df=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
                df.place(x=520,y=75,width=950,height=700)
                



        # ======================== Table Frame =============

                tf=Frame(df,bd=4,relief=RIDGE,bg="lightgray")
                tf.place(x=5,width=935,height=685)

                scroll_x=Scrollbar(tf,orient=HORIZONTAL)
                scroll_y=Scrollbar(tf,orient=VERTICAL)

                self.branch_table=ttk.Treeview(tf,columns=("bname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.branch_table.xview)

                self.branch_table.heading("bname",text="Branch Name")
                self.branch_table['show']='headings'
                self.branch_table.column("bname",width=200)
                self.branch_table.pack(fill=BOTH,expand=1)
                self.branch_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()

        def fetch_data(self):
                try:
                        conn=pymysql.connect(host="localhost",user="root",password="",database="college")
                        cursor = conn.cursor()
                        cursor.execute("select * from branches")
                        rows=cursor.fetchall()
                        if len(rows)!=0:
                                self.branch_table.delete(*self.branch_table.get_children())
                                for row in rows :
                                        self.branch_table.insert('',END,values=row)
                                conn.commit()
                                # self.search_clear()
                                conn.close()
                except pymysql.connect.Error as err:
                                messagebox.showerror("Database Error", f"Error: {err}")

        def delete_data(self):
                try:
                        if self.br_var.get()=="":
                                messagebox.showerror("Alert", "Field Empty...!")
                        else:        
                                conn=pymysql.connect(host="localhost",user="root",password="",database="college")
                                cursor = conn.cursor()
                                cursor.execute("delete from branches where bname=%s",self.br_var.get())
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
                self.br_var.set("")    
                
                

        def get_cursor(self,ev):
                cursor_row=self.branch_table.focus()
                contents=self.branch_table.item(cursor_row)
                row=contents['values']
                # print(row)
                self.br_var.set(row[0])
                               

root=Tk()
ob=branch(root)

root.mainloop()                