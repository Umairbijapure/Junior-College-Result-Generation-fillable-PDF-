import os
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import ttk,messagebox
import sqlite3
con = sqlite3.connect(database="rms.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS bqkTable(grno INTEGER PRIMARY KEY AUTOINCREMENT,ebc_caste varchar, age float, mothers_name varchar, ht_wt float, date_of_birth varchar, roll_no int, students_name varchar)")
con.commit()

class csv_export:

    def __init__(self,window):
        self.window=window
        self.window.title("Import Data")
        self.window.geometry("1350x800+80+50")
        self.window.config(bg="#a0cff8")
        self.window.focus_force()
        title = Label(self.window, text="Note:Columns of the excel sheet should be in this format> ebc_caste , age , mothers_name, ht_wt , grno , date_of_birth , roll_no , students_name", padx=10,font=("goudy old stlye", 10), bg="#87CEFA", fg="red").place(x=44, y=650,height=50)
        #title = Label(self.window, text="Please Fill Student Details", padx=10,font=("goudy old stlye", 15, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=30)
        btn_course = Button(self.window, text="Import Excel file", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2",command=self.file_open).place(x=500, y=700, width=180, height=35)
        #btn_course = Button(self.window, text="Search", font=("goudym old style", 15), bg="#0b5377",
                            #fg="white", cursor="hand2", command=self.search).place(x=400, y=700, width=180,
                                                                                     # height=35)
        #variuables
        self.var_cast = StringVar()
        self.var_age = StringVar()
        self.var_mother = StringVar()
        self.var_ht_wt = StringVar()
        self.var_grno=StringVar()
        self.var_dob = StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()

        self.btn_delete_all = Button(self.window, text='Delete All', font=("goudy old style", 15, "bold"),
                                     command=self.delete_all, bg="red")
        self.btn_delete_all.place(x=300, y=700, width=110, height=30)



        #self.txt_grno = Entry(self.window, textvariable=self.var_grno, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        #self.txt_grno.place(x=130, y=700, width=200)
        #self.txt_name = Entry(self.window, textvariable=self.var_name, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        #self.txt_name.place(x=130, y=670, width=200)


        self.my_frame=Frame(window)
        #my_frame.pack(padx=20,pady=20,ipadx=200,ipady=200)
        self.my_frame.place(x=50,y=50,width=1385,height=595)
        scrolly = Scrollbar(self.my_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.my_frame, orient=HORIZONTAL)

        self.bqkTable=ttk.Treeview(self.my_frame)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.bqkTable.xview)
        scrolly.config(command=self.bqkTable.yview)
        self.bqkTable.pack(fill=BOTH,expand=1)
        #self.bqkTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()


        """df=pd.read_excel('bkq.xlsx')
        df.to_csv('bkq.csv', header=df.columns, index=False)
        df=pd.DataFrame(pd.read_csv("bkq.csv"))
        df.to_sql('bqkTable',con,if_exists='replace',index=False)
        cur.execute('select * from bqkTable ')
        row=cur.fetchall()
        bqkTable["column"]=list(df.columns)
        bqkTable["show"]="headings"
        #loop throu clmn list
        for column in bqkTable["column"]:
            bqkTable.heading(column,text=column)
        #put data in treeview
        df_rows=df.to_numpy().tolist()
        for row in df_rows:
            bqkTable.insert("","end",values=row)
        bqkTable.pack()"""
    def get_data(self, ev):
        #self.txt_grno.config()

        r=self.bqkTable.focus()
        content=self.bqkTable.item(r)
        row=content["values"]
        self.var_cast.set(row[0])
        self.var_age.set(row[1])
        self.var_mother.set(row[2])
        self.var_ht_wt.set(row[3])
        self.var_grno.set(row[4])
        self.var_dob.set(row[5])
        self.var_roll.set(row[6])
        self.var_name.set(row[7])
    def delete_all(self):
        for record in self.bqkTable.get_children():
            self.bqkTable.delete(record)
        conn=sqlite3.connect('rms.db')
        c=conn.cursor()
        op = messagebox.askyesno("Confirm", "Do you really wanto to delete?", parent=self.window)
        if op == True:
            c.execute('DROP TABLE bqkTable')
            messagebox.showinfo("Delete", "Deleted succesfilly", parent=self.window)
        conn.commit()
        conn.close()



    def file_open(self):
        filename = filedialog.askopenfilename(
            initialdir="Downloads",
            title="Open A File",
            filetype=(("xlsx files", "*.xlsx"), ("All files", "*.*"))
        )
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)
                # df = pd.read_excel('bkq.xlsx')
                df.to_csv('bkq.csv', header=df.columns, index=False)
                df = pd.DataFrame(pd.read_csv("bkq.csv"))
                self.clean(df)
                df.to_sql('bqkTable', con, if_exists='replace', index=False)
                cur.execute('select * from bqkTable ')
                row = cur.fetchall()
                for r in row:
                    print(r, end="\n")

            except ValueError:
                my_label.config(text="FIle Couldnt Be Opened..")
            except FileNotFoundError:
                my_label.config(text="FIle Couldnt Be found..")
        # clear old treeview
        # clear_tree()
        self.bqkTable["column"] = list(df.columns)
        self.bqkTable["show"] = "headings"
        # loop throu clmn list
        for column in self.bqkTable["column"]:
            self.bqkTable.heading(column, text=column)
        # put data in treeview
        self.df_rows = df.to_numpy().tolist()
        for row in self.df_rows:
            print("ggg")
            self.bqkTable.insert("", "end", values=row)
        self.bqkTable.pack()

    def clean(self,df):
        file="Customer Contracts$"
        clean_tbl_name=file.lower().replace(" ","_").replace("?","").replace("-","_").replace(r"/","_").replace("\\","_").replace("%","").replace(")","").replace(r"(","").replace("$","").replace(r"'","")
        print(clean_tbl_name)
        df.columns=[x.lower().replace(" ","_").replace("?","").replace("-","_").replace(r"/","_").replace("\\","_").replace("%","").replace(")","").replace(r"(","").replace("$","").replace(r"'","").replace("__","_").replace(".","") for x in df.columns]
        print(df.columns)
        replacements={
            'object':'varchar',
            'float64':'float',
            'int64':'int',
            'datetime64':'timestamp',
            'timedelta64[ns]':'varchar'
        }
        col_str=', '.join("{} {}".format(n,d)for n,d in zip(df.columns,df.dtypes.replace(replacements)))
        print(col_str)
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select students_name from bqkTable where grno=?", (self.var_grno.get(),))
            row = cur.fetchone()
            print(row,"llllllllll")
            if row != None:
                self.var_name.set(row[0])
                #self.var_std.set(row[1])
                #self.var_class.set(row[2])

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from bqkTable")
            rows = cur.fetchall()
            self.bqkTable.delete(*self.bqkTable.get_children())
            for row in rows:
                self.bqkTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")











if __name__=="__main__":
    window=Tk()
    obj1=csv_export(window)
    my_label = Label(window, text=20)
    window.mainloop()
