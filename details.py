from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk 
import random 
from time import strftime
from datetime import datetime
import mysql.connector # type: ignore #pip install pillow
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1039x410+232+228")  
 
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
                          text="Adding New Room", 
                          font=("arial", 10, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=340, height=210)

     # ===========labels and entrys ================
       
      # Floor
        lbl_floor= Label(labelframeleft, text="Floor",font=("Lucida Calligraphy",9,"bold"),padx=2,pady=3)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()
        enty_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("Lucida Calligraphy",9,"bold"), width=21)
        enty_floor.grid(row=0, column=1,sticky=W) 
   
       # Room No
        lbl_RoomNo= Label(labelframeleft, text="Room_Number",font=("Lucida Calligraphy",9,"bold"),padx=2,pady=3)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_roomno=StringVar()
        enty_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_roomno,font=("Lucida Calligraphy",9,"bold"), width=21)
        enty_RoomNo.grid(row=1, column=1,sticky=W) 

        # Room Type
        lbl_RoomType= Label(labelframeleft, text="Room_Type",font=("Lucida Calligraphy",9,"bold"),padx=2,pady=3)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_roomtype=StringVar()
        enty_RoomType= ttk.Entry(labelframeleft,textvariable=self.var_roomtype,font=("Lucida Calligraphy",9,"bold"), width=21)
        enty_RoomType.grid(row=2, column=1,sticky=W) 


      #=============btns======
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=147,width=330,height=40)

        btnAdd = Button(btn_frame,text="Add",command=self.add_data,font=("arial", 11, "bold"),bg="#17899F",fg="#f2f2f1",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame,text="Update",command=self.update,font=("arial", 11, "bold"),bg="#17899F",fg="#f2f2f1",width=8,padx=1)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete = Button(btn_frame,text="Delete",command=self.mDelete,font=("arial", 11, "bold"),bg="#17899F",fg="#f2f2f1",width=8,padx=1)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset = Button(btn_frame,text="Reset",command=self.reset_data,font=("arial", 11, "bold"),bg="#17899F",fg="#f2f2f1",width=7,padx=1)
        btnReset.grid(row=0,column=3,padx=1)


   #===============table frame search system =========== 

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial", 10, "bold"),padx=2)
        Table_Frame.place(x=350,y=50,width=685,height=210)
    
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview) 
        
        self.room_table.heading("floor",text="floor")
        self.room_table.heading("roomno",text="roomno")
        self.room_table.heading("roomtype",text="roomtype")
        

        self.room_table["show"]="headings" 

        self.room_table.column("floor",width = 70)
        self.room_table.column("roomno",width = 70)
        self.room_table.column("roomtype",width =70)
          
        self.room_table.pack(fill=BOTH,expand=1) 
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

 #======add data ====
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
               my_cursor=conn.cursor()
               my_cursor.execute("Insert into details values(%s,%s,%s)",(   
                                                            self.var_floor.get(),
                                                            self.var_roomno.get(),
                                                            self.var_roomtype.get()
                                                            
                                                            
                                                             )) 
               conn.commit() 
               self.fetch_data()
               conn.close() 
              

               messagebox.showinfo("Success","New Room has been Added Successfully",parent=self.root)
            except Exception as es:
               messagebox.showwarning("Warning","Some thing went wrong:{str(es)}",parent=self.root) 
       

  #======fetch data =====

    def fetch_data(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("select * from details")
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
        
        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])    

# ======update function ========

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Floor Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,roomtype=%s where roomno=%s",(
                                                                                                                                                                      
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomno.get()
                                                                                            
                                                                                        
                                                                                                                  ))
                                                                                            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update"," New Room details has been Updated Successfully",parent=self.root)    
   

  #======== delete =========
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="@sadia2003@",database="management")
            my_cursor=conn.cursor() 
            query="delete from details where roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()    
        self.fetch_data()
        conn.close()  

    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")

if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
         