from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

#icon
image_icon = PhotoImage(file=r"D:\TinkerForm\BMI calculator\icon.png")
root.iconphoto(False,image_icon)


top = PhotoImage(file=r"D:\TinkerForm\BMI calculator\\top.png")
top_image = Label(root,image=top,background="#f0f1f5")
top_image.place(x=-10,y=-10)

Label(root,width=72,height=18,bg='lightblue').pack(side=BOTTOM)


box = PhotoImage(file=r"D:\TinkerForm\BMI calculator\box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

scale = PhotoImage(file=r"D:\TinkerForm\BMI calculator\scale.png")
Label(root,image=scale,bg="lightblue").place(x=20,y=310)


#slider
current_value  =DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event=None):
    Height.set(get_current_value())

style = ttk.Style()
style.configure("TScale",background='white')

slider = ttk.Scale(root,from_=0,to=220,orient='horizontal',style='TScale',
                   command=slider_changed,variable=current_value)
slider.place(x=80,y=250)



#slider
current_value2  =DoubleVar()

def get_current_value2():
    return "{: .2f}".format(current_value2.get())

def slider_changed2(event=None):
    Weight.set(get_current_value2())

    size = int(float(get_current_value()))
    image = (Image.open("D:\\TinkerForm\BMI calculator\\man.png"))
    resized_image = image.resize((50,10+size))

    photo2 = ImageTk.PhotoImage(resized_image)
    second_image.config(image=photo2)
    second_image.place(x=70,y=550-size)
    second_image.image=photo2

style2 = ttk.Style()
style2.configure("TScale",background='white')

slider2 = ttk.Scale(root,from_=0,to=200,orient='horizontal',style='TScale',
                   command=slider_changed2,variable=current_value2)
slider2.place(x=300,y=250)

def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    m=h/100
    bmi = round(float(w/(m*2)),2)
    label1.config(text=bmi)

    if bmi<=18.5:
        label2.config(text="UnderWeight!")
        label3.config(text="You have lower weight than normal")
    elif bmi>18.5 and bmi<=25:
        label2.config(text="Normal!")
        label3.config(text="You have normal weight, Healthy")
    elif bmi<25 and bmi <=30:
        label2.config(text="OverWeight!")
        label3.config(text="You are Over weight than normal")
    else:
        label2.config(text="OBSED!")
        label3.config(text="GO TO GYM NOW!!!")




Height = StringVar()
Weight = StringVar()

Label(root, text="Height (cm)", font='ariel 12', bg='white', fg='black').place(x=35, y=110)
Label(root, text="Weight (kg)", font='ariel 12', bg='white', fg='black').place(x=255, y=110)



height = Entry(root,textvariable=Height,width=5,font='ariel 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())
weight = Entry(root,textvariable=Weight,width=5,font='ariel 50',bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=255,y=160)
Weight.set(get_current_value2())

#man image
second_image = Label(root,bg="lightblue")


Button(root,text="View Report",width=15,height=2,font='ariel 10 bold',bg="#1f6e68",fg='white',command=BMI).place(x=280,y=340)

label1 = Label(root,font="ariel 40 bold",bg='lightblue',fg='black')
label1.place(x=115,y=330)

label2 = Label(root,font="ariel 20 bold",bg='lightblue',fg='black')
label2.place(x=280,y=405)

label3 = Label(root,font="ariel 10 bold",bg='lightblue',fg='black',justify=LEFT)
label3.place(x=200,y=450)



root.mainloop()