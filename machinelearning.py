import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_iris
import joblib
from sklearn.tree import DecisionTreeClassifier
from tkinter import messagebox
import numpy as np 
import pandas as pd
from PIL import ImageTk,Image


iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier()

model.fit(X,y)


joblib.dump(model,"iris_model.joblib")

root = tk.Tk()

title = root.title("machinelearning")

root.geometry("300x500")

root.configure(background="skyblue")

root.iconbitmap('D:\\TinkerForm\\letter_m_alphabet_icon_263111.ico')
root.configure(bg="skyblue")

image = Image.open("D:\\TinkerForm\\letter_m_alphabet_icon_263111.ico")
photo = ImageTk.PhotoImage(image)


label = tk.Label(root,image=photo)
label.pack(pady=10)

sapel_length = tk.Label(root,text="sepel Length",background="skyblue")
sapel_length.pack()
sapel_length_entry = tk.Entry(root,width=20)
sapel_length_entry.pack(pady=5)

pettel_length = tk.Label(root,text="pettel Length",background="skyblue")
pettel_length.pack()
pettel_length_entry = tk.Entry(root,width=20)
pettel_length_entry.pack(pady=5)

sapel_width = tk.Label(root,text="sepel width",background="skyblue")
sapel_width.pack()
sapel_width_entry = tk.Entry(root,width=20)
sapel_width_entry.pack(pady=5)

pettel_width = tk.Label(root,text="pettel width",background="skyblue")
pettel_width.pack()
pettel_width_entry = tk.Entry(root,width=20)
pettel_width_entry.pack(pady=5)

species = tk.Label(root,text="",background="skyblue")
species.pack()

model1 = joblib.load("iris_model.joblib")

def predict_species():
    try:
        sapel_length = float(sapel_length_entry.get())
        sapel_width = float(sapel_width_entry.get())
        pettel_length = float(pettel_length_entry.get())
        pettel_width = float(pettel_width_entry.get())

        prediction = model.predict([[sapel_length,sapel_width,pettel_length,pettel_width]])
        species.config(text="Predicted species: "+ iris.target_names[prediction[0]])
    except ValueError:
        messagebox.showerror("Warning","Enter the value")


login_button = tk.Button(text="Predict",command=predict_species)
login_button.pack()
info = tk.Label(text="Enter number: 1,2,3,4,5",background='skyblue')
info.pack(pady=20)




root.mainloop()



