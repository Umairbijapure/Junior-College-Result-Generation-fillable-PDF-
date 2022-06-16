from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class add11stdA:

    def __init__(self,window):
        self.window=window
        self.window.title("Add Student")
        self.window.geometry("1350x700+80+170")
        self.window.config(bg="white")
        #title = Label(self.window, text="Add Student", padx=10,font=("goudy old stlye", 20, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=50)
        title = Label(self.window, text="Please Fill Student Details", padx=10,font=("goudy old stlye", 15, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=30)

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_class = StringVar()
        self.var_admission = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_std = StringVar()
        self.var_search = StringVar()


        #info details:column1
        lbl_roll=Label(self.window,text="Roll No:",font=("goudy old style",15,"bold"),bg='white').place(x=20, y=48,height=50)
        lbl_name = Label(self.window, text="Name:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=108,height=50)
        lbl_email = Label(self.window, text="Email:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=168,height=50)
        lbl_address = Label(self.window, text="Address:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=400,height=50)
        lbl_gender = Label(self.window, text="Gender:", font=("goudy old style", 15, "bold"), bg='white').place(x=20, y=228,height=50)#20 296 50
        lbl_sate = Label(self.window, text="State:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=288,height=50)
        self.txt_state = Entry(self.window, textvariable=self.var_state, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_state.place(x=125, y=358, width=200)
        lbl_city = Label(self.window, text="City:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=348,height=50)
        self.txt_city = Entry(self.window, textvariable=self.var_city, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_city.place(x=125, y=291, width=200)#125,358

        #info entry:column1
        self.txt_roll=Entry(self.window,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg='#e3f4fe')
        self.txt_roll.place(x=125,y=50,width=200)

        self.txt_name = Entry(self.window, textvariable=self.var_name, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_name.place(x=125, y=110, width=200)

        self.txt_email = Entry(self.window, textvariable=self.var_email, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_email.place(x=125, y=170, width=200)

        self.txt_gender = ttk.Combobox(self.window, textvariable=self.var_gender,values=("Select","male","female","other"),font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_gender.place(x=125, y=230, width=200)
        self.txt_gender.current(0)






        #TEXT Fields

        self.txt_address = Text(self.window, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_address.place(x=150, y=400, width=550,height=96)



        # info entry:column2
        lbl_dob = Label(self.window, text="DOB:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=48,height=50)
        lbl_contact = Label(self.window, text="Contact:", font=("goudy old style", 15, "bold"), bg='white').place(x=375, y=108,height=50)
        lbl_admission = Label(self.window, text="Admission:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=168,height=50)
        lbl_class = Label(self.window, text="Class:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=228,height=50)
        lbl_std = Label(self.window, text="Std:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=288,height=50)
        lbl_pin = Label(self.window, text="Pin Code:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=340,height=50)

        self.course_list=["Select","Class A","Class B","Class C"]
        self.std_list=["Select","XI","XII"]
        #self.fetch_details()
        self.txt_dob = Entry(self.window, textvariable=self.var_dob, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_dob.place(x=495, y=50, width=200)

        self.txt_contact = Entry(self.window, textvariable=self.var_contact, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_contact.place(x=495, y=110, width=200)

        self.txt_admission = Entry(self.window, textvariable=self.var_admission, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_admission.place(x=495, y=170, width=200)

        self.txt_class = ttk.Combobox(self.window, textvariable=self.var_class,values=(self.course_list),font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_class.place(x=495, y=230, width=200)  # 150 300 200
        self.txt_class.current(0)

        #self.txt_std = Entry(self.window, textvariable=self.var_std, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        #self.txt_std.place(x=495, y=288, width=200)
        self.txt_std = ttk.Combobox(self.window, textvariable=self.var_std,values=(self.std_list),font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_std.place(x=495, y=288, width=200)  # 150 300 200
        self.txt_std.current(0)


        self.txt_pin = Entry(self.window, textvariable=self.var_pin, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_pin.place(x=495, y=348, width=200)



        #buttons oparation
        self.btn_add=Button(self.window,text='Save',font=("goudy old style",15,"bold"),command=self.add,bg="#87d3f8")
        self.btn_add.place(x=150,y=510,width=110,height=40)
        self.btn_update = Button(self.window, text='Update', font=("goudy old style", 15, "bold"),command=self.update, bg="#87d3f8")
        self.btn_update.place(x=270, y=510, width=110, height=40)
        self.btn_add = Button(self.window, text='Delete', font=("goudy old style", 15, "bold"),command=self.delete, bg="#87d3f8")
        self.btn_add.place(x=390, y=510, width=110, height=40)
        self.btn_clear = Button(self.window, text='Clear', font=("goudy old style", 15, "bold"),command=self.clear_data, bg="#87d3f8")
        self.btn_clear.place(x=510, y=510, width=110, height=40)






        #SEARCH section
        lbl_search_roll=Label(self.window,text="Search Roll",font=("goudy old style",15,"bold"),bg="white").place(x=710,y=48,height=50)
        self.txt_search_roll=Entry(self.window,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg='#e3f4fe')
        self.txt_search_roll.place(x=860, y=50, width=200)
        self.btn_search=Button(self.window,text='Search',font=("goudy old style",15,"bold"),command=self.search,bg="red")
        self.btn_search.place(x=1070, y=50, width=110, height=30)
        #show table
        self.C_frame=Frame(self.window,bd=2,relief=RIDGE)
        self.C_frame.place(x=720,y=100,width=450,height=400)
        scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_frame,orient=HORIZONTAL)
        self.studentTable=ttk.Treeview(self.C_frame,columns=("roll","name","email","gender","dob","contact","admission","class","std","state","city","pin","address"))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.studentTable.xview)
        scrolly.config(command=self.studentTable.yview)

        self.studentTable.heading("roll",text="Roll")
        self.studentTable.heading("name",text="Name")
        self.studentTable.heading("email",text="Email")
        self.studentTable.heading("gender",text="Gender")
        self.studentTable.heading("dob",text="DOB")
        self.studentTable.heading("contact",text="Contact")
        self.studentTable.heading("admission",text="Admission")
        self.studentTable.heading("class",text="Class")
        self.studentTable.heading("std", text="Std")
        self.studentTable.heading("state",text="state")
        self.studentTable.heading("city",text="City")
        self.studentTable.heading("pin",text="Pin")
        self.studentTable.heading("address",text="Address")
        self.studentTable["show"]='headings'
        self.studentTable.column("roll",width=100)
        self.studentTable.column("name",width=100)
        self.studentTable.column("email",width=100)
        self.studentTable.column("gender",width=100)
        self.studentTable.column("dob",width=100)
        self.studentTable.column("contact",width=100)
        self.studentTable.column("admission",width=100)
        self.studentTable.column("class",width=100)
        self.studentTable.column("std", width=100)
        self.studentTable.column("state",width=100)
        self.studentTable.column("city",width=100)
        self.studentTable.column("pin",width=100)
        self.studentTable.column("address",width=200)
        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #self.fetch_details()

    def clear_data(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_admission.set(""),
        self.var_class.set(""),
        self.var_std.set(""),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0", END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":

                messagebox.showerror("Error","Roll no.should be required",parent=self.window)

            else:
                cur.execute("select * from studentTable where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error","please select studentTable from the list first",parent=self.window)

                else:
                    op=messagebox.askyesno("Confirm","Do you really wanto to delete?",parent=self.window)
                    if op==True:

                        cur.execute("delete from studentTable where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted succesfilly",parent=self.window)

                        self.clear_data()
        except Exception as ex:
            messagebox.showerror(("Error",f"Error due to{str(ex)}"))

    def get_data(self, ev):
        self.txt_roll.config(state='readonly')

        r=self.studentTable.focus()
        content=self.studentTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_admission.set(row[6]),
        self.var_class.set(row[7]),
        self.var_class.set(row[8]),
        self.var_state.set(row[9]),
        self.var_city.set(row[10]),
        self.var_pin.set(row[11]),
        self.txt_address.delete("1.0", END),
        self.txt_address.insert(END,row[10])





    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll no. should be required", parent=self.window)
            else:
                cur.execute("select *  from studentTable where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "Roll no. Already present", parent=self.window)
                else:

                    cur.execute("insert into studentTable(roll,name,email,gender,dob,contact,admission,class,std,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(

                           self.var_roll.get(),
                           self.var_name.get(),
                           self.var_email.get(),
                           self.var_gender.get(),
                           self.var_dob.get(),
                           self.var_contact.get(),
                           self.var_admission.get(),
                           self.var_class.get(),
                           self.var_std.get(),
                           self.var_state.get(),
                           self.var_city.get(),
                           self.var_pin.get(),
                           self.txt_address.get("1.0", END)))

                    con.commit()
                    messagebox.showinfo("Success", "student Added Successfully", parent=self.window)
                    self.show()
        except Exception as ex:

            messagebox.showerror("Error", f"Error due to  {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":

                messagebox.showerror("Error","Roll no. should be required",parent=self.window)
            else:
                cur.execute("select * from studentTable where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select studentTable from list",parent=self.window)
                else:
                    cur.execute("update StudentTable set name=?,email=?,gender=?,dob=?,contact=?,admission=?,class=?,std=?,state=?,city=?,pin=?,address=? where roll=?", (

                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_admission.get(),
                        self.var_class.get(),
                        self.var_std.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END),
                        self.var_roll.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Update Successfully",parent=self.window)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from studentTable")
            rows = cur.fetchall()
            self.studentTable.delete(*self.studentTable.get_children())
            for row in rows:
                self.studentTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    """def fetch_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from studentTable")
            rows = cur.fetchall()
            print(rows)

            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")"""



    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from studentTable where roll=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row != None:
                self.studentTable.delete(*self.studentTable.get_children())
                self.studentTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




if __name__=="__main__":
    window=Tk()
    obj1=add11stdA(window)
    window.mainloop()
