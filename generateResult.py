from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
class resultClass():
    def __init__(self, window):
        self.window=window
        self.window.title("Generate Results")
        self.window.geometry("1350x700+80+170")
        self.window.config(bg="white")
        self.window.focus_force()
        #Variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_std = StringVar()
        self.var_class=StringVar()
        self.var_grn=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        self.var_math=StringVar()
        self.var_bio =StringVar()
        self.var_phy=StringVar()
        self.var_chem=StringVar()
        self.var_ur=StringVar()
        self.var_eng=StringVar()
        self.var_Hin=StringVar()
        self.var_geo=StringVar()
        self.var_cs1=StringVar()
        self.var_cs2=StringVar()
        self.var_ET46=StringVar()
        self.var_ET47=StringVar()
        self.var_ET48=StringVar()
        self.var_ET49=StringVar()
        self.var_ET50=StringVar()
        self.var_ET51=StringVar()
        self.var_ET52=StringVar()
        self.var_ET53=StringVar()
        self.var_ET54=StringVar()
        self.var_Cs2_6 = StringVar()
        self.var_date=StringVar()
        self.var_result=StringVar()
        self.var_grandtotal=StringVar()
        self.var_grade=StringVar()
        self.var_perc=StringVar()
        self.var_adress=StringVar()
        self.var_reopening=StringVar()
        self.var_env=StringVar()
        self.var_pe=StringVar()
        #self.generate_btn = QPushButton("Generate PDF")
        #self.generate_btn.pressed.connect(self.generate)

        #Grace variables
        self.var_ET461=IntVar()
        self.var_ET471=IntVar()
        self.var_ET481=IntVar()
        self.var_ET491=IntVar()
        self.var_ET501=IntVar()
        self.var_ET511=IntVar()
        self.var_ET521=IntVar()
        self.var_ET531=IntVar()
        self.var_ET541=IntVar()
        self.var_Cs2_61 = IntVar()
        #labels
        lbl_select = Label(self.window, text="Select Student:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=35,height=50)
        lbl_std = Label(self.window, text="Std:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=70,height=50)
        lbl_class = Label(self.window, text="Class:", font=("goudy old style", 15, "bold"), bg='white').place(x=200,y=70,height=50)
        lbl_adress = Label(self.window, text="Address:", font=("goudy old style", 15, "bold"), bg='white').place(x=390,y=70,height=50)
        lbl_grn = Label(self.window, text="GRNo:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=105,height=50)
        lbl_name = Label(self.window, text="Name:", font=("goudy old style", 15, "bold"), bg='white').place(x=200,y=105,height=40)
        lbl_date = Label(self.window, text="Date:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=168,height=50)
        lbl_result = Label(self.window, text="Result:", font=("goudy old style", 15, "bold"), bg='white').place(x=375, y=205,height=50)
        lbl_grand = Label(self.window, text="Grand Total:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=240,height=50)
        lbl_perc = Label(self.window, text="Percentage:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=275,height=50)
        lbl_grade = Label(self.window, text="Grade:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=310,height=50)
        lbl_env = Label(self.window, text="Environent:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=345,height=50)
        lbl_pe = Label(self.window, text="PE:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=380,height=50)
        lbl_reopning = Label(self.window, text="Reopening:", font=("goudy old style", 15, "bold"), bg='white').place(x=375,y=415,height=50)

        #lbl_math = Label(self.window, text="Mathematics:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=160,height=50)
        self.txt_E46 = Entry(self.window, textvariable=self.var_math, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E46.place(x=20, y=160, width=100)

        #lbl_bio = Label(self.window, text="biology:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=200,height=50)
        self.txt_E47 = Entry(self.window, textvariable=self.var_bio, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E47.place(x=20, y=200, width=100)

        #lbl_phy = Label(self.window, text="Physics:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=240,height=50)
        self.txt_E48 = Entry(self.window, textvariable=self.var_phy, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E48.place(x=20, y=240, width=100)


        #lbl_chem = Label(self.window, text="Chemistry:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=280,height=50)
        self.txt_E49 = Entry(self.window, textvariable=self.var_chem, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E49.place(x=20, y=280, width=100)


        #lbl_urdu = Label(self.window, text="Urdu:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=320,height=50)
        self.txt_E50 = Entry(self.window, textvariable=self.var_ur, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E50.place(x=20, y=320, width=100)

        #lbl_eng = Label(self.window, text="English:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=360,height=50)
        self.txt_E51 = Entry(self.window, textvariable=self.var_eng, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E51.place(x=20, y=360, width=100)

        #lbl_hindi = Label(self.window, text="Hindi:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=400,height=50)
        self.txt_E52 = Entry(self.window, textvariable=self.var_Hin, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E52.place(x=20, y=400, width=100)

        #lbl_geo = Label(self.window, text="Geography:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=440,height=50)
        self.txt_E53 = Entry(self.window, textvariable=self.var_geo, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E53.place(x=20, y=440, width=100)

        #lbl_cs1 = Label(self.window, text="CS1:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=480,height=50)
        self.txt_E54 = Entry(self.window, textvariable=self.var_cs1, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_E54.place(x=20, y=480, width=100)


        #lbl_cs2 = Label(self.window, text="CS2:", font=("goudy old style", 15, "bold"), bg='white').place(x=20,y=520,height=50)
        self.txt_Cs2_6 = Entry(self.window, textvariable=self.var_cs2, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_Cs2_6.place(x=20, y=520, width=100)


        #Entriies
        self.txt_student = ttk.Combobox(self.window, textvariable=self.var_roll,values=self.roll_list, font=("goudy old style", 15, "bold"),state='readonly', justify=CENTER)
        self.txt_student.place(x=180, y=40, width=150)
        self.txt_student.set("Select")

        self.txt_name = Entry(self.window, textvariable=self.var_name, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_name.place(x=280, y=110, width=400)

        self.txt_std = Entry(self.window, textvariable=self.var_std, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_std.place(x=90, y=80, width=100)

        self.txt_class = Entry(self.window, textvariable=self.var_class, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_class.place(x=280, y=80, width=100)

        self.txt_adress = Entry(self.window, textvariable=self.var_adress, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_adress.place(x=500 , y=80, width=300)

        self.txt_grn = Entry(self.window, textvariable=self.var_grn, font=("goudy old style", 15,"bold"),bg='#e3f4fe',state='readonly')
        self.txt_grn.place(x=90, y=110, width=100)

        self.txt_E46 = Entry(self.window, textvariable=self.var_ET46, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E46.place(x=200, y=160, width=80)

        self.txt_E47 = Entry(self.window, textvariable=self.var_ET47, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E47.place(x=200, y=200, width=80)

        self.txt_E48 = Entry(self.window, textvariable=self.var_ET48, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E48.place(x=200, y=240, width=80)

        self.txt_E49 = Entry(self.window, textvariable=self.var_ET49, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E49.place(x=200, y=280, width=80)

        self.txt_E50 = Entry(self.window, textvariable=self.var_ET50, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E50.place(x=200, y=320, width=80)

        self.txt_E51 = Entry(self.window, textvariable=self.var_ET51, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E51.place(x=200, y=360, width=80)

        self.txt_E52 = Entry(self.window, textvariable=self.var_ET52, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E52.place(x=200, y=400, width=80)

        self.txt_E53 = Entry(self.window, textvariable=self.var_ET53, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E53.place(x=200, y=440, width=80)

        self.txt_E54 = Entry(self.window, textvariable=self.var_ET54, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E54.place(x=200, y=480, width=80)

        self.txt_Cs2_6 = Entry(self.window, textvariable=self.var_Cs2_6, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_6.place(x=200, y=520, width=80)
        #Grace
        self.txt_E461 = Entry(self.window, textvariable=self.var_ET461, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E461.place(x=300, y=160, width=80)

        self.txt_E471 = Entry(self.window, textvariable=self.var_ET471, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E471.place(x=300, y=200, width=80)

        self.txt_E481 = Entry(self.window, textvariable=self.var_ET481, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E481.place(x=300, y=240, width=80)

        self.txt_E491 = Entry(self.window, textvariable=self.var_ET491, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E491.place(x=300, y=280, width=80)

        self.txt_E501 = Entry(self.window, textvariable=self.var_ET501, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E501.place(x=300, y=320, width=80)

        self.txt_E511 = Entry(self.window, textvariable=self.var_ET511, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E511.place(x=300, y=360, width=80)

        self.txt_E521 = Entry(self.window, textvariable=self.var_ET521, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E521.place(x=300, y=400, width=80)

        self.txt_E531 = Entry(self.window, textvariable=self.var_ET531, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E531.place(x=300, y=440, width=80)

        self.txt_E541 = Entry(self.window, textvariable=self.var_ET541, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_E541.place(x=300, y=480, width=80)

        self.txt_Cs2_61 = Entry(self.window, textvariable=self.var_Cs2_61, font=("goudy old style", 15,"bold"),bg='#e3f4fe')
        self.txt_Cs2_61.place(x=300, y=520, width=80)

        #column2
        self.txt_date = Entry(self.window, textvariable=self.var_date, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_date.place(x=495, y=168, width=200)

        self.txt_result = Entry(self.window, textvariable=self.var_result, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_result.place(x=495, y=205, width=200)

        self.txt_grandtotal = Entry(self.window, textvariable=self.var_grandtotal, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_grandtotal.place(x=495, y=240, width=200)

        self.txt_perc = Entry(self.window, textvariable=self.var_perc, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_perc.place(x=495, y=275, width=200)

        self.txt_grade = Entry(self.window, textvariable=self.var_grade, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_grade.place(x=495, y=310, width=200)

        self.txt_env = Entry(self.window, textvariable=self.var_env, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_env.place(x=495, y=345, width=200)

        self.txt_pe = Entry(self.window, textvariable=self.var_pe, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_pe.place(x=495, y=380, width=200)


        self.txt_reopening = Entry(self.window, textvariable=self.var_reopening, font=("goudy old style", 15, "bold"),bg='#e3f4fe')
        self.txt_reopening.place(x=495, y=415, width=200)





        #Buttons
        self.btn_search=Button(self.window,text='Search',font=("times new roman",15,"bold"),command=self.search,bg="red",cursor="hand2")
        self.btn_search.place(x=340, y=40, width=110, height=30)
        self.btn_search=Button(self.window,text='Get Result',font=("times new roman",15,"bold"),command=self.main_result,bg="red",cursor="hand2")
        self.btn_search.place(x=495, y=450, width=110, height=30)
        self.btn_search=Button(self.window,text='Generate Result',font=("times new roman",15,"bold"),command=self.generate,bg="red",cursor="hand2")
        self.btn_search.place(x=400, y=500, width=160, height=30)
        self.btn_search=Button(self.window,text='Generate CSV',font=("times new roman",15,"bold"),command=self.main_result,bg="red",cursor="hand2")
        self.btn_search.place(x=600, y=500, width=160, height=30)
        #Frame
        self.C_frame = Frame(self.window, bd=2, relief=RIDGE)
        self.C_frame.place(x=820, y=50, width=600, height=600)
        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)
        self.resultTable = ttk.Treeview(self.C_frame, columns=("roll", "Std", "Class", "Grn", "Math", "Bio", "Phy", "Chem", "Urdu", "Eng", "Hin", "Geo","Cs1","Cs2","env","pe","date","result","grandtotal","perc","grade","name","adress"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=X)
        scrollx.config(command=self.resultTable.xview)
        scrolly.config(command=self.resultTable.yview)

        self.resultTable.heading("roll", text="Roll")
        self.resultTable.heading("Std", text="Std")
        self.resultTable.heading("Class", text="Class")
        self.resultTable.heading("Grn", text="GRNo")
        self.resultTable.heading("Math", text="Math")
        self.resultTable.heading("Bio", text="Biology")
        self.resultTable.heading("Phy", text="physics")
        self.resultTable.heading("Chem", text="Chemistry")
        self.resultTable.heading("Urdu", text="Urdu")
        self.resultTable.heading("Eng", text="English")
        self.resultTable.heading("Hin", text="Hindi")
        self.resultTable.heading("Geo", text="Geograpy")
        self.resultTable.heading("Cs1", text="CS1")
        self.resultTable.heading("Cs2", text="CS2")
        self.resultTable.heading("env", text="Environment")
        self.resultTable.heading("pe", text="P.E.")
        self.resultTable.heading("date",text="Date")
        self.resultTable.heading("result",text="Result")
        self.resultTable.heading("grandtotal",text="grandtotal")
        self.resultTable.heading("perc",text="percentage")
        self.resultTable.heading("grade",text="grade")
        self.resultTable.heading("name",text="Name")
        self.resultTable.heading("adress",text="Address")


        self.resultTable["show"] = 'headings'
        self.resultTable.column("roll", width=60)
        self.resultTable.column("Std", width=60)
        self.resultTable.column("Class", width=60)
        self.resultTable.column("Grn", width=60)
        self.resultTable.column("Math", width=60)
        self.resultTable.column("Bio", width=60)
        self.resultTable.column("Phy", width=60)
        self.resultTable.column("Chem", width=60)
        self.resultTable.column("Urdu", width=60)
        self.resultTable.column("Eng", width=60)
        self.resultTable.column("Hin", width=60)
        self.resultTable.column("Geo", width=60)
        self.resultTable.column("Cs1", width=60)
        self.resultTable.column("Cs2", width=60)
        self.resultTable.column("env", width=60)
        self.resultTable.column("pe", width=60)
        self.resultTable.column("date", width=60)
        self.resultTable.column("result",width=60)
        self.resultTable.column("grandtotal",width=60)
        self.resultTable.column("perc",width=60)
        self.resultTable.column("grade",width=80)
        self.resultTable.column("name",width=180)
        self.resultTable.column("adress",width=180)
        self.resultTable.pack(fill=BOTH, expand=1)
        self.resultTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        #buttons
        self.btn_add=Button(self.window,text='Save',font=("goudy old style",15,"bold"),command=self.add,bg="#87d3f8")
        self.btn_add.place(x=150,y=600,width=110,height=40)
        self.btn_update = Button(self.window, text='Update', font=("goudy old style", 15, "bold"),command=self.update, bg="#87d3f8")
        self.btn_update.place(x=270, y=600, width=110, height=40)
        self.btn_add = Button(self.window, text='Delete', font=("goudy old style", 15, "bold"),command=self.delete, bg="#87d3f8")
        self.btn_add.place(x=390, y=600, width=110, height=40)
        self.btn_clear = Button(self.window, text='Clear', font=("goudy old style", 15, "bold"),command=self.clear_data, bg="#87d3f8")
        self.btn_clear.place(x=510, y=600, width=110, height=40)
        #main result
        #self.main_result()




    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from studentTable")
            rows = cur.fetchall()

            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from courseTable where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            cur.execute("select name,address from studentTable where roll=?", (self.var_roll.get(),))
            row2 = cur.fetchone()
            cur.execute("select ET46,ET47,ET48,ET49,ET50,ET51,ET52,ET53,ET54,Cs_2_6 from marksTable where roll=?", (self.var_roll.get(),))
            row3 = cur.fetchone()


            if row != None:

                self.var_std.set(row[1])

                self.var_class.set(row[2])
                self.var_grn.set(row[3])
                #print(row[7])
                if row[4]=="1":
                    self.var_math.set("Math")
                else:
                    self.var_math.set("-")
                if row[5]=="1":
                    self.var_bio.set("Biology")
                else:
                    self.var_bio.set("-")
                if row[6]=="1":
                    self.var_phy.set("Physics")
                else:
                    self.var_phy.set("-")
                if row[7]=="1":
                    self.var_chem.set("Chemistry")
                else:
                    self.var_chem.set("-")
                if row[8]=="1":
                    self.var_ur.set("Urdu")
                else:
                    self.var_ur.set("-")
                if row[9]=="1":
                    self.var_eng.set("English")
                else:
                    self.var_eng.set("-")
                if row[10]=="1":
                    self.var_Hin.set("Hindi")
                else:
                    self.var_Hin.set("-")
                if row[11]=="1":
                    self.var_geo.set("Geography")
                else:
                    self.var_geo.set("-")
                if row[12]=="1":
                    self.var_cs1.set("CS1")
                else:
                    self.var_cs1.set("-")
                if row[12]=="1":
                    self.var_cs2.set("CS2")
                else:
                    self.var_cs2.set("-")

            if row2!=None:
                self.var_name.set(row2[0])
                self.var_adress.set(row2[1])
            if row3!=None:
                if row[4]=="1":
                    self.var_ET46.set(row3[0])
                    if float(row3[0])<35:
                        #print(35-float(row3[0]),"hereee")
                        self.var_ET461.set(35-float(row3[0]))
                else:
                    self.var_ET46.set("-")
                    self.var_ET461.set("-")
                if row[5]=="1":
                    self.var_ET47.set(row3[1])
                    if float(row3[1])<35:
                        self.var_ET471.set(35-float(row3[1]))
                else:
                    self.var_ET47.set("-")
                    self.var_ET471.set("-")
                if row[6]=="1":
                    self.var_ET48.set(row3[2])
                    if float(row3[2])<35:
                        self.var_ET481.set(35-float(row3[2]))
                else:
                    self.var_ET48.set("-")
                    self.var_ET48.set("-")
                if row[7]=="1":
                    self.var_ET49.set(row3[3])
                    if float(row3[3])<35:
                        self.var_ET49.set(35-float(row3[3]))
                else:
                    self.var_ET49.set("-")
                    self.var_ET491.set("-")
                if row[8]=="1":
                    self.var_ET50.set(row3[4])
                    if float(row3[4])<35:
                        self.var_ET501.set(35-float(row3[4]))
                else:
                    self.var_ET50.set("-")
                    self.var_ET501.set("-")
                if row[9]=="1":
                    self.var_ET51.set(row3[5])
                    if float(row3[5])<35:
                        self.var_ET511.set(35-float(row3[5]))
                else:
                    self.var_ET51.set("-")
                    self.var_ET511.set("-")
                if row[10]=="1":
                    self.var_ET52.set(row3[6])
                    if float(row3[6])<35:
                        self.var_ET521.set(35-float(row3[6]))
                else:
                    self.var_ET52.set("-")
                    self.var_ET521.set("-")
                if row[11]=="1":
                    self.var_ET53.set(row3[7])
                    if float(row3[7])<35:
                        self.var_ET531.set(35-float(row3[7]))
                else:
                    self.var_ET53.set('-')
                    self.var_ET531.set('-')
                if row[12]=="1":
                    self.var_ET54.set(row3[8])
                    self.var_Cs2_6.set(row3[9])
                    if float(row3[8])<35:
                        self.var_ET541.set(35-float(row3[8]))
                    if float(row3[9])<35:
                        self.var_Cs2_61.set(35-float(row3[9]))

                else:
                    self.var_ET54.set("-")
                    self.var_Cs2_6.set("-")
                    self.var_ET541.set("-")
                    self.var_Cs2_61.set("-")


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
        self.var_math.set(""),
        self.var_bio.set(""),
        self.var_phy.set(""),
        self.var_chem.set(""),
        self.var_ur.set(""),
        self.var_eng.set(""),
        self.var_Hin.set(""),
        self.var_geo.set(""),
        self.var_cs1.set(""),
        self.var_cs2.set(""),
        self.var_ET46.set(""),
        self.var_ET47.set(""),
        self.var_ET48.set(""),
        self.var_ET49.set(""),
        self.var_ET50.set(""),
        self.var_ET51.set(""),
        self.var_ET52.set(""),
        self.var_ET53.set(""),
        self.var_ET54.set(""),
        self.var_Cs2_6.set(""),
        self.var_date.set(""),
        self.var_result.set(""),
        self.var_grandtotal.set(""),
        self.var_perc.set(""),
        self.var_grade.set(""),
        self.var_ET461.set(""),
        self.var_ET471.set(""),
        self.var_ET481.set(""),
        self.var_ET491.set(""),
        self.var_ET501.set(""),
        self.var_ET511.set(""),
        self.var_ET521.set(""), 
        self.var_ET531.set(""),
        self.var_ET541.set(""),
        self.var_Cs2_61.set(""),
        self.var_name.set(""),
        self.var_adress.set(""),
        self.var_env.set(""),
        self.var_pe.set("")


    def get_data(self, ev):
        #self.var_roll.config(state='readonly')

        r=self.resultTable.focus()
        content=self.resultTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_class.set(row[1]),
        self.var_std.set(row[2]),
        self.var_grn.set(row[3]),
        #self.var_sub.set(row[4])
#        self.var_math.set(row[4]),
#        self.var_bio.set(row[5]),
#        self.var_phy.set(row[6]),
#        self.var_chem.set(row[7]),
#        self.var_ur.set(row[8]),
#        self.var_eng.set(row[9]),
#        self.var_Hin.set(row[10]),
#        self.var_geo.set(row[11]),
#        self.var_cs1.set(row[12])
#        self.var_cs2.set(row[13])
        self.var_ET46.set(row[4]),
        self.var_ET47.set(row[5]),
        self.var_ET48.set(row[6]),
        self.var_ET49.set(row[7]),
        self.var_ET50.set(row[8]),
        self.var_ET51.set(row[9]),
        self.var_ET52.set(row[10]),
        self.var_ET53.set(row[11]),
        self.var_ET54.set(row[12]),
        self.var_Cs2_6.set(row[13]),
        self.var_env.set(row[14]),
        self.var_pe.set(row[15])
        self.var_date.set(row[16]),
        self.var_result.set(row[17]),
        self.var_grandtotal.set(row[18]),
        self.var_perc.set(row[19]),
        self.var_grade.set(row[20]),
        self.var_name.set(row[21]),
        self.var_adress.set(row[22])


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":

                messagebox.showerror("Error","Roll no.should be required",parent=self.window)

            else:
                cur.execute("select * from resultTable where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error","please select resultTable from the list first",parent=self.window)

                else:
                    op=messagebox.askyesno("Confirm","Do you really wanto to delete?",parent=self.window)
                    if op==True:

                        cur.execute("delete from resultTable where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted succesfilly",parent=self.window)

                        self.clear_data()
        except Exception as ex:
            messagebox.showerror(("Error",f"Error due to{str(ex)}"))



    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll no. should be required", parent=self.window)
            else:
                cur.execute("select *  from resultTable where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "Roll no. Already present", parent=self.window)
                else:

                    cur.execute("insert into resultTable(roll,Std,Class,Grn,Math,Bio,Phy,Chem,Urdu,Eng,Hin,Geo,Cs1,Cs2,env,pe,date,result,grandtotal,perc,grade,name,adress) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(

                           self.var_roll.get(),
                           self.var_std.get(),
                           self.var_class.get(),
                           self.var_grn.get(),
                           self.var_ET46.get(),
                           self.var_ET47.get(),
                           self.var_ET48.get(),
                           self.var_ET49.get(),
                           self.var_ET50.get(),
                           self.var_ET51.get(),
                           self.var_ET52.get(),
                           self.var_ET53.get(),
                           self.var_ET54.get(),
                           self.var_Cs2_6.get(),
                           self.var_env.get(),
                           self.var_pe.get(),
                           #self.var_math.get(),
                           #self.var_bio.get(),
                           #self.var_phy.get(),
                           #self.var_chem.get(),
                           #self.var_ur.get(),
                           #self.var_eng.get(),
                           #self.var_Hin.get(),
                           #self.var_geo.get(),
                           #self.var_cs1.get(),
                           #self.var_cs2.get(),
                           self.var_date.get(),
                           self.var_result.get(),
                           self.var_grandtotal.get(),
                           self.var_perc.get(),
                           self.var_grade.get(),
                           self.var_name.get(),
                           self.var_adress.get()



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
                cur.execute("select * from resultTable where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select resultTable from list",parent=self.window)
                else:
                    cur.execute("update resultTable set Std=?,Class=?,Grn=?,Math=?,Bio=?,Phy=?,Chem=?,Urdu=?,Eng=?,Hin=?,Geo=?,Cs1=?,Cs2=?,env=?,pe=?,date=?,result=?,grandtotal=?,perc=?,grade=?,name=?,adress=? where roll=?", (

                        self.var_std.get(),
                        self.var_class.get(),
                        self.var_grn.get(),
                        self.var_ET46.get(),
                        self.var_ET47.get(),
                        self.var_ET48.get(),
                        self.var_ET49.get(),
                        self.var_ET50.get(),
                        self.var_ET51.get(),
                        self.var_ET52.get(),
                        self.var_ET53.get(),
                        self.var_ET54.get(),
                        self.var_Cs2_6.get(),
                        self.var_env.get(),
                        self.var_pe.get(),
                        #self.var_math.get(),
                        #self.var_bio.get(),
                        #self.var_phy.get(),
                        #self.var_chem.get(),
                        #self.var_ur.get(),
                        #self.var_eng.get(),
                        #self.var_Hin.get(),
                        #self.var_geo.get(),
                        #self.var_cs1.get(),
                        #self.var_cs2.get(),
                        self.var_date.get(),
                        self.var_result.get(),
                        self.var_grandtotal.get(),
                        self.var_perc.get(),
                        self.var_grade.get(),
                        self.var_name.get(),
                        self.var_adress.get(),
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
            cur.execute("select * from resultTable")
            rows = cur.fetchall()
            self.resultTable.delete(*self.resultTable.get_children())
            for row in rows:
                self.resultTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def main_result(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select Math,Bio,Phy,Chem,Urdu,Eng,Hin,Geo,Cs1,Cs2 from resultTable where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                sum=0
                for r in row:

                    if r!='-':
                        sum=sum+float(r)
                self.var_grandtotal.set(sum)
                perc=(sum/600)*100
                self.var_perc.set(round(perc,2))
                print(perc)
                if perc>=75:
                    self.var_grade.set("Ist Class with Distinction")
                    self.var_result.set("Pass")
                elif 75>perc>=60:
                    self.var_grade.set("Ist Class")
                    self.var_result.set("Pass")
                elif 60>perc>=45:
                    self.var_grade.set("2nd Class")
                    self.var_result.set("Pass")
                elif perc<35:
                    self.var_result.set("Fail")


            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def generate(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from resultTable where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            print(row)
            if row != None:
                self.var_name.set(row[21])

            else:
                messagebox.showerror("Error", "No record found", parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFillColorRGB(1, 0, 0)
        can.setFont("Times-Roman", 14)
        can.drawString(174,687, str(row[21]))
        can.drawString(174, 660, str(row[2]+'-'+row[1]))
        can.drawString(174, 633, str(row[0]))
        can.drawString(174, 607, str(row[3]))
        can.drawString(174, 580, str(row[16]))
        #can.drawString(174, 552, str(row[14]))reopenning
        can.drawString(468,477, str(row[4])) #1
        can.drawString(468,450, str(row[5])) #2
        can.drawString(468,430, str(row[6])) #3
        can.drawString(468,410, str(row[7])) #4
        can.drawString(468,387, str(row[8])) #5
        can.drawString(468,365, str(row[9])) #6
        can.drawString(468,345, str(row[10])) #7
        can.drawString(468,325, str(row[11])) #8
        can.drawString(468,305, str((row[12])+(row[13]))) #9
        can.drawString(468,285, str(row[14]))  # 11
        can.drawString(468,265 , str(row[15]))  # 12
        can.drawString(136, 215, str(row[19]))  # 13
        can.drawString(136,178, str(row[18])) #13
        can.drawString(136, 108, str(row[20]))  # 14


        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        existing_pdf = PdfFileReader(open("SSAR.pdf", "rb"))
        output = PdfFileWriter()
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        outputStream = open("AAAAA.pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        messagebox.showinfo("Success", "Result Generated Successfully", parent=self.window)
        self.show()



if __name__=="__main__":
    window=Tk()
    obj=resultClass(window)
    window.mainloop()
