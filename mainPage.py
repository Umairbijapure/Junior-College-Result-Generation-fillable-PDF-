from tkinter import *
from PIL import Image,ImageTk
from test5 import SSA
class standardClass:
    def __init__(self,window):
        self.window=window
        self.window.title("SSA Result Management System")
        self.window.geometry("1500x800+60+60")
        self.window.config(bg="white")
        # ICONS
        img = (Image.open("logo.png"))
        resized_image = img.resize((60, 60))
        self.logo_dash = ImageTk.PhotoImage(resized_image)
        # Image
            #self.image1 = Image.open("SSA3.jpg")
            #self.image1 = self.image1.resize((920, 350), Image.ANTIALIAS)
            #self.image1 = ImageTk.PhotoImage(self.image1)
            #self.label_image1 = Label(self.window, image=self.image1).place(x=370, y=77, width=600, height=500)
        #footer
        title = Label(self.window,text="SSA Result Management System\nContact US for any technical issue:Umer Bijapure-7020152273",font=("goudy old stlye", 10), bg="#87CEFA", fg="White").pack(side=BOTTOM, fill=X)
        #widgets
        title = Label(self.window, text="SSA Result Management System", padx=10, compound=LEFT, image=self.logo_dash,font=("goudy old stlye", 20, "bold"), bg="#87CEFA", fg="White").place(x=0, y=0, relwidth=1,height=50)
        btn_std = Button(self.window, text="Class A", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.std11).place(x=160, y=170, width=170, height=35)
        btn_std = Button(self.window, text="Class B", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.std11).place(x=340, y=170, width=170, height=35)
        btn_std = Button(self.window, text="Class C", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.std11).place(x=520, y=170, width=170, height=35)
        btn_std = Button(self.window, text="Class A", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.std12).place(x=160, y=370, width=170, height=35)
        btn_std = Button(self.window, text="Class B", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.std12).place(x=340, y=370, width=170, height=35)
        btn_std = Button(self.window, text="Class C", font=("goudym old style", 15), bg="#0b5377", fg="white",cursor="hand2", command=self.std12).place(x=520, y=370, width=170, height=35)
        self.label_student = Label(self.window, text="Standard 11th:", font=("goudy old style", 16), bd=10)
        self.label_student.place(x=10, y=170, width=150, height=35)
        self.label_student = Label(self.window, text="Standard 12th:", font=("goudy old style", 16), bd=10)
        self.label_student.place(x=10, y=370, width=150, height=35)
    def std11(self):
        self.new_win=Toplevel(self.window)
        self.obj1=SSA(self.new_win)
    def std12(self):
        self.new_win=Toplevel(self.window)
        self.obj2=SSA(self.new_win)
if __name__=="__main__":
    window=Tk()
    obj=standardClass(window)
    window.mainloop()
