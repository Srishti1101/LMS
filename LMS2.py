from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

#defining login function
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      if uname=="admin123" and pwd=="pass123":
       message.set("Login success")
      else:
       message.set("Wrong username or password!!!")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Login Form")
    #setting height and width of screen
    login_screen.geometry("300x250")
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(login_screen, text="Username * ").place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    #Password Label
    Label(login_screen, text="Password * ").place(x=20,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
    login_screen.mainloop()
#calling function Loginform
Loginform()

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        
        # ================================================ variable ===================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        # ===============================================Data Frame Left======================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        lblmember=Label(DataFrameLeft,bg="powder blue",textvariable=self.member_var,text="Member Type",font=("arial",15,"bold"),padx=2,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        lblPRN_No=Label(DataFrameLeft,bg="powder blue",text="PRN No:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=ttk.Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)
        validate_PRN_No=self.root.register(self.checkprnno)
        txtPRN_No.config(validate='key',validatecommand=(validate_PRN_No,'%P'))
        lblID_No=Label(DataFrameLeft,bg="powder blue",text="ID NO:",font=("arial",12,"bold"),padx=2,pady=6)
        lblID_No.grid(row=2,column=0,sticky=W)
        txtID_No=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtID_No.grid(row=2,column=1)        
        validate_ID_No=self.root.register(self.checkidno)
        txtID_No.config(validate='key',validatecommand=(validate_ID_No,'%P'))
        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName:",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        validate_FirstName=self.root.register(self.checkfirstname)
        txtFirstName.config(validate='key',validatecommand=(validate_FirstName,'%P'))
        lblLastName=Label(DataFrameLeft,bg="powder blue",text="LastName:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)       
        validate_LastName=self.root.register(self.checklastname)
        txtLastName.config(validate='key',validatecommand=(validate_LastName,'%P'))
        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)        
        validate_PostCode=self.root.register(self.checkpostid)
        txtPostCode.config(validate='key',validatecommand=(validate_PostCode,'%P'))
        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)        
        validate_Mobile=self.root.register(self.checkmobile)
        txtMobile.config(validate='key',validatecommand=(validate_Mobile,'%P'))
        lblBookID=Label(DataFrameLeft,bg="powder blue",text="Book ID:",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookID.grid(row=0,column=3)
        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)
        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Author:",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)
        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)
        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)
        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)
        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)
        lblDateOverdue=Label(DataFrameLeft,bg="powder blue",text="Date Overdue:",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverdue.grid(row=7,column=2,sticky=W)
        txtDateOverdue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverdue.grid(row=7,column=3)
        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)
   
          # =============================================== Data Frame Right======================================================
        DataFrameRight=LabelFrame(frame,bd=12,padx=20,relief=RIDGE,bg="powder blue",font=("arial",12,"bold"),text="Book Details")
        DataFrameRight.place(x=870,y=5,width=580,height=350)
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        listBooks=['Head First Book','Python Programming','Learn Python The Hard Way','Secret Rahsya','Python CookBook','Machine Techno','My Python','Joss Ellif Guru','Elite Jungle Python','Jungli Python','Machine Python','Advance Python','Inton Python','Redchilli Python','Business And Management','Engineering Chemistry','Engineering Physics','Engineering Maths','Probability And Statistics','General Knowledge','Fantastic Beast And Crimes Of Grindelwald','Harry Pottter Novels','Fantastic Beats And Where To Find Them','Spiderman Into Spiderverse','The Mighty Thor']
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Pual Berry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")
            
            elif (x=="Python Programming"):
                self.bookid_var.set("SKY0701")
                self.booktitle_var.set("Python Learning")
                self.author_var.set("Sam Potter")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.23")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.786")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("JKDF5634")
                self.booktitle_var.set("Hard Learning")
                self.author_var.set("Ron Weaseley")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.45")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.755")

            elif (x=="Secret Rahsya"):
                self.bookid_var.set("GOVID1988")
                self.booktitle_var.set("Finding")
                self.author_var.set("Albus Yadav")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.37")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.700")

            elif (x=="Python CookBook"):
                self.bookid_var.set("NAND1975")
                self.booktitle_var.set("Cook Pyhton")
                self.author_var.set("ND Raman")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.39")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.719")

            elif (x=="Machine Techno"):
                self.bookid_var.set("STAR1989")
                self.booktitle_var.set("Technology")
                self.author_var.set("Tara Stark")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.42")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.979")

            elif (x=="My Python"):
                self.bookid_var.set("SRIS2002")
                self.booktitle_var.set("Monthly Learning")
                self.author_var.set("Tom Riddle")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.33")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.777")

            elif (x=="Joss Ellif Guru"):
                self.bookid_var.set("AMAN1998")
                self.booktitle_var.set("Guru ji")
                self.author_var.set("AMAN KING")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.22")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.798")

            elif (x=="Elite Jungle Python"):
                self.bookid_var.set("REDY2501")
                self.booktitle_var.set("Jungle Book")
                self.author_var.set("Red Dumbledore")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.14")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.210")

            elif (x=="Jungli Python"):
                self.bookid_var.set("BKID4501")
                self.booktitle_var.set("Python")
                self.author_var.set("Josaph")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.600")

            elif (x=="Machine Python"):
                self.bookid_var.set("GODY0105")
                self.booktitle_var.set("Pyhton Structure")
                self.author_var.set("Nevel Longbottom")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.38")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.370")

            elif (x=="Advance Python"):
                self.bookid_var.set("GOTM1508")
                self.booktitle_var.set(" Update Pyhton")
                self.author_var.set("Nody Roggers")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.42")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.470")

            elif (x=="Inton Python"):
                self.bookid_var.set("VOLD7001")
                self.booktitle_var.set("Intro Of Python")
                self.author_var.set("Harry Potter")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.28")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.450")

            elif (x=="Redchilli Python"):
                self.bookid_var.set("ALBS7201")
                self.booktitle_var.set("Redchilli Snape")
                self.author_var.set("Sevrous Snape")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.49")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.500")

            elif (x=="Business And Management"):
                self.bookid_var.set("NUDE7856")
                self.booktitle_var.set("Fantastic Idea")
                self.author_var.set("Lilly Jackson")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.39")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.510")

            elif (x=="Engineering Chemistry"):
                self.bookid_var.set("KFKI5665")
                self.booktitle_var.set("Chemical Reaction")
                self.author_var.set("Loki Odinson")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.41")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.610")

            elif (x=="Engineering Physics"):
                self.bookid_var.set("CHKB5675")
                self.booktitle_var.set("Current Electricity")
                self.author_var.set("Pradeep")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.40")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.450")

            elif (x=="Engineering Maths"):
                self.bookid_var.set("SDER5432")
                self.booktitle_var.set("Matrices")
                self.author_var.set("Shilpa Aggarwal")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.30")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.430")

            elif (x=="Probability And Statistics"):
                self.bookid_var.set("XCFD8705")
                self.booktitle_var.set("Probability And Statistics")
                self.author_var.set("B.S. Grewal")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.31")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.320")

            elif (x=="General Knowledge"):
                self.bookid_var.set("SWQE5902")
                self.booktitle_var.set("World")
                self.author_var.set("Pooja Malik")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.210")
            
            elif (x=="Fantastic Beast And Crimes Of Grindelwald"):
                self.bookid_var.set("KXCF6509")
                self.booktitle_var.set("Fantastic Beats")
                self.author_var.set("Dhanpat Rai")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.15")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.470")

            elif (x=="Harry Pottter Novels"):
                self.bookid_var.set("SDER8965")
                self.booktitle_var.set("Harry Potter")
                self.author_var.set("Sai")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.430")

            elif (x=="Fantastic Beats And Where To Find Them"):
                self.bookid_var.set("ASDE3421")
                self.booktitle_var.set("Fantastic Beats Search")
                self.author_var.set("Mukesh Pal")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.35")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.405")

            elif (x=="Spiderman Into Spiderverse"):
                self.bookid_var.set("KFHG6265")
                self.booktitle_var.set("Spiderman Into Spiderverse")
                self.author_var.set("John Keats")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.45")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.320")

            elif (x=="The Mighty Thor"):
                self.bookid_var.set("KSEV6098")
                self.booktitle_var.set("The Mighty Thor")
                self.author_var.set("Keshav Kumar")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.21")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.210")

        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)
                
        for item in listBooks:
            listBox.insert(END,item)

        # ================================================Buttons Frame========================================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=60)        
        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)
        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)
        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)
        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)
        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
                
        #=================================================Information Frame====================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=590,width=1530,height=210)
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)      
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","idno","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll,yscrollcommand=yscroll)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("idno",text="ID No.")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Overdue")
        self.library_table.heading("finalprice",text="Final Price")
       
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("idno",width=100) 
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def checkprnno(self,prnno):
        if prnno.isdigit():
           return True
        if len(str(prnno))==0:
            return True
        else:
           messagebox.showerror("Invalid,it can't be alphabet!")
           return False
    
    def checkidno(self,idno):
        if idno.isdigit():
           return True
        if len(str(idno))==0:
           return True
        else:
           messagebox.showerror("Invalid,it can't be alphabet!")
           return False

    def checkfirstname(self,firstname):
        if firstname.isalpha():
           return True
        if firstname=='':
           return True
        else:
           messagebox.showerror("Invalid,it should be alphabet!")
           return False
     
    def checklastname(self,lastname):
        if lastname.isalpha():
           return True
        if lastname=='':
           return True
        else:
           messagebox.showerror("Invalid,it should be alphabet!")
           return False
    
    def checkpostid(self,postid):
        if postid.isdigit():
           return True
        if len(str(postid))==0:
           return True
        else:
           messagebox.showerror("Invalid,it can't be alphabet!")
           return False
 
    def checkmobile(self,mobile):
        if mobile.isdigit():
           return True
        if len(str(mobile))==0:
           return True
        else:
           messagebox.showerror("Invalid,it can't be alphabet!")
           return False

    
    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="11012301@Ss",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                            self.member_var.get(),
                                                                                                            self.prn_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.dateoverdue_var.get(),
                                                                                                            self.finalprice_var.get()
                                                                                                          ))
        conn.commit()
        self.fatch_data()         
        conn.close()        
        messagebox.showinfo("Success","Member Has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="11012301@Ss",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Postid=%s,Mobile=%s,Bookid=%s,Booktitle=%s,Author=%s,Dateborrowed=%s,Datedue=%s,daysofbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_NO=%s",(
                                                                                                            
                                                                                                            self.member_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address1_var.get(),
                                                                                                            self.address2_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.dateoverdue_var.get(),
                                                                                                            self.finalprice_var.get(),
                                                                                                            self.prn_var.get()                                                                                                         
                                                                                                                                                             ))    
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member Has been Updated successfully")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="11012301@Ss",database="sys")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="11012301@Ss",database="sys")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Member Has been Deleted successfully")

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()