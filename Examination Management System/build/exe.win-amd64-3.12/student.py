from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox,filedialog
import pymysql
from fpdf import FPDF
from datetime import datetime
import os 

def callback():
    root.destroy()
    filename = 'admin.py'
    os.system(filename) #Open file [Same as Right-click Open]
    

class student:
        

        def __init__(self,root):
                self.root=root
                self.root.title("Student Management System")
                self.root.geometry("1500x785+0+0")
                self.root.iconbitmap(r'images/logo.ico')


                title=Label(self.root,text="Student Management System",bd=5,relief=GROOVE,font=("times new roman",40,"bold"),bg="lightblue",fg="red")
                title.pack(side=TOP,fill=X)

                # ================= All variables ==========
                self.enroll_var=StringVar()
                self.roll_var=StringVar()
                self.name_var=StringVar()
                self.father_var=StringVar()
                # self.dob_var=StringVar()
                self.semester_var=StringVar()
                self.branch_var=StringVar(value="--Select--")
                self.year_var=StringVar(value="--Select--")
                self.institute_var=StringVar(value="--Select--")
                self.paper_var=StringVar(value="--Select--")
                self.search_by=StringVar(value="--Select--")
                self.search_txt=StringVar()



        # ========= Manage Frame ==================
                mf=Frame(self.root,bd=4,relief=RIDGE,bg="lightgray")
                mf.place(x=20,y=75,width=480,height=700)

                m_title=Label(mf,text="Manage Student",bg="wheat",fg="black",font=("times new roman",20,"bold"))
                m_title.grid(row=0,columnspan=2,pady=10)

                lbl_enroll=Label(mf,text="Enrollment",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_enroll.grid(row=1,column=0,pady=10,padx=10,sticky="w")

                txt_enroll=Entry(mf,textvariable=self.enroll_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_enroll.grid(row=1,column=1,pady=10,padx=10,sticky="w")

                lbl_roll=Label(mf,text="Roll No.",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_roll.grid(row=2,column=0,pady=10,padx=10,sticky="w")

                txt_roll=Entry(mf,textvariable=self.roll_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_roll.grid(row=2,column=1,pady=10,padx=10,sticky="w")

                lbl_name=Label(mf,text="Name",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_name.grid(row=3,column=0,pady=10,padx=10,sticky="w")

                txt_name=Entry(mf,textvariable=self.name_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE,)
                txt_name.grid(row=3,column=1,pady=10,padx=10,sticky="w")

                lbl_father=Label(mf,text="Father's Name",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_father.grid(row=4,column=0,pady=10,padx=10,sticky="w")

                txt_father=Entry(mf,textvariable=self.father_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                txt_father.grid(row=4,column=1,pady=10,padx=10,sticky="w")

                # lbl_birth=Label(mf,text="DOB",font=("times new roman",20,"bold"),bg="lightgray")
                # lbl_birth.grid(row=5,column=0,pady=10,padx=10,sticky="w")

                # txt_birth=Entry(mf,textvariable=self.dob_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
                # txt_birth.grid(row=5,column=1,pady=10,padx=10,sticky="w")

                lbl_institute=Label(mf,text="Institute",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_institute.grid(row=5,column=0,pady=10,padx=10,sticky="w")

                combo_institute = OptionMenu(mf, self.institute_var, *self.clnames)
                combo_institute.grid(row=5,column=1,pady=10,padx=10,sticky="w")
                

                lbl_branch=Label(mf,text="Branch",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_branch.grid(row=6,column=0,pady=10,padx=10,sticky="w")

                combo_branch = OptionMenu(mf, self.branch_var, *self.bname)
                combo_branch.grid(row=6,column=1,pady=10,padx=10,sticky="w")

                lbl_sem=Label(mf,text="Semester",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_sem.grid(row=7,column=0,pady=10,padx=10,sticky="w")

                combo_sem=ttk.Combobox(mf,textvariable=self.semester_var,font=("times new roman",16,"bold"),state="readonly")
                combo_sem['values']=("1","2","3","4","5","6")
                combo_sem.grid(row=7,column=1,pady=10,padx=10,sticky="w")

                lbl_year=Label(mf,text="Year",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_year.grid(row=8,column=0,pady=10,padx=10,sticky="w")

                combo_year = OptionMenu(mf, self.year_var, *self.year)
                combo_year.grid(row=8,column=1,pady=10,padx=10,sticky="w")

                lbl_paper=Label(mf,text="Paper",font=("times new roman",20,"bold"),bg="lightgray")
                lbl_paper.grid(row=9,column=0,pady=10,padx=10,sticky="w")

                combo_paper = OptionMenu(mf, self.paper_var, *self.paper)
                combo_paper.grid(row=9,column=1,pady=10,padx=10,sticky="w")

        # ==================== Button Frame =========================

                btn_frame=Frame(mf,bg="lightgray")
                btn_frame.place(x=12,y=650,width=450)

                addbtn=Button(btn_frame,text="Add",width=6,bg="lightgreen",font=(5),command=self.add_students).grid(row=0,column=0,padx=5)
                updatebtn=Button(btn_frame,text="Update",width=6,bg="lightyellow",font=(5),command=self.update_data).grid(row=0,column=1,padx=5)
                deletebtn=Button(btn_frame,text="Delete",width=6,bg="red",font=(5),command=self.delete_data).grid(row=0,column=2,padx=5)
                clrbtn=Button(btn_frame,text="Clear",width=6,bg="wheat",font=(5),command=self.clear).grid(row=0,column=3,padx=5)
                backbtn=Button(btn_frame,text="Back",width=6,bg="lightblue",font=(5) ,command=callback).grid(row=0,column=4,padx=5)
                
        # ===================================================================
                df=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
                df.place(x=520,y=75,width=950,height=700)

                lbl_search=Label(df,text="Search By",bg="lightblue",font=("times new roman",20,"bold"))
                lbl_search.grid(row=0,column=0,pady=10,sticky="w")

                combo_search=ttk.Combobox(df,textvariable=self.search_by,font=("times new roman",16,"bold"),state="readonly")
                combo_search['values']=("enroll","branch","name","paper","semester","institute","year")
                combo_search.grid(row=0,column=1,pady=10,padx=10,sticky="w")

                txt_search=Entry(df,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_search.grid(row=0,column=2,pady=10,padx=10,sticky="w")

                searchbtn=Button(df,text="Search",width=7,bg="lightyellow",font=(10),command=self.search_data).grid(row=0,column=3,padx=10)
                showbtn=Button(df,text="Show All",width=7,bg="wheat",font=(10),command=self.fetch_data).grid(row=0,column=4,padx=10)
                printbtn=Button(df,text="Print",width=6,bg="lightgreen",font=(10),command=self.generate_pdf).grid(row=0,column=5,padx=10)
        # ======================== Table Frame =============

                tf=Frame(df,bd=4,relief=RIDGE,bg="lightgray")
                tf.place(x=10,y=75,width=920,height=618)

                scroll_x=Scrollbar(tf,orient=HORIZONTAL)
                scroll_y=Scrollbar(tf,orient=VERTICAL)

                self.student_table=ttk.Treeview(tf,columns=("enroll","roll","name","father","sem","branch","year","paper","institute"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.student_table.xview)
                scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("enroll",text="Enrollment No")
                self.student_table.heading("roll",text="Roll No")
                self.student_table.heading("name",text="Name")
                self.student_table.heading("father",text="Father's Name")
                # self.student_table.heading("birth",text="Date of Birth")
                self.student_table.heading("sem",text="Sem")
                self.student_table.heading("branch",text="Branch")
                self.student_table.heading("year",text="Year")
                self.student_table.heading("paper",text="Back Papers")
                self.student_table.heading("institute",text="Institute")
                self.student_table['show']='headings'
                self.student_table.column("enroll",width=150)
                self.student_table.column("roll",width=150)
                self.student_table.column("name",width=170)
                self.student_table.column("father",width=170)
                # self.student_table.column("birth",width=150)
                self.student_table.column("sem",width=50)
                self.student_table.column("branch",width=120)
                self.student_table.column("year",width=100)
                self.student_table.column("paper",width=150)
                self.student_table.column("institute",width=160)
                self.student_table.pack(fill=BOTH,expand=1)
                self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
                self.fetch_data()


        def fetch_data_drop():
                try:
                        conn = mysql.connector.connect(
                        host='localhost',
                        user='root',  # Change as needed
                        password='',  # Change as needed
                        database='college'  # Change to your database name
                        )
                        cursor = conn.cursor()

                        # Fetch distinct values for each dropdown
                        cursor.execute("SELECT DISTINCT clname FROM institutes")
                        clnames = [row[0] for row in cursor.fetchall()]
                        clnames.insert(0, "None")  # Add "All" option
                        
                        cursor.execute("SELECT DISTINCT bname FROM branches")
                        bname = [row[0] for row in cursor.fetchall()]
                        bname.insert(0, "None")  # Add "All" option

                        cursor.execute("SELECT DISTINCT nyear FROM years")
                        year = [row[0] for row in cursor.fetchall()]
                        year.insert(0, "None")  # Add "All" option

                        cursor.execute("SELECT DISTINCT sname FROM subject")
                        paper = [row[0] for row in cursor.fetchall()]
                        paper.insert(0, "None")  # Add "All" option

                        return clnames,bname,year,paper

                except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.close()

        # Fetch data for dropdowns
        clnames,bname,year,paper = fetch_data_drop()


        def add_students(self):
                try:
                        if self.enroll_var.get()=="":
                                messagebox.showerror("Alert", "All Fields are mandatory!")
                        else:

                                conn=pymysql.connect(host="localhost",user="root",password="",database="stm")
                                cursor = conn.cursor()

                                # Insert student data
                                cursor.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.enroll_var.get(),self.roll_var.get(),self.name_var.get().strip().upper(),self.father_var.get(),self.semester_var.get(),self.branch_var.get().strip().upper(),self.year_var.get(),self.paper_var.get().strip().upper(),self.institute_var.get().strip().upper()
                                        ))
                                conn.commit()
                                self.clear()
                                cursor.close()
                                conn.close()
                                messagebox.showinfo("Success", "Data inserted successfully!")
                               
                except pymysql.connect.Error as err:
                                messagebox.showerror("Database Error", f"Error: {err}")
                finally:
                                self.fetch_data()

        def fetch_data(self):
                try:
                        conn=pymysql.connect(host="localhost",user="root",password="",database="stm")
                        cursor = conn.cursor()
                        cursor.execute("select * from student")
                        rows=cursor.fetchall()
                        if len(rows)!=0:
                                self.student_table.delete(*self.student_table.get_children())
                                for row in rows :
                                        self.student_table.insert('',END,values=row)
                                conn.commit()
                                self.search_clear()
                                conn.close()
                except pymysql.connect.Error as err:
                                messagebox.showerror("Database Error", f"Error: {err}")

        def clear(self):
                self.enroll_var.set("")
                self.roll_var.set("")
                self.name_var.set("")
                self.father_var.set("")
                # self.dob_var.set("")
                self.semester_var.set("")
                self.branch_var.set("")
                self.year_var.set("")
                self.paper_var.set("")
                self.institute_var.set("")


        def search_clear(self):
                self.search_by.set("")
                self.search_txt.set("")
                

        def get_cursor(self,ev):
                cursor_row=self.student_table.focus()
                contents=self.student_table.item(cursor_row)
                row=contents['values']
                # print(row)
                self.enroll_var.set(row[0])
                self.roll_var.set(row[1])
                self.name_var.set(row[2])
                self.father_var.set(row[3])
                # self.dob_var.set(row[4])
                self.semester_var.set(row[4])
                self.branch_var.set(row[5])
                self.year_var.set(row[6])
                self.paper_var.set(row[7])
                self.institute_var.set(row[8])
                
        def update_data(self):
                try:
                        conn=pymysql.connect(host="localhost",user="root",password="",database="stm")
                        cursor = conn.cursor()

                        # Insert student data
                        cursor.execute("update student set roll=%s,name=%s,father=%s,semester=%s,branch=%s,year=%s,paper=%s,institute=%s where enroll=%s",(self.roll_var.get(),self.name_var.get().strip().upper(),self.father_var.get(),self.semester_var.get(),self.branch_var.get().strip().upper(),self.year_var.get(),self.institute_var.get().strip().upper(),self.paper_var.get().strip().upper(),self.enroll_var.get()
                        ))
                        conn.commit()
                        self.clear()
                               
                        messagebox.showinfo("Success", "Data updated successfully!")

                               

                except pymysql.connect.Error as err:
                        messagebox.showerror("Database Error", f"Error: {err}")
                finally:
                        cursor.close()
                        self.fetch_data()
                        conn.close()

        def delete_data(self):
                try:
                        conn=pymysql.connect(host="localhost",user="root",password="",database="stm")
                        cursor = conn.cursor()
                        cursor.execute("delete from student where enroll=%s",self.enroll_var.get())
                        messagebox.showinfo("Success", "Data Deleted successfully!")
                       
                except pymysql.connect.Error as err:
                        messagebox.showerror("Database Error", f"Error: {err}")
                finally:
                        cursor.close()
                        conn.commit()
                        conn.close()
                        self.fetch_data()
                        self.clear()

        def search_data(self):
                try:
                        if self.search_by.get()=="" or self.search_txt.get()=="":
                                messagebox.showerror('Error',"Choose correct option!")        
                        else:

                                conn=pymysql.connect(host="localhost",user="root",password="",database="stm")
                                cursor = conn.cursor()
                                query="select * from student where " + str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get().strip().upper())+"%'"
                                cursor.execute(query)
                                rows=cursor.fetchall()
                                if len(rows)!=0:
                                        self.student_table.delete(*self.student_table.get_children())
                                        for row in rows :
                                                self.student_table.insert('',END,values=row)
                                        conn.commit()
                                        cursor.close()
                                else:
                                        messagebox.showerror("Denied", "There is no Data!")          


                except pymysql.connect.Error as err:
                        messagebox.showerror("Database Error", f"Error: {err}")
                finally:

                        # self.fetch_data()
                        conn.close()

        # Fetch data from the database
        def fetch_data_pdf(self):
                conn = pymysql.connect(host="localhost",user="root",password="",database="stm")
                cursor = conn.cursor()
                if self.search_by.get()=="" or self.search_txt.get()=="":
                        qry = "select enroll,roll,name,semester,branch,year,paper,institute from student "
                        cursor.execute(qry)
                else:         
                        qry = "select enroll,roll,name,semester,branch,year,paper,institute from student where " +str(self.search_by.get()) + " LIKE '%"+str(self.search_txt.get())+"%'"
                        # print(qry)
                        cursor.execute(qry)
                        # data = cursor.fetchall()
                # cursor.execute("SELECT * FROM users")
                data = cursor.fetchall()  # Fetch all data as a list of tuples
                conn.close()
                return data
        
        # Generate PDF
        def generate_pdf(self):
                # Generate a PDF from the fetched data."""
                data = self.fetch_data_pdf()
                # print(data)
                if not data:
                        messagebox.showinfo("Info", "No data found in the database.")
                        return
                
                
                # Ask for the file path to save the PDF
                # file_path = filedialog.asksaveasfilename(
                # defaultextension=".pdf",
                # filetypes=[("PDF files", "*.pdf")],
                # title="Save PDF as"
                # )

                

                # Generate a timestamp for the filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                default_filename = f"user_list_{timestamp}.pdf"
                # file_path = f"{file_path.rsplit('.', 1)[0]}_{timestamp}.pdf"
                file_path=filedialog.asksaveasfilename(
                defaultextension=".pdf",
                initialfile=default_filename,
                filetypes=[("PDF files", "*.pdf")],
                title="Save PDF as"
                )

                if not file_path:  # If the user cancels the dialog
                        return

                pdf = FPDF(orientation="landscape",format="A4")
                pdf.add_page()
                pdf.set_font("Arial", size=9)

                # Add a title
                pdf.cell(250, 10, txt="Student  List", ln=True, align='C')


                cell_widths=[35,35,40,10,30,15,36,30]
                # Add table header
                pdf.cell(cell_widths[0], 10, 'Enrollment', border=1)
                pdf.cell(cell_widths[1], 10, 'Roll', border=1)
                pdf.cell(cell_widths[2], 10, 'Name', border=1)
                pdf.cell(cell_widths[3], 10, 'Sem', border=1)
                pdf.cell(cell_widths[4], 10, 'Branch', border=1)
                pdf.cell(cell_widths[5], 10, 'Year', border=1)
                pdf.cell(cell_widths[6], 10, 'Institute', border=1)
                pdf.cell(cell_widths[7], 10, 'Paper', border=1)
                pdf.ln()

                # Add data to the PDF
                for row in data:
                        pdf.cell(cell_widths[0], 10, str(row[0]), border=1)  # ID
                        pdf.cell(cell_widths[1], 10, str(row[1]), border=1)  # ID
                        pdf.cell(cell_widths[2], 10, str(row[2]), border=1)  # ID
                        pdf.cell(cell_widths[3], 10, str(row[3]), border=1)  # ID
                        pdf.cell(cell_widths[4], 10, str(row[4]), border=1)  # ID
                        pdf.cell(cell_widths[5], 10, str(row[5]), border=1)  # ID
                        pdf.cell(cell_widths[6], 10, str(row[6]), border=1)  # ID
                        pdf.cell(cell_widths[7], 10, str(row[7]), border=1)  # ID  
                        pdf.ln()

                # Save the PDF to a file
                pdf.output(file_path)
                messagebox.showinfo("Success", "PDF generated successfully!")
root=Tk()
ob=student(root)

root.mainloop()