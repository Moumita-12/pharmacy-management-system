from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:


    def __init__(self,root) :
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")


        #adding  side  variable
        self.addmed_var=StringVar()
        self.refmed_var=StringVar()


        ########## MEDICINE DEPARTMENT VARIABLE #######
        self.refno_var = StringVar()
        self.cmpName_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.product_var = StringVar()



        lbltitle=Label(self.root,text="Pharmacy Management System",bd=15,relief=RIDGE
                                ,bg='black',fg="lightpink",font=("times new roman",50,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)


        img1=Image. open(r"C:\Users\user\Desktop\pharma\toplogo.JPG")
        img1=img1. resize((90,83), Image. ANTIALIAS)
        self. photoimg1 = ImageTk. PhotoImage(img1)
        b1=Button(self. root, image=self. photoimg1, borderwidth=0)
        b1. place(x=220, y=15)

        DataFrame=Frame(self. root, bd=15, relief=RIDGE, padx=20)
        DataFrame . place(x=0, y=120, width=1530, height=400)

        DataFrameLeft=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information",
                                       fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameLeft. place(x=0, y=5, width=908, height=350)

        DataFramerRight=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department",
                                            fg="darkgreen", font=("arial",12, "bold"))

        DataFramerRight . place(x=910, y=5, width=540, height=350)

       

         #below buttons

        ButtonFrame=Frame (self . root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame . place (x=0, y=520, width=1530, height=65)

        btnAddData=Button(ButtonFrame, text="Medicine Add",font=("arial", 12, "bold"), bg="darkgreen", fg="white" , command = self.add_data )
        btnAddData. grid(row=0, column=0)

        btnUpdateMed=Button(ButtonFrame, text="UPDATE", font=("arial", 13, "bold"), width=14, bg="darkgreen",fg="white" , command=self.update_new)
        btnUpdateMed . grid(row=0, column=1)
        
        btnDeleteMed=Button(ButtonFrame, text="DELETE", font=("arial", 13, "bold"), width=14, bg="red",fg="white", command=self.delete_new )
        btnDeleteMed. grid(row=0, column=2)

        btnExitMed=Button(ButtonFrame, text="RESET", font=("arial", 13, "bold"), width=14, bg="darkgreen", fg="white", command=self.clear_new)
        btnExitMed. grid(row=0, column=4)

        # search by-----------

        lblSearch=Label(ButtonFrame, font=("arial", 17, "bold"), text=" Search By ", padx=2, bg="lightgreen", fg="black" )
        lblSearch. grid(row=0, column=5, sticky=W)

        #variable for search 
        self.searchby_var = StringVar()
        self.searchtxt_var = StringVar()

        serch_combo=ttk. Combobox(ButtonFrame, textvariable=self.searchby_var, width=12, font=("arial", 17, "bold"), state="readonly")
        serch_combo[ "values"]= ("Ref_no", "medname", "lot")
        serch_combo. grid(row=0, column=6)
        serch_combo. current(0)

        txtSerch=Entry(ButtonFrame, textvariable=self.searchtxt_var, bd=3, relief=RIDGE, width=12, font=("arial", 17, "bold"))
        txtSerch.grid(row=0, column=7)

        searchBtn=Button(ButtonFrame, text="SEARCH", font=("arial", 13, "bold"), width=13, bg="darkgreen", fg="white" , command=self.search_data )
        searchBtn. grid(row=0, column=8)

        showAll=Button (ButtonFrame, text="SHOW ALL", font=("arial", 13, "bold"), width=13, bg="darkgreen", fg="white" , command=self.fetch_new )
        showAll . grid(row=0, column=9)




         #### labeling & entry box #########


         #1

       
        lblrefno=Label(DataFrameLeft,  font=("arial", 12, "bold"), text="Reference No", padx=2)
        lblrefno. grid(row=0, column=0, sticky=W)


        conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
        mycursor=conn.cursor()
        mycursor.execute("select ref from pharma")
        r=mycursor.fetchall()

        ref_combo=ttk. Combobox(DataFrameLeft, textvariable = self.refno_var, width=27, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"]=r
        ref_combo. grid(row=0, column=1)
        ref_combo. current (0)

        # 2


        lblCmpName=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Company Name: ", padx=2, pady=6)
        lblCmpName. grid(row=1, column=0, sticky=W)
        txtCmpName=Entry(DataFrameLeft, textvariable = self.cmpName_var, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtCmpName. grid(row=1, column=1)


        # 3


        lblTypeofMedicine=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Type Of Medicine", padx=2, pady=6)
        lblTypeofMedicine. grid(row=2, column=0, sticky=W)

        comTypeofMedicine=ttk . Combobox(DataFrameLeft, textvariable =  self.typeMed_var , state="readonly",
                                                     font=("arial",12, "bold"), width=27)
        comTypeofMedicine['value' ]=("Tablet", "Syrup", "Capsules", "Topical Medicines", "Drops", "Inhales", "Injection")
        comTypeofMedicine. current(0)
        comTypeofMedicine. grid(row=2, column=1)

        #      4   --------------------------- add medicine name-----------

        lblMedicineName=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name", padx=2, pady=6)
        lblMedicineName. grid(row=3, column=0, sticky=W)


        conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
        mycursor=conn.cursor()
        mycursor.execute("select MedName from pharma")
        med=mycursor.fetchall()
       
        comMedicineName = ttk. Combobox(DataFrameLeft, textvariable = self.medName_var, state="readonly",
                                    font=("arial", 12, "bold"), width=27)
        comMedicineName[ 'value' ]= med
        comMedicineName. current(0)
        comMedicineName . grid(row=3, column=1)

        # 5


        lblLotNo=Label(DataFrameLeft, font=("arial",12, "bold"), text="Lot No:", padx=2, pady=6)
        lblLotNo. grid(row=4, column=0, sticky=W)
        txtLotNo=Entry(DataFrameLeft, textvariable = self.lot_var , font=("arial", 13, "bold"), bg="white",bd=2, relief=RIDGE, width=29)
        txtLotNo. grid(row=4, column=1)

        # 6

        lblIssueDate=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate. grid(row=5, column=0, sticky=W)
        txtIssueDate=Entry(DataFrameLeft, textvariable = self.issuedate_var, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtIssueDate. grid(row=5, column=1)

        # 7

        lblExDate=Label (DataFrameLeft, font=("arial",12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExDate. grid(row=6, column=0, sticky=W)
        txtExDate=Entry(DataFrameLeft, textvariable = self.expdate_var, font=("arial", 13, "bold"), bg="white",bd=2, relief=RIDGE, width=29)
        txtExDate. grid(row=6, column=1)

        # 8

        lbluses=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses:",padx=2, pady=4)
        lbluses. grid(row=7, column=0, sticky=W)
        txtUses=Entry(DataFrameLeft, textvariable = self.uses_var, font=("arial", 13, "bold"), bg="white",bd=2, relief=RIDGE, width=29)
        txtUses. grid(row=7, column=1)

        # 9


        lblSideEffect=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect. grid(row=8, column=0, sticky=W)
        txtSideEffect=Entry(DataFrameLeft, textvariable = self.sideeffect_var, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtSideEffect . grid(row=8, column=1)

        # 10
        
        lblPrecWarning = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Prec&Warning: ", padx=15)
        lblPrecWarning . grid(row=0, column=2, sticky=W)
        txtPrecwarning= Entry(DataFrameLeft, textvariable = self.warning_var, font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrecwarning . grid(row=0, column=3)

        #11

        lblDosage=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dosage:",padx=15, pady=6)
        lblDosage. grid(row=1, column=2, sticky=W)
        txtDosage=Entry(DataFrameLeft, textvariable = self.dosage_var, font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtDosage. grid(row=1, column=3)

        #12

        lblPrice=Label(DataFrameLeft, font=("arial", 12, "bold"), text="Tablets Price:", padx=15, pady=6)
        lblPrice.grid(row =2, column=2,sticky=W)
        txtPrice=Entry (DataFrameLeft, textvariable = self.price_var, font=("arial",12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrice.grid(row=2, column=3)

        #13

        lblProductQt=Label(DataFrameLeft, font=("arial",12, "bold"), text="Product QT:",padx=15, pady=6)
        lblProductQt.grid(row=3, column=2, sticky=W)
        txtProductQt=Entry(DataFrameLeft, textvariable = self.product_var, font=("arial",12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtProductQt . grid(row=3, column=3, sticky=W)


         #  frame right......


        lblrefno=Label(DataFramerRight, font=("arial",12, "bold"), text="Reference No:")
        lblrefno. place(x=0, y=80)
        txtrefno=Entry(DataFramerRight, textvariable=self.refmed_var, font=("arial", 15, "bold"), bg="white",bd=2, relief=RIDGE, width=14)     
        txtrefno . place(x=135,y=80)

        lblmedName=Label (DataFramerRight, font=("arial", 12, "bold"), text="Medicine Name:")
        lblmedName. place (x=0, y=110)
        txtmedName=Entry(DataFramerRight, textvariable=self.addmed_var, font=("arial", 15, "bold"), bg="white", bd=2, relief=RIDGE, width=14)
        txtmedName. place (x=135, y=110)


        #side frame

        side_frame=Frame(DataFramerRight, bd=4, relief=RIDGE, bg="white")
        side_frame. place(x=0, y=150, width=290, height=160)

        sc_x=ttk. Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x. pack(side=BOTTOM, fill=X)
        sc_y=ttk. Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table=ttk.Treeview(side_frame, column=("ref", "medname"), xscrollcommand=sc_x.set,  yscrollcommand=sc_y.set)

        sc_x. config(command=self.medicine_table.xview)
        sc_y.config(command=self .medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table. heading("medname", text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table. pack(fill=BOTH, expand=1)

        self.medicine_table. column("ref",width=100)
        self.medicine_table. column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.medget_cursor)
        self.fetch_dataMed()

        # side button

        down_frame = Frame( DataFramerRight  , bd=4, relief=RIDGE, bg="darkgreen")
        down_frame. place(x=330, y=150, width=135, height=160)


        btnAddmed=Button(down_frame, text="ADD", font=("arial", 12, "bold"), width=12, bg="lime",fg="white", pady=4 , command=self.Addmed)
        btnAddmed.grid(row=0, column=0)

        btnUpdatemed=Button(down_frame, text="UPDATE", font=("arial", 12, "bold"), width=12, bg="purple", fg="white", pady=4 , command=self.Updatemed)
        btnUpdatemed. grid(row=1, column=0)

        btnDeletemed=Button(down_frame, text="DELETE", font=("arial", 12, "bold"), width=12, bg="red", fg="white", pady=4 , command=self.Deletemed)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame, text="CLEAR", font=("arial", 12, "bold"), width=12, bg="orange", fg="white", pady=4 , command=self.clearmed)
        btnClearmed. grid(row=3, column=0)

         # frame detail

        Framedeatils=Frame(self. root, bd=15, relief=RIDGE)
        Framedeatils. place(x=0, y=580, width=1530, height=210)

        #=Main Table & scrollbar===
        Table_frame=Frame(self. root, bd=15, relief=RIDGE)
        Table_frame. place(x=0, y=590, width=1460, height=180)

        scroll_x=ttk. Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack (side=RIGHT, fill=Y)


        self. pharmacy_table=ttk. Treeview(Table_frame, column=("reg", "companyname", "type", "tabletname", "lotno", "issuedate",
                                 "expdate", "uses", "sideeffect", "warning", "dosage", "price", "productqt")
                                             ,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x. pack(side=BOTTOM, fill=X)
        scroll_y . pack (side=RIGHT, fill=Y)

        scroll_x. config(command=self . pharmacy_table. xview)
        scroll_y . config(command=self . pharmacy_table. yview)

        self. pharmacy_table["show"]="headings"

        self.pharmacy_table. heading("reg", text="Reference No")
        self. pharmacy_table. heading("companyname", text="Company Name")
        self. pharmacy_table. heading("type", text="Type Of Medicine")
        self. pharmacy_table. heading("tabletname", text="Tablet Name")
        self. pharmacy_table. heading("lotno", text="Lot No")
        self. pharmacy_table. heading( "issuedate", text="Issue Date")
        self. pharmacy_table. heading("expdate", text="Exp Date")
        self . pharmacy_table. heading("uses", text="Uses")
        self. pharmacy_table. heading("sideeffect", text="side Effect")
        self. pharmacy_table. heading("warning", text="Prec&warning")
        self. pharmacy_table. heading("dosage", text="Dosage")
        self . pharmacy_table. heading("price", text="price")
        self. pharmacy_table. heading("productqt", text="Product Qts")
        self.pharmacy_table. pack(fill=BOTH, expand=1)

        self.pharmacy_table.column("reg",width=100)
        self. pharmacy_table. column("companyname", width=100)
        self. pharmacy_table. column( "type", width=100)
        self. pharmacy_table. column("tabletname", width=100)
        self . pharmacy_table. column("lotno", width=100)
        self . pharmacy_table. column("issuedate", width=100)
        self . pharmacy_table. column("expdate", width=100)
        self. pharmacy_table. column("uses", width=100)
        self . pharmacy_table. column( "sideeffect", width=100)
        self . pharmacy_table. column("warning", width=100)
        self . pharmacy_table. column("dosage", width=100)
        self . pharmacy_table. column("price", width=100)
        self. pharmacy_table. column("productqt", width=100)
        self.fetch_dataMed()
        self.fetch_new()
        self.pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor)


              # for add button....................

    def Addmed (self) :

        if self.refmed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
            
        else:
    
            conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
            mycursor=conn.cursor()
        
            mycursor.execute("insert into pharma(Ref, MedName) values(%s,%s)", (
                                                                        self.refmed_var.get(),
                                                                        self.addmed_var.get(),
                                                                    
                                                                                ))
            
            conn.commit()
            self.fetch_dataMed()
            self.Medget_curser()
            conn.close()   
            


    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
        mycursor=conn.cursor()
    
        mycursor.execute("select * from pharma")
        rows=mycursor.fetchall()  
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in rows:
                self.medicine_table.insert("",END,values=i)

            conn.commit()
            conn.close()    

 ###### for show data on click #####

    def medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])



    def Updatemed(self):
    
        if self.refmed_var.get() == "" or self.addmed_var.get() == "":
         messagebox.showerror("Error", "All fields are required")

        else:
            
            conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
            my_cursor = conn.cursor()

            my_cursor.execute("Update pharma set MedName=%s where Ref=%s", (
                                                                            self.addmed_var.get(),
                                                                            self.refmed_var.get(),
                                                                          ))

            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Update", "Successfully Updated")



    def Deletemed(self):

        conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
        my_cursor = conn.cursor()

       
        sql="Delete from pharma where Ref=%s"
        val= (self.refmed_var.get(),)
        my_cursor.execute(sql,val)
    
        conn.commit()
        self.fetch_dataMed()
        conn.close()


    def clearmed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")


        ######## MEDICINE DEPARTMENT FUNCTIONALITY #######

    def add_data(self):

        if self.refno_var.get() == "" or self.lot_var.get() == "" or self.typeMed_var.get() == "":
            messagebox.showerror("Error","Lot No is required")

           
        else:
       
            conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
            mycursor=conn.cursor()
            
            mycursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (


                                                                                                self.refno_var.get(),
                                                                                                self.cmpName_var.get(),
                                                                                                self.typeMed_var.get(),
                                                                                                self.medName_var.get(),
                                                                                                self.lot_var.get(),
                                                                                                self.issuedate_var.get(),
                                                                                                self.expdate_var.get(),
                                                                                                self.uses_var.get(),
                                                                                                self.sideeffect_var.get(),
                                                                                                self.warning_var.get(),
                                                                                                self.dosage_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.product_var.get(),                                                                          

                                                                                             ))
            
            conn.commit()
            self.fetch_new()
            conn.close()    

            messagebox.showinfo("Success","Data has been added")



    def fetch_new(self):
    
        conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
        mycursor=conn.cursor()
        mycursor.execute("select * from pharmacy")
        row=mycursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())

            for i in row:
                self.pharmacy_table.insert("",END,values=i)

            conn.commit() 
        conn.close()      



    def get_cursor(self,event=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]

        self.refno_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])
        self.issuedate_var.set(row[5])
        self.expdate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideeffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.product_var.set(row[12])    



    def update_new(self):  
        
        if self.refno_var.get() == "" or self.lot_var.get() == "" or self.typeMed_var.get() == "":
            messagebox.showerror("Error","Lot No is required")


        else:
            
            conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
            my_cursor = conn.cursor()

            my_cursor.execute("Update pharmacy set cmpName=%s , Type=%s , medname=%s, lot=%s, Issuedate=%s, expdate=%s, uses=%s,  Sideeffect=%s,  warning=%s, dosage=%s, price=%s, product=%s where Ref_no=%s ",(
                                                                                               
                                                                                                self.cmpName_var.get(),
                                                                                                self.typeMed_var.get(),
                                                                                                self.medName_var.get(),
                                                                                                self.lot_var.get(),
                                                                                                self.issuedate_var.get(),
                                                                                                self.expdate_var.get(),
                                                                                                self.uses_var.get(),
                                                                                                self.sideeffect_var.get(),
                                                                                                self.warning_var.get(),
                                                                                                self.dosage_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.product_var.get(), 
                                                                                                self.refno_var.get(),
                                                                                                                               )) 

            conn.commit()
            self.fetch_new()
            #   self.clear_new()
            conn.close()

            messagebox.showinfo("Update", "Record has been Updated Successfully") 




    def delete_new(self):

        conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
        my_cursor = conn.cursor()

       
        sql="Delete from pharmacy where Ref_no=%s"
        val= (self.refno_var.get(),)
        my_cursor.execute(sql,val)
    
        conn.commit()
        self.fetch_new()
        conn.close()

        messagebox.showinfo("Delete", "Record has been deleted Successfully") 



    def clear_new(self):
       # self.refno_var.set("")
        self.cmpName_var.set("")
       # self.typeMed_var.set("")
       # self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideeffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.product_var.set("")



    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username = "root", password= "5432" , database = "mydata")
        my_cursor = conn.cursor()

        selected = self.searchby_var.get()
        if selected == "Ref_no":

            my_cursor.execute("select * from pharmacy where Ref_no = %s  ",(self.searchtxt_var.get(),)) 

        elif selected == "medname":        
      
            my_cursor.execute("select * from pharmacy where medname = %s  ",(self.searchtxt_var.get(),)) 

        elif selected == "lot":        
      
            my_cursor.execute("select * from pharmacy where lot = %s  ",(self.searchtxt_var.get(),)) 

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)

            conn.commit()
        conn.close()    






if __name__ == "__main__":


    def ok():
        uname = e1.get()
        password = e2.get()


        if(uname == "" and password ==""):
            messagebox.showinfo("","blank not allowed")

        elif(uname == "admin" and password =="123"):
            messagebox.showinfo("","login success")
            obj=PharmacyManagementSystem(root)

        else:
            messagebox.showinfo("","incorrect username and password")

    




    root = Tk()
    root.title("login")
    root.geometry("300x200")
    global e1
    global e2

    Label(root, text="username").place(x=10, y=10)
    Label(root, text="password").place(x=10, y=40)

    e1= Entry(root)
    e1.place(x=148, y=10)

    e2= Entry(root)
    e2.place(x=148, y=40)
    e2.config(show="*")


    Button(root, text="login", command=ok, height=3, width=13).place(x=10, y=100)

    
    
    root.mainloop()
