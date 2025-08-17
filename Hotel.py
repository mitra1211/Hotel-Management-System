from tkinter import *
from PIL import Image, ImageTk
from Customer import Cust_win 
from Room import Roombooking 
from details import DetailsRoom

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
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()