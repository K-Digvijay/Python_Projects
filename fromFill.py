import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import openpyxl
import os

def enter_data():
    accepted = accept_var.get()
    if accepted == "Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if first_name and last_name:
            title = title_combobox.get()
            age = age_spin_box.get()
            nationality = nationality_combobox.get()
            completed_course = num_semester_spinbox.get()
            Registertion_status = reg_status_var.get()

            print(f"first name: {first_name} \nlast name: {last_name} \ntitle: {title}\nage:{age} \nnationality: {nationality} \ncompleted courses: {completed_course}")
            print(f"Registration status: {Registertion_status}")
            # creating the database
            file_path = "D:\DSA\data.xlsx"
            if not os.path.exists(file_path):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading=["First Name","Last Name","Title","age","Nationality",
                         "courses","Semesters","Registration Status"]
                sheet.append(heading)
                workbook.save(file_path)
            workbook = openpyxl.load_workbook(file_path)

        else:
            tk.messagebox.showwarning(title="Error", message="Enter First and Last Name")
    else:
        tk.messagebox.showwarning(title='Warning',message="Please accept the Trems")

window = tk.Tk()
window.title("Data entry Form")
#window.geometry("500x500")

frame = tk.Frame(window)
frame.grid(padx=10,pady=10)


user_info_frame = tk.LabelFrame(frame,text="USER INFORMATION")
user_info_frame.grid(row=0,column=0,padx=10,pady=10)

first_name_label = tk.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0,sticky='news')

last_name_label = tk.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)

last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=1,column=1)

title_label= tk.Label(user_info_frame,text='Title')
title_combobox = ttk.Combobox(user_info_frame,values=['Mr','Ms','Dr'])
title_label.grid(row=0,column=3)
title_combobox.grid(row=1,column=3)

age_label = tk.Label(user_info_frame,text='age')
age_spin_box = tk.Spinbox(user_info_frame,from_=1,to=100)
age_label.grid(row=4,column=0)
age_spin_box.grid(row=5,column=0)

nationality_label = tk.Label(user_info_frame,text="Nationality")
nationality_label.grid(row=4,column=1)

nationality_combobox = ttk.Combobox(user_info_frame,values=["India","Nepal","Bhutan","srilanka"])
nationality_combobox.grid(row=5,column=1)


courses_form = tk.LabelFrame(frame)
courses_form.grid(row=1,column=0,sticky="news",padx=10,pady=10)

regestration_label = tk.Label(courses_form,text="Registration Status")
regestration_label.grid(row=0,column=0)

reg_status_var = tk.StringVar(value="Not Registered")
registration_check = tk.Checkbutton(courses_form,text="currently Register",variable=reg_status_var,
                                    onvalue="Registered",offvalue="Not Registered")
registration_check.grid(row=1,column=0)

num_courses_label = tk.Label(courses_form,text="Completed Courses")
num_courses_label.grid(row=2,column=0)

num_courses_spinbox = tk.Spinbox(courses_form,from_=0, to=8)
num_courses_spinbox.grid(row=1,column=1)

num_semester_label = tk.Label(courses_form,text='Sementer')
num_semester_label.grid(row=0,column=2)

num_semester_spinbox = ttk.Combobox(courses_form,
                                    values=['Sem 1','sem 2','sem 3','sem 4','sem 5','sem 6','sem 7','sem 8'])
num_courses_spinbox.grid(row=1,column=2)


terms_cnd = tk.LabelFrame(frame)
terms_cnd.grid(row=2,column=0,sticky="news",padx=10,pady=10)

term_cnd_label = tk.Label(terms_cnd,text="Terms and Condition")
term_cnd_label.grid()

accept_var = tk.StringVar(value="Not Accepted")
terms_cnd_tick = tk.Checkbutton(terms_cnd,text="I accept Terms and Condition",
                                variable=accept_var,onvalue="Accepted",offvalue="Not accepted")
terms_cnd_tick.grid()


button = tk.Button(frame,text="Enter Data",command=enter_data)
button.grid(row=3,column=0,padx=10,pady=10)




for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=5,pady=5)

for widget1 in courses_form.winfo_children():
    widget1.grid_configure(padx=5,pady=5)
window.mainloop()