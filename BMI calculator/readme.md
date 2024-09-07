# Welcome, this the small python project BMI Calculator
## let get in to the step by step how to write the code using the tkinter library

first install tkinker and PIL library in using pip in the terminal. you can your any favourate IDE (Integrated Development Environment)
  ``` python
  pip install tkinker
  pip install pil
  ```
After installing the required libraries lets jump into IDE.
- First we have to impoe=rts some libraries
  ``` python
  from tkinter import *
  from tkinter import ttk
  from PIL import Image,ImageTk
  ```
- lets create the basic frame usng the tkinker app
  ```python
  root = Tk()
  root.title("BMI Calculator")
  root.geometry("470x580+300+200")
  root.resizable(False,False)
  root.configure(bg="#f0f1f5")
  
  
  root.mainloop()
  ```
Note : root.mainloop() will remain at the last for looping your code

- After the basic frame lets add widgets the files are present in the folder 

  ``` python
  top = PhotoImage(file=r"D:\TinkerForm\BMI calculator\\top.png")
  top_image = Label(root,image=top,background="#f0f1f5")
  top_image.place(x=-10,y=-10)
  
  Label(root,width=72,height=18,bg='lightblue').pack(side=BOTTOM)
  
  box = PhotoImage(file=r"D:\TinkerForm\BMI calculator\box.png")
  Label(root,image=box).place(x=20,y=100)
  Label(root,image=box).place(x=240,y=100)
  
  scale = PhotoImage(file=r"D:\TinkerForm\BMI calculator\scale.png")
  Label(root,image=scale,bg="lightblue").place(x=20,y=310)
  ```

- Lets add the slider for the weight and height
- slider 1

  ``` python
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
  ```
- Slider 2
  ``` python
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
  ```
- now styling the app 

  ``` python
  style2 = ttk.Style()
  style2.configure("TScale",background='white')
  
  slider2 = ttk.Scale(root,from_=0,to=200,orient='horizontal',style='TScale',
                     command=slider_changed2,variable=current_value2)
  slider2.place(x=300,y=250)
  ```
- Add the formula to calculate the BMI of the person defining the function BMI
  ``` python
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
  ``` 

- Adding entry widget to enter the valuse of height and weight of the person

  ``` python
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

  ```

- Adding the image of the man is optional (for me some how it is not working)

``` python
second_image = Label(root,bg="lightblue")
```
- Now adding all the required buttons to calculate the BMI of the person.
  ``` python
  Button(root,text="View Report",width=15,height=2,font='ariel 10 bold',bg="#1f6e68",fg='white',command=BMI).place(x=280,y=340)

  label1 = Label(root,font="ariel 40 bold",bg='lightblue',fg='black')
  label1.place(x=115,y=330)
  
  label2 = Label(root,font="ariel 20 bold",bg='lightblue',fg='black')
  label2.place(x=280,y=405)
  
  label3 = Label(root,font="ariel 10 bold",bg='lightblue',fg='black',justify=LEFT)
  label3.place(x=200,y=450)
  ```

## There you are you have created you BMI app using tkinker.

# Thank you

### The output of the app is shown below
<img align ="center" alt ="Coding" width = "400" src="">













