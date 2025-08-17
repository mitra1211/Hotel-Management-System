from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
import mysql.connector  # type: ignore #pip install pillow 
from Hotel import HotelManagementSystem
from Customer import Cust_win 
from Room import Roombooking 
from details import DetailsRoom


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1500x800+0+0")

        self.bg = ImageTk.PhotoImage(file="E:/Hotel Management System (DBMS)/loginf.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="#fefae0")
        frame.place(x=485, y=120, width=340, height=400)

        
        get_str = Label(frame, text="Get Started", font=("Lucida Handwriting", 25, "bold"), fg="#bc6c25", bg="#fefae0")
        get_str.place(x=65, y=40)

        username = Label(frame, text="Username", font=("arial", 12, "bold"), fg="#bc6c25", bg="#fefae0")
        username.place(x=30, y=130)

        self.txtuser = Entry(frame, font=("arial", 16, "bold"), fg="black", bg="white")
        self.txtuser.place(x=10, y=155, width=250)

        password = Label(frame, text="Password", font=("arial", 12, "bold"), fg="#bc6c25", bg="#fefae0")
        password.place(x=30, y=190)

        self.txtpass = Entry(frame, font=("arial",16, "bold"), fg="black", bg="white",show="*")
        self.txtpass.place(x=10, y=215, width=250)

        
        loginbtn = Button(frame, command=self.login, text="Log In", font=("arial", 12, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=125, y=260, width=100, height=30)

        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("arial", 10, "bold"), borderwidth=0, fg="#bc6c25", bg="#fefae0", activeforeground="black", activebackground="white")
        registerbtn.place(x=110, y=310, width=130)

        forgetpassbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("arial", 10, "bold"), borderwidth=0, fg="#bc6c25", bg="#fefae0", activeforeground="black", activebackground="white")
        forgetpassbtn.place(x=110, y=340, width=130)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        elif self.txtuser.get() == "sadia" and self.txtpass.get() == "deep":
            messagebox.showinfo("Success", "Welcome to ROSEVILLE EL GRANDO")
            self.new_window = Toplevel(self.root)
            self.app = HotelManagementSystem(self.new_window)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="@sadia2003@",
                    database="management"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "select * from register where email=%s and password=%s",
                    (self.txtuser.get(), self.txtpass.get())
                )
                row = my_cursor.fetchone()
                #print(row)
                if row == None:
                    messagebox.showerror("Error", "Invalid Username & Password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Access only for Admin")
                    if open_main>0:
                        self.new_window = Toplevel(self.root)
                        self.app = HotelManagementSystem(self.new_window)
                    else:
                        if not open_main:
                            return        
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}")
            finally:
                conn.close() 
    
    #============= reset password ===========
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the Answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password")
        else:
            conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="@sadia2003@",
                    database="management"
                )
            my_cursor = conn.cursor()
            query="select * from register where email=%s and securityQ=%s and securityA=%s"
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer")
            else:
                query="update register set password=%s where email=%s"
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been Reset,Please login New password")
                self.root2.destroy()

    #============ forget pass=================

    def forgot_password_window(self):
            if self.txtuser.get()=="":
                messagebox.showerror("Error","Please Enter the Email address to reset password")
            else:
                conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="@sadia2003@",
                        database="management"
                    )
                my_cursor = conn.cursor()
                query="select * from register where email=%s"
                value=(self.txtuser.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
              

            if row==None:
                messagebox.showerror("Error","Please Enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("450x350+500+200")

                l=Label(self.root2,text="Forget Password",font=("arial", 16, "bold"), fg="red")
                l.place(x=0,y=10,relwidth=1)    

                security_Q= Label(self.root2, text="Select Security Question ", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=70, y=60) 

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend's Name","Your pet's Name")
                self.combo_security_Q.place(x=70,y=90,width=200)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2, text="Security Answer ", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=70, y=130)

                self.txt_security= ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_security.place(x=70, y=160, width=200)
               
                new_password=Label(self.root2, text="New Password ", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=70, y=200)

                self.txt_newpass= ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_newpass.place(x=70, y=230, width=200)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman", 15, "bold"),fg="#f2f2f1",bg="#17899F")
                btn.place(x=170,y=270)

           



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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
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

    def return_login(self):
        self.root.destroy()


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")
       
        # ======= First Image (hotel img.jpg) ========
        img1 = Image.open("E:/Hotel Management System (DBMS)/final2hotel.jpg")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1550, height=140)

        # ======= Logo Image (images.jpeg) ========
        
        img2 = Image.open("E:/Hotel Management System (DBMS)/logof.jpg")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)


        
       # ======= Title Label ========
        lbl_title = Label(
            self.root,
            text="🏖 WELCOME TO OUR RESORT 🏖",
            font=("Lucida Handwriting", 32, "bold"),
            bg="#17899F",
            fg="#f2f2f1",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=140, width=1550, height=50)
       #=========== main frame ===========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

      #==============menu=======================
        lbl_menu = Label(
        main_frame,
        text="MENU",
        font=("Lucida Handwriting", 20, "bold"),
        bg="#f2f2f1",
        fg="#17899F",
        bd=4,
        relief=RIDGE,
        anchor="w",  # Left-align the text
        padx=10     # Add horizontal padding
    )
        lbl_menu.place(x=0, y=0, width=228, height=35)  # Match width with btn_frame and set explicit height

        #=========== btn frame ===========
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=210)  # Frame width = 228 pixels

# Remove width from button options since we'll let them expand
        button_options = {
            "font": ("Lucida Handwriting", 14, "bold"),
            "bg": "#f2f2f1",
            "fg": "#17899F",
            "bd": 0,
            "cursor": "hand1",
            "relief": RIDGE,
            "anchor": "w",  # Align text to the left
            "padx": 10,     # Add some horizontal padding
        }

        # Configure the column to take all available space
        btn_frame.columnconfigure(0, weight=1)

        cust_btn = Button(
            btn_frame,
            text="CUSTOMER",
            command=self.cust_details,
            **button_options
        )
        cust_btn.grid(row=0, column=0, pady=1, sticky="ew")  # Will expand to full width (228px)

        room_btn = Button(
            btn_frame,
            text="ROOM",
            command=self.roombooking_details,
            **button_options
        )
        room_btn.grid(row=1, column=0, pady=1, sticky="ew")

        details_btn = Button(
            btn_frame,
            text="DETAILS",
            command=self.details_room,
            **button_options
        )
        details_btn.grid(row=2, column=0, pady=1, sticky="ew")

        
        logout_btn = Button(
            btn_frame,
            text="LOGOUT",
            command=self.logout,
            **button_options
        )
        logout_btn.grid(row=4, column=0, pady=1, sticky="ew")

     #=========== right side image ================ 
        img3 = Image.open("E:/Hotel Management System (DBMS)/finalhotel.jpg")
        img3 = img3.resize((1160, 436), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1140, height=444)

     #============ down images ==============
        img4 = Image.open("E:/Hotel Management System (DBMS)/downf.jpg")
        img4 = img4.resize((228, 120), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=220, width=228, height=120)
    
   
        img5 = Image.open("E:/Hotel Management System (DBMS)/foodf2.jpg")
        img5 = img5.resize((228, 100), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=335, width=228, height=109)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)
     
    def roombooking_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
   
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
 
    def logout(self):
        self.root.destroy()



if __name__ == "__main__":
    main()
