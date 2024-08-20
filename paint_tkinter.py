from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk

root = Tk()
root.title("Paint Brush")
root.geometry("800x600")
root.configure(bg='white')
root.resizable(False, False)


current_color = "black"


def Show_color(color):
    global current_color
    current_color = color

# List of colors for buttons
colors_list = ["black", "gray", "brown", "red", "orange", "yellow", "green", "blue", "purple", "pink"]


for index, color in enumerate(colors_list):
    Button(root, bg=color, width=3, height=2, command=lambda col=color: Show_color(col)).place(x=10, y=60 + index * 30)


canvas = Canvas(root, width=650, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)


last_x, last_y = None, None

def paint(event):
    global last_x, last_y
    x, y = event.x, event.y
    if last_x and last_y:
        canvas.create_line(last_x, last_y, x, y, fill=current_color, width=2)
    last_x, last_y = x, y

def reset(event):
    global last_x, last_y
    last_x, last_y = None, None

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", reset)







root.mainloop()
