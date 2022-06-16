from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class course:
    def __init__(self,window):
        self.window=window
        self.window.title("Add Subjects")
        self.window.geometry("1350x700+80+170")
        self.window.config(bg="white")
        self.window.focus_force()
        #variables
        self.var_roll=StringVar()
        self.var_class=StringVar()
        self.var_std=StringVar()
        self.var_grn=StringVar()
        self.var_name=StringVar()
        self.tkvar1 =IntVar()
        self.tkvar2 =IntVar()
        self.tkvar3 = IntVar()
        self.tkvar4 = IntVar()
        self.tkvar5 = IntVar()
        self.tkvar6 = IntVar()
        self.tkvar7 = IntVar()
        self.tkvar8 = IntVar()
        self.tkvar9 = IntVar()
        self.roll_list = []
        self.class_list=["Select",'Class A',"Class B","Class C"]
        self.fetch_roll()
        #Labels
        title = Label(self.window, text="Add Subjects to a Student ", padx=10, font=("goudy old stlye", 15, "bold"),bg="#87CEFA", fg="white").place(x=0, y=0, relwidth=1, height=30)
        lbl_roll = Label(self.window, text="Roll no:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=85,height=50)
        lbl_class = Label(self.window, text="Class:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=125,height=50)
        lbl_std = Label(self.window, text="Std:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=175,height=50)
        lbl_grn = Label(self.window, text="GRNo:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=230,height=50)
        lbl_sub = Label(self.window, text="Name:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=285,height=50)
        #Entriess
        self.txt_student = ttk.Combobox(self.window, textvariable=self.var_roll, values=self.roll_list,font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        self.txt_student.place(x=180, y=85, width=200)
        self.txt_student.set("Select")

        self.txt_class = Entry(self.window, textvariable=self.var_class, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_class.place(x=180, y=125, width=100)
        #self.txt_class = ttk.Combobox(self.window, textvariable=self.var_class, values=self.class_list,font=("goudy old style", 15, "bold"), state='readonly', justify=CENTER)
        #self.txt_class.place(x=180, y=125, width=200)
        #self.txt_class.set("Select")

        self.txt_std = Entry(self.window, textvariable=self.var_std, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_std.place(x=180, y=175, width=100)

        self.txt_grn = Entry(self.window, textvariable=self.var_grn, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_grn.place(x=180, y=230, width=100)

        self.txt_name = Entry(self.window, textvariable=self.var_name, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_name.place(x=180, y=285, width=400)
        #buton
        self.btn_search = Button(self.window, text='Search', font=("times new roman", 15, "bold"), command=self.search,bg="red",cursor="hand2")
        self.btn_search.place(x=726, y=38, width=90, height=30)

        #frame
        self.C_frame=Frame(self.window,bd=2,relief=RIDGE)
        self.C_frame.place(x=820,y=50,width=600,height=600)
        scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_frame,orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.C_frame,columns=("roll","Std","Class","Grn","English","Physics","Chemistry","Maths","Biology","Geo","Urdu","Hindi","CS"))
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("roll",text="Roll")
        self.courseTable.heading("Std",text="Std")
        self.courseTable.heading("Class", text="Class")
        self.courseTable.heading("Grn", text="GRNo")
        self.courseTable.heading("English",text="English")
        self.courseTable.heading("Physics",text="Physics")
        self.courseTable.heading("Chemistry",text="Chemistry")
        self.courseTable.heading("Maths",text="Maths")
        self.courseTable.heading("Biology",text="Biology")
        self.courseTable.heading("Geo",text="Geography")
        self.courseTable.heading("Urdu",text="Urdu")
        self.courseTable.heading("Hindi",text="Hindi")
        self.courseTable.heading("CS",text="Computer Science")
        self.courseTable["show"]='headings'

        self.courseTable.column("roll",width=60)
        self.courseTable.column("Std", width=60)
        self.courseTable.column("Class", width=60)
        self.courseTable.column("Grn", width=60)
        self.courseTable.column("English",width=60)
        self.courseTable.column("Physics",width=60)
        self.courseTable.column("Chemistry",width=60)
        self.courseTable.column("Maths",width=60)
        self.courseTable.column("Biology",width=60)
        self.courseTable.column("Geo",width=60)
        self.courseTable.column("Urdu",width=60)
        self.courseTable.column("Hindi",width=60)
        self.courseTable.column("CS",width=60)
        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        self.c1 = Checkbutton(window, text='English', variable=self.tkvar1, onvalue=1, offvalue=0, command=self.selection,bg='#aadefc').place(x=600,y=85,width=150,height=50)
        #self.c1.pack()
        self.c2 = Checkbutton(window, text='Physics', variable=self.tkvar2, onvalue=1, offvalue=0, command=self.selection,bg='#e3e7fe').place(x=600,y=150,width=150,height=50)
        #self.c2.pack()

        self.c3 = Checkbutton(window, text='Chemistry', variable=self.tkvar3, onvalue=1, offvalue=0, command=self.selection,bg='#71c7fa').place(x=600,y=210,width=150,height=50)
        #self.c2.pack()
        self.c4 = Checkbutton(window, text='Maths', variable=self.tkvar4, onvalue=1, offvalue=0, command=self.selection,bg='#fefbe3').place(x=600,y=270,width=150,height=50)
        #self.c2.pack()
        self.c5 = Checkbutton(window, text='Biology', variable=self.tkvar5, onvalue=1, offvalue=0, command=self.selection,bg='#fee3f4').place(x=600,y=330,width=150,height=50)
        #self.c2.pack()
        self.c6 = Checkbutton(window, text='Geography', variable=self.tkvar6, onvalue=1, offvalue=0, command=self.selection,bg='#feede3').place(x=600,y=390,width=150,height=50)
        #self.c2.pack()
        self.c7 = Checkbutton(window, text='Urdu', variable=self.tkvar7, onvalue=1, offvalue=0, command=self.selection,bg='#e3fefb').place(x=600,y=450,width=150,height=50)
        #self.c2.pack()
        self.c8 = Checkbutton(window, text='Hindi', variable=self.tkvar8, onvalue=1, offvalue=0, command=self.selection,bg='#f6f3ec').place(x=600,y=510,width=150,height=50)
        #self.c2.pack()
        self.c9 = Checkbutton(window, text='CS', variable=self.tkvar9, onvalue=1, offvalue=0, command=self.selection,bg='#e3f4fe').place(x=600,y=570,width=150,height=50)
        #self.c2.pack()
        self.btn_add=Button(self.window,text='Save',font=("goudy old style",15,"bold"),command=self.add,bg="#87d3f8")
        self.btn_add.place(x=120,y=510,width=110,height=40)
        self.btn_update = Button(self.window, text='Update', font=("goudy old style", 15, "bold"),command=self.update, bg="#87d3f8")
        self.btn_update.place(x=240, y=510, width=110, height=40)
        self.btn_add = Button(self.window, text='Delete', font=("goudy old style", 15, "bold"),command=self.delete, bg="#87d3f8")
        self.btn_add.place(x=360, y=510, width=110, height=40)
        self.btn_clear = Button(self.window, text='Clear', font=("goudy old style", 15, "bold"),command=self.clear_data, bg="#87d3f8")
        self.btn_clear.place(x=480, y=510, width=110, height=40)

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,class,std from studentTable where roll=?  ", (self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_class.set(row[1])
                self.var_std.set(row[2])

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




    def clear_data(self):
        self.show()
        self.var_roll.set(""),
        self.var_class.set(""),
        self.var_std.set(""),
        self.var_grn.set(""),
        #self.var_sub.set(row[4])
        self.tkvar1.set(0),
        self.tkvar2.set(0),
        self.tkvar3.set(0),
        self.tkvar4.set(0),
        self.tkvar5.set(0),
        self.tkvar6.set(0),
        self.tkvar7.set(0),
        self.tkvar8.set(0),
        self.tkvar9.set(0),
        self.var_name.set("")
                                                    
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":

                messagebox.showerror("Error","Roll no.should be required",parent=self.window)

            else:
                cur.execute("select * from courseTable where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error","please select courseTable from the list first",parent=self.window)

                else:
                    op=messagebox.askyesno("Confirm","Do you really wanto to delete?",parent=self.window)
                    if op==True:

                        cur.execute("delete from courseTable where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted succesfilly",parent=self.window)

                        self.clear_data()
        except Exception as ex:
            messagebox.showerror(("Error",f"Error due to{str(ex)}"))



    def get_data(self, ev):
        #self.var_roll.config(state='readonly')

        r=self.courseTable.focus()
        content=self.courseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_class.set(row[1]),
        self.var_std.set(row[2]),
        self.var_grn.set(row[3]),

        #self.var_sub.set(row[4])
        self.tkvar1.set(row[4]),
        self.tkvar2.set(row[5]),
        self.tkvar3.set(row[6]),
        self.tkvar4.set(row[7]),
        self.tkvar5.set(row[8]),
        self.tkvar6.set(row[9]),
        self.tkvar7.set(row[10]),
        self.tkvar8.set(row[11]),
        self.tkvar9.set(row[12])

    def selection(self):
        lis=[self.tkvar1.get(),
             self.tkvar2.get(),
             self.tkvar3.get(),
             self.tkvar4.get(),
             self.tkvar5.get(),
             self.tkvar6.get(),
             self.tkvar7.get(),
             self.tkvar8.get(),
             self.tkvar9.get()]
        print(lis)





    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll no. should be required", parent=self.window)
            else:
                cur.execute("select *  from courseTable where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "Roll no. Already present", parent=self.window)
                else:

                    cur.execute("insert into courseTable(roll,Std,Class,Grn,English,Physics,Chemistry,Maths,Biology,Geo,Urdu,Hindi,CS) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(

                           self.var_roll.get(),
                           self.var_std.get(),
                           self.var_class.get(),
                           self.var_grn.get(),
                           self.tkvar1.get(),
                           self.tkvar2.get(),
                           self.tkvar3.get(),
                           self.tkvar4.get(),
                           self.tkvar5.get(),
                           self.tkvar6.get(),
                           self.tkvar7.get(),
                           self.tkvar8.get(),
                           self.tkvar9.get()
                    ) )

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
                cur.execute("select * from courseTable where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select courseTable from list",parent=self.window)
                else:
                    cur.execute("update courseTable set Std=?,Class=?,Grn=?,English=?,Physics=?,Chemistry=?,Maths=?,Biology=?,Geo=?,Urdu=?,Hindi=?,CS=? where roll=?", (

                        self.var_std.get(),
                        self.var_class.get(),
                        self.var_grn.get(),
                        self.tkvar1.get(),
                        self.tkvar2.get(),
                        self.tkvar3.get(),
                        self.tkvar4.get(),
                        self.tkvar5.get(),
                        self.tkvar6.get(),
                        self.tkvar7.get(),
                        self.tkvar8.get(),
                        self.tkvar9.get(),
                        self.var_roll.get()

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
            cur.execute("select * from courseTable")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from studentTable")
            rows = cur.fetchall()
            print(rows)

            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
                    #self.class_list.append(row[8])



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")





if __name__=="__main__":
    window=Tk()
    obj1=course(window)
    window.mainloop()
