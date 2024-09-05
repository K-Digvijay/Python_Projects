from tkinter import *
from tkinter import messagebox, ttk, simpledialog
import json
from datetime import datetime

def create_widget(self):
    main_frame = ttk.Frame(self.root,padding="10")
    main_frame.grid(row=0,column=0,sticky="NEWS")
    input_frame=  ttk.Labelframe(main_frame,text='Add Expence',padding='10')
    input_frame.grid(row=0,column=0,sticky='NEWS',padx=5,pady=5)

    ttk.Label(input_frame,text="Date (YYYY-MM-DD)").grid(row=0,column=0,sticky='W')
    self.date_entry = ttk.Entry(input_frame)
    self.date_entry.grid(row=0,column=1,padx=5,pady=5)

    







if __name__ == "__main__":
    root = Tk()
    #app = ExpenceTrackerApp(root)
    root.title("Expence Tracker")
    root.mainloop()