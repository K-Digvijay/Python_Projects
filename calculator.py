import tkinter as tk

calcualtion = ""
def add_to_calculation(symbol):
    global calcualtion
    calcualtion += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0,calcualtion)

def evaluate_calculation():
    global calcualtion
    try:
        result = str(eval(calcualtion))
        calcualtion = ""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)

    except:
        clear_field()
        text_result.insert(1.0,"Error")
        pass

def clear_field():
    global calcualtion
    calcualtion =""
    text_result.delete(1.0,"end")



root = tk.Tk()
root.geometry()
text_result = tk.Text(root,height=2,width=16,font=('Ariel',24))
text_result.grid(columnspan=5)
root.title("Calculator")

button1 = tk.Button(root,text="1",command=(lambda:add_to_calculation(1)),width=5)
button1.grid(row=2,column=1)
button2 = tk.Button(root,text="2",command=(lambda:add_to_calculation(2)),width=5)
button2.grid(row=2,column=2)
button3 = tk.Button(root,text="3",command=(lambda:add_to_calculation(3)),width=5)
button3.grid(row=2,column=3)
button4 = tk.Button(root,text="4",command=(lambda:add_to_calculation(4)),width=5)
button4.grid(row=3,column=1)
button5 = tk.Button(root,text="5",command=(lambda:add_to_calculation(5)),width=5)
button5.grid(row=3,column=2)
button6 = tk.Button(root,text="6",command=(lambda:add_to_calculation(6)),width=5)
button6.grid(row=3,column=3)
button7 = tk.Button(root,text="7",command=(lambda:add_to_calculation(7)),width=5)
button7.grid(row=4,column=1)
button8 = tk.Button(root,text="8",command=(lambda:add_to_calculation(8)),width=5)
button8.grid(row=4,column=2)
button9 = tk.Button(root,text="9",command=(lambda:add_to_calculation(9)),width=5)
button9.grid(row=4,column=3)
button0 = tk.Button(root,text="0",command=(lambda:add_to_calculation(0)),width=5)
button0.grid(row=5,column=2)


button_plus = tk.Button(root,text="+",command=(lambda:add_to_calculation("+")),width=5)
button_plus.grid(row=2,column=4)
button_minus = tk.Button(root,text="-",command=(lambda:add_to_calculation("-")),width=5)
button_minus.grid(row=3,column=4)
button_multiply = tk.Button(root,text="*",command=(lambda:add_to_calculation("*")),width=5)
button_multiply.grid(row=4,column=4)
button_divide = tk.Button(root,text="/",command=(lambda:add_to_calculation("/")),width=5)
button_divide.grid(row=5,column=4)

button_open = tk.Button(root,text="(",command=(lambda:add_to_calculation("(")),width=5)
button_open.grid(row=5,column=1)
button_close = tk.Button(root,text=")",command=(lambda:add_to_calculation(")")),width=5)
button_close.grid(row=5,column=3)

button_clear = tk.Button(root,text="C",command=clear_field,width=11)
button_clear.grid(row=6,column=2)

button_equal = tk.Button(root,text="=",command=(evaluate_calculation),width=11)
button_equal.grid(row=6,column=3)





tk.mainloop()