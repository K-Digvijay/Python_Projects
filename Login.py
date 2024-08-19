import tkinter as tk
from tkinter import messagebox
import numpy as np 
import pandas as pd
from PIL import ImageTk,Image


root = tk.Tk()
title = root.title("Machine Learning")
root.geometry("400x300")
root.minsize(300,300)
root.maxsize(600,600)
root.iconbitmap('D:\\TinkerForm\\letter_m_alphabet_icon_263111.ico')
root.configure(bg="skyblue")

image = Image.open("D:\\TinkerForm\\letter_m_alphabet_icon_263111.ico")
photo = ImageTk.PhotoImage(image)


label = tk.Label(root,image=photo)
label.pack(pady=10)

login = tk.Label(root,text="Username", background="skyblue")
login.pack()
login_entry = tk.Entry(root,width=20)
login_entry.pack(pady=5)



def login():
    login1 = login_entry.get()
    if login1 == "admin":
        tk.messagebox.showinfo("Login","You have Enter the data")
    elif login1 != "admin":
        tk.messagebox.showerror("Warning","Enter correct data")
    else:
        tk.messagebox.showerror("Warning","Enter the data")

login_button = tk.Button(text="Click",command=login)
login_button.pack()



root.mainloop()