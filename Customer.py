from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk 
import random
import mysql.connector # type: ignore #pip install pillow
from tkinter import messagebox

class Cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1039x410+232+228") 

       #=============variables==========
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        

        self.var_cust_name=StringVar()
        self.var_guardian=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
       # ======= Title Label ========
        lbl_title = Label(
            self.root,
            text=" ADD  CUSTOMER  DETAILS ",
            font=("Lucida Handwriting", 20, "bold"),
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
                          text="Customer Details", 
                          font=("Lucida Handwriting", 10, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=340, height=370)

       # ===========labels and entrys ================ 
       # Common style for all labels
        label_style = {"font": ("Lucida Handwriting", 9, "bold"), "padx": 2, "pady": 3}
        entry_style = {"font": ("arial", 9), "width": 24}  # Reduced from 29 to fit better
        combobox_style = {"font": ("arial", 9), "width": 22, "state": "readonly"}

        # custRef
        lbl_cust_ref = Label(labelframeleft, text="Customer Reference", **label_style)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        enty_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref, **entry_style,state="readonly")
        enty_ref.grid(row=0, column=1, pady=3)

        # custname
        cname = Label(labelframeleft, text="Customer Name:", **label_style)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name, **entry_style)
        txtcname.grid(row=1, column=1, pady=3)

        # guardian name
        lblmname = Label(labelframeleft, text="Guardian's Name:", **label_style)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_guardian ,**entry_style)
        txtmname.grid(row=2, column=1, pady=3)

        # gender combobox
        label_gender = Label(labelframeleft, text="Gender:", **label_style)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender, **combobox_style)
        combo_gender["values"] = ("Male", "Female", "Others")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1, pady=3)

        # postcode
        lblPostCode = Label(labelframeleft, text="PostCode:", **label_style)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft,textvariable=self.var_post, **entry_style)
        txtPostCode.grid(row=4, column=1, pady=3)

        # mobilenumber
        lblMobile = Label(labelframeleft, text="Mobile Number:", **label_style)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, **entry_style)
        txtMobile.grid(row=5, column=1, pady=3)

        # email
        lblEmail = Label(labelframeleft, text="Email:", **label_style)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email, **entry_style)
        txtEmail.grid(row=6, column=1, pady=3)

        # nationality
        lblNationality = Label(labelframeleft, text="Nationality:", **label_style)
        lblNationality.grid(row=7, column=0, sticky=W)
        combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality,**combobox_style)
        combo_Nationality["values"] = ( "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
        "Antigua and Barbuda", "Argentina", "Armenia", "Australia", 
        "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", 
        "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", 
        "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
        "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Côte d'Ivoire", 
        "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", 
        "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", 
        "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", 
        "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", 
        "Dominican Republic", "Ecuador", "Egypt", "El Salvador", 
        "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (fmr. Swaziland)", 
        "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", 
        "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", 
        "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", 
        "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", 
        "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", 
        "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", 
        "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", 
        "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", 
        "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", 
        "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", 
        "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", 
        "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine State", 
        "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", 
        "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", 
        "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",  "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", 
        "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", 
        "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", 
        "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", 
        "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", 
        "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
        "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", 
        "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", 
        "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe", "Other"
        )
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1, pady=3)

        # idproof type combobox
        lblIdProof = Label(labelframeleft, text="ID Proof Type:", **label_style)
        lblIdProof.grid(row=8, column=0, sticky=W)
        combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, **combobox_style)
        combo_id["values"] = ("National ID", "Driving license", "Passport")
        combo_id.current(0)
        combo_id.grid(row=8, column=1, pady=3)

        # id number
        lblIdNumber = Label(labelframeleft, text="ID Number:", **label_style)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number,**entry_style)
        txtIdNumber.grid(row=9, column=1, pady=3)

        # address
        lblAddress = Label(labelframeleft, text="Address:", **label_style)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft,textvariable=self.var_address, **entry_style)
        txtAddress.grid(row=10, column=1, pady=3)

        
        #==============btns=================
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=305,width=330,height=40)

        btnAdd = Button(btn_frame,text="Add",command=self.add_data,font=("arial", 11, "bold"),fg="#f2f2f1",bg="#17899F",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame,text="Update",command=self.update,font=("arial", 11, "bold"),fg="#f2f2f1",bg="#17899F",width=8,padx=1)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete = Button(btn_frame,text="Delete",command=self.mDelete,font=("arial", 11, "bold"),fg="#f2f2f1",bg="#17899F",width=8,padx=1)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset = Button(btn_frame,text="Reset",command=self.reset,font=("arial", 11, "bold"),fg="#f2f2f1",bg="#17899F",width=7,padx=1)
        btnReset.grid(row=0,column=3,padx=1)
    #===============table frame search system =========== 
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("Lucida Handwriting", 10, "bold"),padx=2)
        Table_Frame.place(x=360,y=50,width=680,height=370)
       
        lblSearchBy=Label( Table_Frame,font=("arial", 10, "bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)  
         
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",10,"bold"),width=24,state="readonly") 
        combo_Search["value"]=("Mobile","Ref")
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
        details_table.place(x=0,y=50,width=660,height=295)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","guardian","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Ref No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("guardian",text="Guardian's Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings" 

        self.Cust_Details_Table.column("ref",width = 70)
        self.Cust_Details_Table.column("name",width = 70)
        self.Cust_Details_Table.column("guardian",width =70)
        self.Cust_Details_Table.column("gender",width =70)
        self.Cust_Details_Table.column("post",width = 70)
        self.Cust_Details_Table.column("mobile",width =70)
        self.Cust_Details_Table.column("email",width = 70)
        self.Cust_Details_Table.column("nationality",width =70)
        self.Cust_Details_Table.column("idproof",width = 70)
        self.Cust_Details_Table.column("idnumber",width = 70)
        self.Cust_Details_Table.column("address",width = 70)



        self.Cust_Details_Table.pack(fill=BOTH,expand=1) 
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_guardian.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("Insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(   
                                                            self.var_ref.get(),
                                                            self.var_cust_name.get(),
                                                            self.var_guardian.get(),
                                                            self.var_gender.get(),
                                                            self.var_post.get(),
                                                            self.var_mobile.get(),
                                                            self.var_email.get(),
                                                            self.var_nationality.get(),
                                                            self.var_id_proof.get(),
                                                            self.var_id_number.get(),
                                                            self.var_address.get()

                                                             )) 
               conn.commit() 
               self.fetch_data()
               conn.close()

               messagebox.showinfo("Success","Customer has been Added Successfully",parent=self.root)
            except Exception as es:
               messagebox.showwarning("Warning","Some thing went wrong:{str(es)}",parent=self.root)
    def fetch_data(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("select * from customer")
              rows=my_cursor.fetchall()
              if len(rows)!=0:
                  self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                  for i in rows:
                      self.Cust_Details_Table.insert("",END,values=i)
                  conn.commit()
              conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"] 

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_guardian.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
        
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,guardian=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(
                                                                                                                                                                      
                                                                                            self.var_cust_name.get(),
                                                                                            self.var_guardian.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_post.get(),
                                                                                            self.var_mobile.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_nationality.get(),
                                                                                            self.var_id_proof.get(),
                                                                                            self.var_id_number.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_ref.get()
            
                                                                                                                                                                                                ))



        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer details has been Updated Successfully",parent=self.root)
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to Delete this Customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
            my_cursor=conn.cursor() 
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return    
        
        conn.commit()
        self.fetch_data()
        conn.close()
   
    def reset(self):
           # self.var_ref.set(""),
            self.var_cust_name.set(""),
            self.var_guardian.set(""),
           # self.var_gender.set(""),
            self.var_post.set(""),
            self.var_mobile.set(""),
            self.var_email.set(""),
          #  self.var_nationality.set(""),
          #  self.var_id_proof.set(""),
            self.var_id_number.set(""),
            self.var_address.set("")
           
            x=random.randint(1000,9999)
            self.var_ref.set(str(x)) 


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
        my_cursor=conn.cursor() 

        query="select * from customer where "+str(self.search_var.get())+" LIKE %s"
        value=("%"+str(self.txt_search.get())+"%",)
        my_cursor.execute(query , value) 
        rows=my_cursor.fetchall()
        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
        if len(rows)!=0:
            
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit() 
        conn.close()    
    
if __name__ == "__main__":
    root = Tk()
    obj = Cust_win(root)
    root.mainloop()
  
