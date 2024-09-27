import tkinter 
from tkinter import ttk 
from tkinter import messagebox
import tkinter.messagebox
import sqlite3

def enter_data():
    accept = accept_var.get()
    if accept == "accepted":
    #user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            numberof_courses = number_of_courses_spinbox.get()
            numberof_semesters =  number_of_semesters_spinbox.get()

            registration_status = reg_status_var.get( )
            numberof_courses = number_of_courses_spinbox.get()
            numberof_semesters = number_of_semesters_spinbox.get()


            print("first name:", firstname,"last name:",lastname)
            print("Title:",title, "Age:", age,"Nationality:",nationality)
            print("#courses:", numberof_courses,"#semesters:", numberof_semesters)
            print("registration status", registration_status)
            print("--------------------------------------------")
            #create a table
            conn = sqlite3.connect('dataentry.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS student_data
                        (firstname TEXT, lastname TEXT, title TEXT, age INT, nationality TEXT,
                        registration_status TEXT, numberof_courses INT, numberof_semesters INT)
                        '''
            conn.execute(table_create_query)
            #insert data
            data_insert_query = '''INSERT INTO student_data(firstname,lastname,title,
            age, nationality, registration_status, numberof_courses, numberof_semesters) VALUES (?,?,?,?,?,?,?,?)'''
            data_insert_tuple = (firstname,lastname,title,
            age, nationality, registration_status, numberof_courses, numberof_semesters)
            cursor = conn.cursor()
            cursor.execute(data_insert_query,data_insert_tuple)
            conn.commit()
            conn.close()

        else:
            tkinter.messagebox.showerror(title="ERROR",message="First name and last name are required")
    else: 
        tkinter.messagebox.showerror(title="ERROR",message="You not accepted the terms")
#create the main frame 
root = tkinter.Tk()
root.title("registeration form")

frame = tkinter.Frame(root)
frame.pack()
#saving user info
user_info_frame = tkinter.LabelFrame(frame,text="user information")
user_info_frame.grid(row= 0, column=0)

first_name_label = tkinter.Label(user_info_frame, text="first name")
first_name_label.grid(row=0, column=0, padx=20, pady= 10)
last_name_label = tkinter.Label(user_info_frame, text="last name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)

first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr","Ms","Dr"])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18 , to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["","UGANDA","KENYA","TANZANIA","SSUDAN","RWANDA","BURINDI"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1 )

#for multi selection edit
for widget in  user_info_frame. winfo_children():
    widget.grid_configure(padx=10,pady=5)

#saving course info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news",padx=20,pady=10)
registered_label = tkinter.Label(courses_frame, text="registration status")

reg_status_var = tkinter.StringVar()
registered_check = tkinter.Checkbutton(courses_frame, text="currently registered", variable= reg_status_var, onvalue="registered",offvalue="not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

number_of_courses_label = tkinter.Label(courses_frame,text="#completed courses")
number_of_courses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
number_of_courses_label.grid(row=0, column=1)
number_of_courses_spinbox.grid(row=1,column=1)

number_of_semesters_label = tkinter.Label(courses_frame,text="#semesters")
number_of_semesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')

number_of_semesters_label.grid(row=0,column=2)
number_of_semesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)
#accept terms
terms_frame = tkinter.LabelFrame(frame,text="terms & conditions")
terms_frame.grid(row=2, column=0, sticky="news",padx=20, pady=10)

accept_var = tkinter.StringVar(value="not accepted")
terms_check = tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions.", variable=accept_var, onvalue="accepted",offvalue="not accepted")
terms_check.grid(row=0, column=0)

#button
button = tkinter.Button(frame, text="enter data",command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
root.mainloop()
