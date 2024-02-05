from tkinter import*

Wn=Tk()
Wn.title("Login")
Wn.geometry("500x150")


Username = Entry(Wn, textvariable="User", font=("Arial", 15))
Username.place(x=145, y=40)
Password = Entry(Wn, textvariable="User", font=("Arial", 15))
Password.place(x=145, y=110)

user = Label(Wn, text="Username", font=("Arial", 20))
user.place(x=145, y=0)
Pass = Label(Wn, text="Password", font=("Arial", 20))
Pass.place(x=145, y=70)


def Login():
    Username = input("Enter Username: ")
    Password = input("Enter Username: ")
    if Username == "MrLeeman":
        if Password == "MrLeeman":
           return True
    else:
        print("Wrong Username Or Password")
        return Login()

def CheckInput(Message):
    Choice = input(Message).upper()
    if Choice == "Y":
        return True
    if Choice == "N":
        return False
    else:
        print("Please try again")
        CheckInput(Message)

def GetStudents():
    CSV = open("Class.csv","r")
    Data = []
    for Line in CSV:
        TempData = (Line.split(","))
        del TempData[-1]
        Data.append(TempData)
    return Data


def SaveStudents(Students):
    CSV = open("Class.csv","w")
    for Student in Students:
        Student_Data = ','.join([str(v) for v in Student])
        CSV.write(Student_Data + ",\n")

def AddStudent(Students):
    ID = input("Enter ID: ")
    Forename  = input("Enter forename")
    Surname = input("Enter surname")
    Number = input("Enter Number")
    Address = input("Enter Address")
    Data = [ID,Forename,Surname,Number,Address]
    Students.append(Data)

def ViewStudent(Students,ID_Lookup):
    for Student in Students:
        if  Student[0] == ID_Lookup:
            return Student

def PrintStudent(Student):
    if Student:
        print("ID: {} Forename: {} Surname: {} Number: {} Address: {}".format(*Student))

def Menu():
    IsLogin = Login()
    Students = GetStudents()
    while True:
        Selection = int(input("Select Option \n\n"
            "1. View Student \n"
            "2. Add Student \n"
            "3. Save Students \n"
            "4. Print Students \n"
            "5. Exit \n"
            ))
        if Selection == 1:
            PrintStudent(ViewStudent(Students,input("Enter Student ID:")))
        elif Selection == 2:
            AddStudent(Students)
        elif Selection == 3:
            SaveStudents(Students)
        elif Selection == 4:
            print(Students)
        elif Selection == 5:
            exit()
        


#Menu()
