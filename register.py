from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox 
import mysql.connector # type: ignore #pip install pillow

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1500x800+0+0") 

        #============variables =============

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        #  =====Load and resize the  bg image======
        original_image = Image.open("E:/Hotel Management System (DBMS)/register1.jpg")
        resized_image = original_image.resize((1500, 800), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(resized_image)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, width=1485, height=785)

# ========== left img ===================
        self.bg1=ImageTk.PhotoImage(file="E:/Hotel Management System (DBMS)/register2.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=90,y=100,width=400,height=500)

 #========== main frame ==================       
        frame=Frame(self.root,bg="white")
        frame.place(x=490,y=100,width=680,height=500) 

        register_lbl=Label(frame,text="REGISTER HERE",font=("Lucida Calligraphy",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=210,y=20) 


        # ==== First Name ====
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=80)

        self.fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 15))
        self.fname_entry.place(x=50, y=110, width=200)

        # ==== Last Name ====
        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=350, y=80)

        self.lname_entry = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15))
        self.lname_entry.place(x=350, y=110, width=200)
       # ============contact and email ========

        contact= Label(frame, text="Contact Number", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=160)

        self.txt_contact= ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman", 15))
        self.txt_contact.place(x=50, y=190, width=200)

        email= Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=350, y=160)

        self.txt_email= ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=350, y=190, width=200)

      #===============security ==================
        security_Q= Label(frame, text="Select Security Question ", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=240) 

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend's Name","Your pet's Name")
        self.combo_security_Q.place(x=50,y=270,width=200)
        self.combo_security_Q.current(0)


        security_A=Label(frame, text="Security Answer ", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=350, y=240)

        self.txt_security= ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15))
        self.txt_security.place(x=350, y=270, width=200)

     #=============== pass ====================
        pswd= Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white") 
        pswd.place(x=50, y=310)

        self.txt_pswd= ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=200)

        confirm_pswd= Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=350, y=310)

        self.txt_confirm_pswd= ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=350, y=340, width=200)


  #================ check btn ============
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree with terms and conditions",font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=385)
   
  #===============buttons==========
        img=Image.open("E:/Hotel Management System (DBMS)/Regbtn.jpg")
        img=img.resize((80,40),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=425,width=150)
    
        img1=Image.open("E:/Hotel Management System (DBMS)/Reg2btn.jpg")
        img1=img1.resize((80,40),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=360,y=425,width=150)  

    #=========== Function declaration==========
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree with our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
            my_cursor=conn.cursor()
            query="select * from register where email=%s"
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row !=None:
                messagebox.showerror("Error","User already exist,Please try with another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(   
                                                            self.var_fname.get(),
                                                            self.var_lname.get(),
                                                            self.var_contact.get(),
                                                            self.var_email.get(),
                                                            self.var_securityQ.get(),
                                                            self.var_securityA.get(),
                                                            self.var_pass.get(),
                                                            
                                                    ))       
            conn.commit() 
            conn.close() 
            messagebox.showinfo("Congratulations!","Registration Successful")

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
