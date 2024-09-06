from tkinter import *
from tkinter import messagebox, ttk, simpledialog
import json
from datetime import datetime

def create_widget(self):
    main_frame = ttk.Frame(self.root,padding="10")
    main_frame.grid(row=0,column=0,sticky='NEWS')
    input_frame=  ttk.Labelframe(main_frame,text='Add Expence',padding='10')
    input_frame.grid(row=0,column=0,sticky='NEWS',padx=5,pady=5)

    ttk.Label(input_frame,text="Date (YYYY-MM-DD)").grid(row=0,column=0,sticky='W')
    self.date_entry = ttk.Entry(input_frame)
    self.date_entry.grid(row=0,column=1,padx=5,pady=5)

    ttk.Label(input_frame,text='Category:').grid(row=1,column=0,sticky='W')
    self.category_combobox = ttk.Combobox(input_frame,values=self.categories)
    self.category_combobox.grid(row=1,column=1,padx=5,pady=2)
    ttk.Label(input_frame,text="Amount:").grid(row=2,column=0,sticky='W')
    self.amount_entry = ttk.Entry(input_frame)
    self.amount_entry.grid(row=2,column=1,padx=5,pady=2)

    ttk.Button(input_frame,text="Add Expense",command=self.add_expense)

    category_frame = ttk.LabelFrame(main_frame,text="Manage Categories",padding='10')
    category_frame.grid(row=1,column=0,sticky='NEWS',padx=5,pady=5)

    self.new_category_entry = ttk.Entry(category_frame)
    self.new_category_entry.grid(row=0,column=0,padx=5,pady=2)
    ttk.Button(category_frame,text="Add Category",command=self.add_category).grid(row=0,column=1,padx=5,pady=2)


    #display frame
    display_frame = ttk.LabelFrame(main_frame,text="Expense and Budget",padding='10')
    display_frame.grid(row=0,column=1,rowspan=2,sticky="NEWS",padx=5,pady=5)

    




def add_expense(self):
    pass

def add_category(self):
    pass





if __name__ == "__main__":
    root = Tk()
    #app = ExpenceTrackerApp(root)
    root.title("Expence Tracker")
    root.mainloop()