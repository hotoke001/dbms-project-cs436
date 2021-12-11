import pymysql
import pymysql.cursors
import tkinter as tk
from tkinter import ttk
from tkinter import *


class Hospital(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.master = master
        zip = StringVar()

    def create_widgets(self): #Option Box Creation
        self.button = Button(self, text="Open Database", fg="green", command=self.begin, height = 2, width = 25)
        self.button.grid(row=0, column=0, sticky=W)

        self.button2 = Button(self, text="Close Connection", fg="red", command=self.closed, height = 2, width = 25)
        self.button2.grid(row=0, column=1, sticky=W)

        self.button3 = Button(self, text="Add new Patient", command=self.insert_patients, height = 2, width = 25)
        self.button3.grid(row=1, column=0, sticky=W)

        self.button4 = Button(self, text="Doctor Staff", command=self.doctorlist, height = 2, width = 25)
        self.button4.grid(row=2, column=1, sticky=W)

        self.button5 = Button(self, text="All patients", command=self.patientlist, height = 2, width = 25)
        self.button5.grid(row=1, column=1, sticky=W)

        self.button6 = Button(self, text="Show City Location", command=self.insurancelist, height = 2, width = 25)
        self.button6.grid(row=3, column=0, sticky=W)

        self.button7 = Button(self, text="Delete Patients", command=self.delete_patients, height = 2, width = 25)
        self.button7.grid(row=2, column=0, sticky=W)

        self.button8 = Button(self, text="Update Patients' information", command=self.update_patients, height = 2, width = 25)
        self.button8.grid(row=3, column=1, sticky=W)

    def begin(self):
        # Establish a MySQL connection
        self.con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Caomeibbt520.',
                                   database='hdbms')
        # Get the cursor to traverse the database, line by line
        self.cur = self.con.cursor()

    def closed(self):
        self.con.commit()
        self.cur.close()
        self.con.close()

    # Close MySQL Connections

    def patientlist(self): # Query and show results
        p1 = tk.Toplevel(root)
        p1.geometry('500x500')
        p1.title("Patient currently enrolled")

        columns = ('Patient Name', 'Gender', 'Phone Number', 'Date of Birth')  # Tree View Setup
        tree = ttk.Treeview(p1, height=20, columns=columns, show='headings')
        tree.grid(row=0, column=0, sticky='news')

        for col in columns:  # Columns Attributes
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        self.cur.execute('Select pname, gender, phonenumber, dob FROM patients')  # Fetch Data
        patientsT = self.cur.fetchall()

        # row in patientsT:
        i = 0
        for i in range(len(patientsT)):
            tree.insert('', 'end', value=patientsT[i])

        print(patientsT)

    def insert_patients(self):  # Add an Patient

        pname = input("Enter New Patient: ").strip()
        gender = input("Enter Gender: ").strip()
        phonenumber = input("Enter Phone Number: ").strip()
        dob = input("Enter Date of Birth: ")
        addyID = input("Enter Address Code:").strip()

        self.cur.execute(
            "INSERT INTO patients (pname, gender,phonenumber,dob,adrID) VALUES (%s, %s, %s, %s,%s)",
            (pname, gender, phonenumber, dob, addyID),
        )
        self.con.commit()
        print() #Debug print
        return

    def doctorlist(self): #Doctor Query
        p2 = tk.Toplevel(root)
        p2.geometry('500x500')
        p2.title("Doctors currently enrolled")

        columns = ('Doctor Name', 'Gender', 'Phone Number', 'Date of Birth',)  # Tree View Setup
        tree = ttk.Treeview(p2, height=20, columns=columns, show='headings')
        tree.grid(row=0, column=0, sticky='news')

        for col in columns:  # Columns Attributes
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        self.cur.execute('Select dname, gender, phonenumber, dateofBirth FROM doctor')  # Fetch Data
        doctorstreeT = self.cur.fetchall()

        i = 0
        for i in range(len(doctorstreeT)):
            tree.insert('', 'end', value=doctorstreeT[i])


    def insurancelist(self): #Insurance Query
        p1 = tk.Toplevel(root)
        p1.geometry('500x500')
        p1.title("Current Hospital network Buildings")

        columns = ('Company','pID')  # Tree View Setup
        tree = ttk.Treeview(p1, height=20, columns=columns, show='headings')
        tree.grid(row=0, column=0, sticky='news')

        for col in columns:  # Columns Attributes
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        self.cur.execute('Select company FROM insurance')  # Fetch Data
        insuranceT = self.cur.fetchall()

        # row in patientsT:
        i = 0
        for i in range(len(insuranceT)):
            tree.insert('', 'end', value=insuranceT[i])

    def insert_doctors(self):  # Add an Doctor

        dname = input("Enter New Doctor: ").strip()
        gender = input("Enter Gender: ").strip()
        phonenumber = input("Enter Phone Number: ").strip()
        dob = input("Enter Date of Birth: ")
        addyID = input("Enter Address Code:").strip()

        self.cur.execute(
            "INSERT INTO doctor (dname, gender,phonenumber,dateofBirth,adrID) VALUES (%s, %s, %s, %s,%s)",
            (dname, gender, phonenumber, dob, addyID),
        )
        self.con.commit()
        print()

    def delete_patients(self):  # delete a Patient

        pname = input("Enter the patients' name that you want to delete:").strip()

        self.cur.execute(
            "DELETE FROM Patients WHERE pname = '%s'" % (pname)
        )
        self.con.commit()
        print()
        return

    def update_patients(self):  # update information

        old_info = input("Enter the patient's old phone number: ").strip()
        update_info = input("Enter the patient's new phone number: ").strip()

        self.cur.execute(
            "UPDATE patients SET phonenumber =  '%s' WHERE phonenumber = '%s'" % (update_info, old_info)
        )
        self.con.commit()
        print()
        return

root = tk.Tk()
root.title("Hospital Database Management")
root.geometry('600x300')
app = Hospital(root)
root.mainloop()
