import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry('')
        self.root.configure(background = "black")
        
        
 ################## Variable Daclaration ################## 
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        
######### To generate Ranom Number #########
        def Reference_numfunc():
                randomnumber = random.randint(10000,9999999) ##ranumber errado
                Ref.set(randomnumber)
        
        
        def prescriptionfunc():
                Reference_numfunc()
                TextPrescription.insert(END,"Patient ID: \t\t"+PatientId.get()+"\n")
                TextPrescription.insert(END,"Patient ID: \t\t"+Patientname.get()+"\n")
                TextPrescription.insert(END,"Patient ID: \t\t"+cmbTabletNames.get()+"\n")
                TextPrescription.insert(END,"Patient ID: \t\t"+Number_of_Tablets.get()+"\n")
                TextPrescription.insert(END,"Patient ID: \t\t"+DailyDose.get()+"\n")
                TextPrescription.insert(END,"Patient ID: \t\t"+IssuedDate.get()+"\n")
                TextPrescription.insert(END,"Patient ID: \t\t"+ExpiryDate.get()+"\n")
                TextPrescription.insert(END,"Patient ID: \t\t"+StorageAdvice.get()+"\n")
                TextPrescription.insert(END,"Patient ID: \t\t"+MoreInformation.get()+"\n")
                return
                
        def prescriptiondatafunc():
                Reference_numfunc()
                TextPrescriptionData.insert(END, Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"+
                "\t"+Patientname.get()+"\t\t"+Dateofbirth.get()+"\t\t"+NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t"+
                Number_of_Tablets.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+
                StorageAdvice.get()+"\t\t"+PatientId.get()+"\n")
                return
        
        
        Ref = StringVar()
        cmbTabletNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()   
        SideEffets = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar ()
        PatientNHnumber = StringVar()
        Patientname = StringVar ()
        Dateofbirth = StringVar()
        PatientAddress = StringVar()
        NHSnumber = StringVar()
        
        
        def exitbtn():
                exitbtn = tkinter.messagebox.askyesno("Hospital Management System","Are you sure you want to exit?")
                if exitbtn > 0:
                    root.destroy()
                    return 
        
        def deletefunc():
                Ref.set("")
                cmbTabletNames.set("")
                HospitalCode.set("")
                Number_of_Tablets.set("")
                Lot.set("")
                IssuedDate.set("")
                ExpiryDate.set("")
                DailyDose.set("")
                SideEffets.set("")
                MoreInformation.set("")
                StorageAdvice.set("")
                Medication.set("")
                PatientId.set("")
                PatientNHnumber.set("")
                Patientname.set("")
                Dateofbirth.set("")
                PatientAddress.set("")
                NHSnumber.set("")
                TextPrescription.delete("1.0",END)
                TextPrescriptionData.delete("1.0",END)
                return
        
        def resetfunc():
                Ref.set("")
                cmbTabletNames.set("")
                HospitalCode.set("")
                Number_of_Tablets.set("")
                Lot.set("")
                IssuedDate.set("")
                ExpiryDate.set("")
                DailyDose.set("")
                SideEffets.set("")
                MoreInformation.set("")
                StorageAdvice.set("")
                Medication.set("")
                PatientId.set("")
                PatientNHnumber.set("")
                Patientname.set("")
                Dateofbirth.set("")
                PatientAddress.set("")
                NHSnumber.set("")
                TextPrescription.delete("1.0",END)
                return

        
        
################## TITLE ##################
        title = Label(self.root, text = "Hospital Management System", font = ("monotype corsiva",42,"bold"), bd = 5,
            relief=GROOVE,bg = "#2eb8b8", fg = "black")
        title.pack(side=TOP,fill= X)
        
################## Frames ##################
        Manage_Frame = Frame(self.root,width=1510, height=400, bd = 5, relief= RIDGE, bg = "#0099cc")
        Manage_Frame.place(x=10,y=80)
        
        Button_Frame = Frame(self.root,width=1510, height=55, bd = 4, relief= RIDGE, bg = "#328695")
        Button_Frame.place(x=10,y=460)
        
        Data_Frame = LabelFrame(self.root,width=1510, height=270, bd = 4, relief= RIDGE, bg = "#266e73")
        Data_Frame.place(x=10,y=510)
        
################## Inner Frames ##################
        Data_FrameLeft = LabelFrame(Manage_Frame,width=1050, text = "General Information", 
        font = ("arail",20,"italic bold"), height=390, bd = 7, relief= RIDGE, bg = "#0099cc")
        Data_FrameLeft.pack(side=LEFT)
        
        Data_Framedata = LabelFrame(Data_Frame,width=1050, text = "Prescription", font = ("arail",12,"italic bold"), 
        height=390, bd = 4, relief= RIDGE, bg = "#3eb7bb")
        Data_Framedata.pack(side=LEFT)
        
        Data_FrameRight = LabelFrame(Manage_Frame,width=1050, text = "Prescription Data", 
        font = ("arail",15,"italic bold"), height=390, bd = 7, relief= RIDGE, bg = "#0099cc")
        Data_FrameRight.pack(side=RIGHT)
        
        
################## Labels ##################
        Datelbl = Label(Data_FrameLeft, font=("arail",12,"bold"), width=20, text = "Date", padx=2, bg = "#0099cc")
        Datelbl.grid(row = 0, column = 0, padx=10, pady=5, sticky = W)
        Datetxt = Entry(Data_FrameLeft, font=("arail",12,"bold"), width=27, textvariable= Date_of_Registration)
        Datetxt.grid(row = 0, column = 1, padx=10, pady=5, sticky = E)

########### REF
        Reflbl = Label(Data_FrameLeft, font = ("arial", 12,"bold"), width = 20, text = "Reference Number", padx = 2, bg= "#0099cc")
        Reflbl.grid(row = 1 , column = 0, padx = 10, pady = 5, sticky = W)
        Reftxt = Entry(Data_FrameLeft, font = ("arial",12, "bold"), width = 27, state= DISABLED, textvariable = Ref)
        Reftxt.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = E)

############ Patient ID
        PatientIdlbl = Label (Data_FrameLeft , font = ("arial", 12, "bold"), width = 20, text = "Patient Id", padx = 2, bg= "#0099cc")
        PatientIdlbl.grid (row = 2, column = 0, padx = 10, pady = 5 , sticky = W)
        PatientIdtxt = Entry(Data_FrameLeft, font = ("arial",12, "bold"), width = 27 , textvariable = PatientId)
        PatientIdtxt.grid (row = 2, column = 1, padx = 10 , pady = 5 , sticky = E)
        
############ Patient Name
        Patientnamelbl = Label (Data_FrameLeft , font = ("arial", 12, "bold"), width = 20, text = "Patient Name", padx = 2, bg= "#0099cc")
        Patientnamelbl.grid (row = 3, column = 0, padx = 10, pady = 5 , sticky = W)
        Patientnametxt = Entry(Data_FrameLeft, font = ("arial",12, "bold"), width = 27 , textvariable = Patientname)
        Patientnametxt.grid (row = 3, column = 1, padx = 10 , pady = 5 , sticky = E)

############ Date of Birth
        Dateofbirthlbl = Label (Data_FrameLeft , font = ("arial", 12, "bold"), width = 20, text = "Date of Birth", padx = 2, bg= "#0099cc")
        Dateofbirthlbl.grid (row = 4, column = 0, padx = 10, pady = 5 , sticky = W)
        Dateofbirthtxt = Entry(Data_FrameLeft, font = ("arial",12, "bold"), width = 27 , textvariable = Dateofbirth)
        Dateofbirthtxt.grid (row = 4, column = 1, padx = 10 , pady = 5 , sticky = E)
        
############ Address
        Addresslbl = Label (Data_FrameLeft , font = ("arial", 12, "bold"), width = 20, text = "Address", padx = 2, bg= "#0099cc")
        Addresslbl.grid (row = 5, column = 0, padx = 10, pady = 5 , sticky = W)
        Addresstxt = Entry(Data_FrameLeft, font = ("arial",12, "bold"), width = 27 , textvariable = PatientAddress)
        Addresstxt.grid (row = 5, column = 1, padx = 10 , pady = 5 , sticky = E)

############ NHSnumber
        NHSnumberlbl = Label (Data_FrameLeft , font = ("arial", 12, "bold"), width = 20, text = "NHS unique number", padx = 2, bg= "#0099cc")
        NHSnumberlbl.grid (row = 6, column = 0, padx = 10, pady = 5 , sticky = W)
        NHSnumbertxt = Entry(Data_FrameLeft, font = ("arial",12, "bold"), width = 27 , textvariable = NHSnumber)
        NHSnumbertxt.grid (row = 6, column = 1, padx = 10 , pady = 5 , sticky = E)
        
############ Tablets name       
        Tabletlbl = Label (Data_FrameLeft , font = ("arial", 12, "bold"), width = 20, text = "Tablet", padx= 2, bg= "#0099cc")
        Tabletlbl.grid(row = 7, column= 0, padx = 10, pady = 5 , sticky = W)
        
        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable = cmbTabletNames, width= 25, state= "readonly", font=("arial",12,"bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Dan-p", "Dio-1 One", "Calpol", "Amlodipine Besylate", "Nexium",
                                    "Singulair", "Plavix", "Amoxicillian", "Azithromycin", "Limcin-906")
        Tabletcmb.current(0) # we will keep index 0 when nothing is selected
        Tabletcmb.grid(row = 7, column = 1, padx = 10 , pady = 5 )
        
##### No of tablets to take
        No_of_Tabletslbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Number of Tablets", padx= 2, bg= "#0099cc")
        No_of_Tabletslbl.grid(row = 8, column = 0, padx = 10, pady = 5 , sticky = W)
        No_of_Tabletstxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 27 , textvariable = Number_of_Tablets)
        No_of_Tabletstxt.grid(row = 8, column = 1 , padx = 10 , pady = 5 , sticky = E)
        
##### Hospital code
        HospitalCodelbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Hospital Code", padx= 2, bg= "#0099cc")
        HospitalCodelbl.grid(row = 0, column = 2, padx = 10, pady = 5 , sticky = W)
        HospitalCodetxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 25 , textvariable = HospitalCode)
        HospitalCodetxt.grid(row = 0, column = 3, padx = 10 , pady = 5 , sticky = E)

##### Strong advice where to keep medicine
        StorageAdvicelbl = Label(Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Storage Advice", padx= 2, bg= "#0099cc")
        StorageAdvicelbl.grid(row = 1, column = 2, padx = 10, pady = 5 , sticky = W)
        
        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable= StorageAdvice, width=23, state= "readonly",
            font = ("arial",12, "bold" ))
        StorageAdvicecmb['values'] = ("", "Under room temp", "Below 5*C", "Refrigeration")
        StorageAdvicecmb.current(0) 
        StorageAdvicecmb.grid(row = 1, column = 3, padx = 10 , pady = 5, sticky = E)

##### Lot number of medicine
        Lot_nolbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Lot Number", padx= 2, bg= "#0099cc")
        Lot_nolbl.grid(row = 2, column = 2, padx = 10, pady = 5 , sticky = W)
        Lot_notxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 25 , textvariable = Lot)
        Lot_notxt.grid(row = 2, column = 3, padx = 10 , pady = 5 , sticky = E)
        
##### Issued Date
        IssuedDatelbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Issued Date", padx= 2, bg= "#0099cc")
        IssuedDatelbl.grid(row = 3, column = 2, padx = 10, pady = 5 , sticky = W)
        IssuedDatetxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 25 , textvariable = IssuedDate)
        IssuedDatetxt.grid(row = 3, column = 3, padx = 10 , pady = 5 , sticky = E)

##### Expiry Date
        ExpiryDatelbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Expiry Date", padx= 2, bg= "#0099cc")
        ExpiryDatelbl.grid(row = 4, column = 2, padx = 10, pady = 5 , sticky = W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 25 , textvariable = ExpiryDate)
        ExpiryDatetxt.grid(row = 4, column = 3, padx = 10 , pady = 5 , sticky = E)
        
##### Daily Dose
        DailyDoselbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Dose", padx= 2, bg= "#0099cc")
        DailyDoselbl.grid(row = 5, column = 2, padx = 10, pady = 5 , sticky = W)
        DailyDosetxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 25 , textvariable = DailyDose)
        DailyDosetxt.grid(row = 5, column = 3, padx = 10 , pady = 5 , sticky = E)

##### Side Effets
        SideEffetslbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Side Effets", padx= 2, bg= "#0099cc")
        SideEffetslbl.grid(row = 6, column = 2, padx = 10, pady = 5 , sticky = W)
        SideEffetstxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 25 , textvariable = SideEffets)
        SideEffetstxt.grid(row = 6, column = 3, padx = 10 , pady = 5 , sticky = E)

##### More Information
        MoreInformationlbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "More Information", padx= 2, bg= "#0099cc")
        MoreInformationlbl.grid(row = 7, column = 2, padx = 10, pady = 5 , sticky = W)
        MoreInformationtxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 25 , textvariable = MoreInformation)
        MoreInformationtxt.grid(row = 7, column = 3, padx = 10 , pady = 5 , sticky = E)

##### Medication (Yes/No)
        Medicationlbl = Label (Data_FrameLeft, font = ("arial",12, "bold"), width = 20 , text = "Medication", padx= 2, bg= "#0099cc")
        Medicationlbl.grid(row = 8, column = 2, padx = 10, pady = 5 , sticky = W)
        Medicationtxt = Entry(Data_FrameLeft, font = ("arial",12, "bold" ),width = 25 , textvariable = Medication)
        Medicationtxt.grid(row = 8, column = 3, padx = 10 , pady = 5 , sticky = E)

##### Text for prescription fild 
        TextPrescription = Text(Data_FrameRight, font = ("arial",12, "bold"), width = 55 , height = 17, padx = 3, 
            pady = 5)
        TextPrescription.grid(row = 0, column = 0)
        
        
        TextPrescriptionData = Text(Data_Framedata, font = ("arial",12, "bold"), width = 203 , height = 12)
        TextPrescriptionData.grid(row = 1, column = 0)

##### Button o the middle frame
        Prescriptionbtn = Button(Button_Frame, text = "Prescription", bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 22, command= prescriptionfunc)
        Prescriptionbtn.grid(row=0, column=0, padx=15)
        
        Receiptbtn = Button(Button_Frame, text = "Prescription Data", bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 22, command= prescriptiondatafunc)
        Receiptbtn.grid(row=0, column=1, padx=15)
        
        Resetbtn = Button(Button_Frame, text = "Reset", bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 22, command= resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)
        
        Deletebtn = Button(Button_Frame, text = "Delete", bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 22, command= deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)
        
        Exitbtn = Button(Button_Frame, text = "Exit", bg = "#ffaab0", activebackground = "#fcceb2",
        font = ("arial",15,"bold"), width = 22, command= exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)
        
        prescriptiondatarow = Label(Data_Framedata, bg = "white", font= ("arial",12,"bold"), 
        text= "Date\tReference Id\tPatient Name\tDate of Birth\tNHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStrong Advice\tPatient Id")
        prescriptiondatarow.grid(row = 0, column= 0, sticky= W)

        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0") ##### geometry da tela ###
        
if __name__ == "__main__":
    root = Tk()
    app = hospital(root)
    root.mainloop()
    
    