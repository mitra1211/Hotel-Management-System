from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk 
import random
from time import strftime
from datetime import datetime
import mysql.connector # type: ignore #pip install pillow
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1039x410+232+228") 

        #============variable=====
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

         # ======= Title Label ========
        lbl_title = Label(
            self.root,
            text=" ROOM  BOOKING   DETAILS",
            font=("Lucida Calligraphy", 20, "bold"),
            bg="#17899F",
            fg="#f2f2f1",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=0, width=1039, height=50)
        
        # ======= Logo Image (images.jpeg) ========
        
        img2 = Image.open("E:/Hotel Management System (DBMS)/logof.jpg")
        img2 = img2.resize((100, 47), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=0, y=2, width=100, height=47)  

         # ===========labelFrame====================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, 
                        text="Room Booking Details", 
                        font=("arial", 10, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=360, height=370) 

        # ===========labels and entrys ================ 
        # custcontact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=("Lucida Calligraphy", 9, "bold"), padx=2, pady=3)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, font=("Lucida Calligraphy", 9), width=26)
        enty_contact.grid(row=0, column=1, sticky=W) 

        # FETCH data btn
        btnFetchData = Button(labelframeleft, command=self.fetch_contact, text="Fetch Data", 
                            font=("arial", 7, "bold"), bg="red", fg="#f2f2f1", width=8)
        btnFetchData.place(x=290, y=3)

        # Check_in_date
        check_in_date = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), text="Check_In Date:", padx=2, pady=3)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, font=("Lucida Calligraphy", 9), width=20)
        txtcheck_in_date.grid(row=1, column=1, sticky=W)

        # Check_out_date
        lbl_Check_out = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), text="Check_Out Date:", padx=2, pady=3)
        lbl_Check_out.grid(row=2, column=0, sticky=W)
        txt_Check_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=("Lucida Calligraphy", 9), width=20)
        txt_Check_out.grid(row=2, column=1, sticky=W)

        # Room type
        label_RoomType = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), text="Room Type:", padx=2, pady=3)
        label_RoomType.grid(row=3, column=0, sticky=W) 

        conn = mysql.connector.connect(host="localhost", username="root", password="@sadia2003@", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomtype from details")
        ide = [row[0] for row in my_cursor.fetchall()]

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, 
                                    font=("Lucida Calligraphy", 9), width=18, state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1, sticky=W)

        # Available room
        lblRoomAvailable = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), 
                                text="Room_Number:", padx=2, pady=3)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="@sadia2003@", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from details")
        rows = my_cursor.fetchall()

        combo_Room_Number = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, 
                                        font=("Lucida Calligraphy", 9), width=18, state="readonly")
        combo_Room_Number["value"] = rows
        combo_Room_Number.current(0)
        combo_Room_Number.grid(row=4, column=1, sticky=W)

        # Meal
        lblMeal = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), text="Meal:", padx=2, pady=3)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=("Lucida Calligraphy", 9), width=20)
        txtMeal.grid(row=5, column=1, sticky=W)

        # No of Days
        lblNoOfDays = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), text="No of Days:", padx=2, pady=3)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, font=("Lucida Calligraphy", 9), width=20)
        txtNoOfDays.grid(row=6, column=1, sticky=W)

        # Paid tax
        lblPaidTax = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), text="Paid Tax:", padx=2, pady=3)
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=("Lucida Calligraphy", 9), width=20)
        txtPaidTax.grid(row=7, column=1, sticky=W)

        # Sub Total
        lblSubTotal = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), text="Sub Total:", padx=2, pady=3)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, font=("Lucida Calligraphy", 9), width=20)
        txtSubTotal.grid(row=8, column=1, sticky=W)

        # Total Cost
        lblTotalCost = Label(labelframeleft, font=("Lucida Calligraphy", 9, "bold"), text="Total Cost:", padx=2, pady=3)
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(labelframeleft, textvariable=self.var_total, font=("Lucida Calligraphy", 9), width=20)
        txtTotalCost.grid(row=9, column=1, sticky=W)
        #======Bill btn=========
        btnBill = Button(labelframeleft,text="Bill",command=self.total,font=("Lucida Calligraphy", 10, "bold"),bg="#17899F",fg="#f2f2f1",width=8)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

 
       #=============btns======
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=305,width=330,height=40)

        btnAdd = Button(btn_frame,text="Add",command=self.add_data,font=("arial", 11, "bold"),bg="#17899F",fg="#f2f2f1",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame,text="Update",command=self.update,font=("arial", 11, "bold"),bg="#17899F",fg="#f2f2f1",width=8,padx=1)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete = Button(btn_frame,text="Delete",command=self.mDelete,font=("arial", 11, "bold"),bg="#17899F",fg="#f2f2f1",width=8,padx=1)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset = Button(btn_frame,text="Reset",command=self.reset,font=("arial", 11, "bold"),bg="#17899F",fg="#f2f2f1",width=7,padx=1)
        btnReset.grid(row=0,column=3,padx=1) 

    #=========Rightside image ============
        img3 = Image.open("E:/Hotel Management System (DBMS)/room.jpeg")
        img3 = img3.resize((683, 170), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=370, y=49,width=670, height=190)


     #===============table frame search system =========== 
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial", 10, "bold"),padx=2)
        Table_Frame.place(x=370,y=210,width=670,height=210)
       
        lblSearchBy=Label( Table_Frame,font=("arial", 10, "bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)  
         
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",10,"bold"),width=24,state="readonly") 
        combo_Search["value"]=("contact","room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2) 

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial", 10, "bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2) 

        btnSearch = Button(Table_Frame,text="Search",command=self.search,font=("arial", 9, "bold"),bg="#17899F",fg="#f2f2f1",width=11)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll = Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial", 9, "bold"),bg="#17899F",fg="#f2f2f1",width=11,padx=1)
        btnShowAll.grid(row=0,column=4,padx=1) 

        #=============== Show data Table ===========
      
        details_table = Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=660,height=135)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","room","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="contact")
        self.room_table.heading("checkin",text="checkin")
        self.room_table.heading("checkout",text="checkout")
        self.room_table.heading("roomtype",text="roomtype")
        self.room_table.heading("room",text="room")
        self.room_table.heading("meal",text="meal")
        self.room_table.heading("noofdays",text="noofdays")
        

        self.room_table["show"]="headings" 

        self.room_table.column("contact",width = 70)
        self.room_table.column("checkin",width = 70)
        self.room_table.column("checkout",width =70)
        self.room_table.column("roomtype",width =70)
        self.room_table.column("room",width = 70)
        self.room_table.column("meal",width =70)
        self.room_table.column("noofdays",width = 70)  
        self.room_table.pack(fill=BOTH,expand=1) 
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
 
 #======add data ====
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("Insert into room values(%s,%s,%s,%s,%s,%s,%s)",(   
                                                            self.var_contact.get(),
                                                            self.var_checkin.get(),
                                                            self.var_checkout.get(),
                                                            self.var_roomtype.get(),
                                                            self.var_roomavailable.get(),
                                                            self.var_meal.get(),
                                                            self.var_noofdays.get()
                                                            
                                                             )) 
               conn.commit() 
               self.fetch_data()
               conn.close()

               messagebox.showinfo("Success","Room has been Added Successfully",parent=self.root)
            except Exception as es:
               messagebox.showwarning("Warning","Some thing went wrong:{str(es)}",parent=self.root) 

     #======fetch data =====

    def fetch_data(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("select * from room")
              rows=my_cursor.fetchall()
              if len(rows)!=0:
                  self.room_table.delete(*self.room_table.get_children())
                  for i in rows:
                      self.room_table.insert("",END,values=i)
                  conn.commit()
              conn.close() 
     
     #======get cursor=====

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"] 
        
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])  
    
    # ======update function ========

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,room=%s,meal=%s,noofdays=%s where contact=%s",(
                                                                                                                                                                      
                                                                                            self.var_checkin.get(),
                                                                                            self.var_checkout.get(),
                                                                                            self.var_roomtype.get(),
                                                                                            self.var_roomavailable.get(),
                                                                                            self.var_meal.get(),
                                                                                            self.var_noofdays.get(),
                                                                                            self.var_contact.get()
                                                                                        
                                                                                                                  ))
                                                                                            
                                                                                            
                                                                                                           

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been Updated Successfully",parent=self.root)    
   
   #======== delete =========
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to Delete this Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
            my_cursor=conn.cursor() 
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return    
        
        conn.commit()
        self.fetch_data()
        conn.close()  

    #======== reset ============
  
    def reset(self):
     self.var_contact.set(""),
     self.var_checkin.set(""),
     self.var_checkout.set(""),
     self.var_roomtype.set(""),
     self.var_roomavailable.set(""),
     self.var_meal.set(""),
     self.var_noofdays.set("") 
     self.var_paidtax.set("")
     self.var_actualtotal.set("")
     self.var_total.set("")

     
            

     #==========All Data Fetch ================ 
           
    def fetch_contact(self):
      if self.var_contact.get()=="":
          messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
      else:    
        conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
        my_cursor=conn.cursor()
        query="select name from customer where mobile=%s"
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        if row==None:
           messagebox.showerror("Error","This Number is Not Found",parent=self.root)
        else:
           conn.commit()
           conn.close() 

           showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
           showDataframe.place(x=347,y=60,width=240,height=150)   

           lblName=Label(showDataframe,text="Name:",font=("arial",9,"bold")) 
           lblName.place(x=0,y=0)       

           lbl=Label(showDataframe,text=row,font=("arial",9,"bold"))
           lbl.place(x=60,y=0) 
    #==========Gender==========   
        conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
        my_cursor=conn.cursor()
        query="select gender from customer where mobile=%s"
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone() 

        lblGender=Label(showDataframe,text="Gender:",font=("arial",9,"bold")) 
        lblGender.place(x=0,y=20)       

        lbl2=Label(showDataframe,text=row,font=("arial",9,"bold"))
        lbl2.place(x=60,y=20) 
    #=============email==========
        conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
        my_cursor=conn.cursor()
        query="select email from customer where mobile=%s"
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone() 

        lblemail=Label(showDataframe,text="Email:",font=("arial",9,"bold")) 
        lblemail.place(x=0,y=40)       

        lbl3=Label(showDataframe,text=row,font=("arial",9,"bold"))
        lbl3.place(x=60,y=40) 
    #=============nationality==========
        conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
        my_cursor=conn.cursor()
        query="select nationality from customer where mobile=%s"
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone() 

        lblNationality=Label(showDataframe,text="Nationality:",font=("arial",9,"bold")) 
        lblNationality.place(x=0,y=60)       

        lbl4=Label(showDataframe,text=row,font=("arial",9,"bold"))
        lbl4.place(x=65,y=60)   

    #=============Address==========
        conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
        my_cursor=conn.cursor()
        query="select address from customer where mobile=%s"
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone() 

        lbladdress=Label(showDataframe,text="Address:",font=("arial",9,"bold")) 
        lbladdress.place(x=0,y=80)       

        lbl5=Label(showDataframe,text=row,font=("arial",9,"bold"))
        lbl5.place(x=60,y=80) 
      
        
   
    #====== search system =======

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
        my_cursor=conn.cursor() 

        query="select * from room where "+str(self.search_var.get())+" LIKE %s"
        value=("%"+str(self.txt_search.get())+"%",)
        my_cursor.execute(query , value) 
        rows=my_cursor.fetchall()
        self.room_table.delete(*self.room_table.get_children())
        if len(rows)!=0:
            
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit() 
        conn.close()   
    #====== Total ===========    

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxurious"):

            q1=float(3000)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):

            q1=float(2000)
            q2=float(350)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):

            q1=float(2000)
            q2=float(400)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
       
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxurious"):

            q1=float(2500)
            q2=float(650)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):

            q1=float(1500)
            q2=float(250)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 

        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):

            q1=float(1000)
            q2=float(250)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):

            q1=float(4000)
            q2=float(350)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):

            q1=float(2500)
            q2=float(450)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxurious"):

            q1=float(4500)
            q2=float(850)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)




if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()