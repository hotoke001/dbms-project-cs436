import pymysql
import pymysql.cursors
from tkinter import *
from prettytable import PrettyTable


class Hospital(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.master = master
        zip = StringVar()

    def create_widgets(self):
        self.button = Button(self, text="Open Database", fg="green", command=self.begin)
        self.button.grid(row=0, column=0, sticky=W)

        self.button2 = Button(self, text="Close Connection", fg="red", command=self.closed)
        self.button2.grid(row=0, column=3, sticky=W)

        self.button3 = Button(self, text="Add new Patient", command=self.insert_patients)
        self.button3.grid(row=0, column=1, sticky=W)

        self.button4 = Button(self, text="Doctor Staff Members", command=self.doctorlist)
        self.button4.grid(row=0, column=2, sticky=W)

    def begin(self):
        # Establish a MySQL connection
        self.con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='DbTest123',
                                   database='hdbms')
        # Get the cursor to traverse the database, line by line
        self.cur = self.con.cursor()

    def closed(self):
        self.con.commit()
        self.cur.close()
        self.con.close()

    # Close MySQL Connections

    def patientlist(self): #Show all Patients
        self.cur.execute('Select pname,gender,phonenumber,dob from patients')
        print(self.cur.fetchall())

    def insert_patients(self):  # Add an Employee
        patient = input("Enter New Patient: ").strip()
        gender = input("Enter Gender: ").strip()
        phonenumber = input("Enter Phone Number: ").strip()
        dob = input("Enter Date of Birth: ").strip()

        self.cur.execute(
            "INSERT INTO patients (patient, gender,phonenumber,dob) VALUES (%s, %s, %s, %s)",
            (patient, gender, phonenumber, dob),
        )
        self.con.commit()
        print()
        return

    def doctorlist(self): #List of All Doctor
        self.cur.execute('Select * from doctor')
        print(self.cur.fetchall())


root = Tk()
root.title("Hospital Database Management")
root.geometry('600x300')
app = Hospital(root)
root.mainloop()
