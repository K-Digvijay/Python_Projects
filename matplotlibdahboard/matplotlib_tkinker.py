from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

df = pd.read_csv("dummy_product_data.csv")


plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#BE36E6", "#A98CCC"]
)

#chart 1
fig1, ax1 = plt.subplots()
ax1.bar(df['category'],df['price'])
ax1.set_title("Sales by product")
ax1.set_xlabel("category")
ax1.set_ylabel("sales")


fig2,ax2 = plt.subplots()
ax2.barh(df['category'],df['stock_level'])
ax2.set_title("Sales by product")
ax2.set_xlabel("category")
ax2.set_ylabel("stock level")

fig3,ax3 = plt.subplots()
ax3.plot(df['product_name'],df['price'].sort_index())
ax3.set_title("Sales by product")
ax3.set_xlabel("product_name")
ax3.set_ylabel("price")
plt.xticks(rotation=90)

plt.tight_layout()

#creating window
root = Tk()
root.title("DashBoard")
root.state("zoomed")

side_frame = Frame(root,bg="#4C2A85")
side_frame.pack(side='left',fill='y')
label = Label(side_frame,text="DashBoard",bg="#4C2A85",font=30)
label.pack(padx=20,pady=20)

chart_frame = Frame(root)
chart_frame.pack()

upper_frame = Frame(chart_frame)
upper_frame.pack(fill='both',expand=True)
lower_frame = Frame(chart_frame)
lower_frame.pack(fill='both',expand=True)


canvas1 = FigureCanvasTkAgg(fig1,upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side='left',fill='both',expand=True)
canvas2 = FigureCanvasTkAgg(fig2,upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side='right',fill='both',expand=True)
canvas3 = FigureCanvasTkAgg(fig3,lower_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side='bottom',fill='both',expand=True)

root.mainloop()