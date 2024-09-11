from tkinter import *
from tkinter import messagebox, ttk, simpledialog
import json
from datetime import datetime


class ExpenseTrackerApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Expense Tracker And Budget Planner")
        self.root.geometry()
        self.expenses = []
        self.categories = ['Rent','Food','Entertainment','Car','CreditCards']
        self.monthly_budget = self.get_initial_budget()
        self.create_widgets()
    
    def get_initial_budget(self):
        while True:
            budget = simpledialog.askfloat("Monthly Budget","Enter your monthly budget")
            if budget not in None:
                return budget
            else:
                if messagebox.askyesno("No Budget","You havent Enter your budget Do you want to exit?"):
                    self.root.quit()
                    return 0




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

    self.expense_tree = ttk.Treeview(display_frame,columns=('Date','Category','Amount'),show='headings')
    self.expense_tree.heading('Date',text='Date')
    self.expense_tree.heading('Category',text='Category')
    self.expense_tree.heading('Amount',text='Amount')
    self.expense_tree.grid(row=0,column=0,sticky='NEWS')

    scrollbar = Scrollbar(display_frame,orient=VERTICAL,command=self.expense_tree)
    scrollbar.grid(row=0,column=0,sticky='W',pady=2)
    self.expense_tree.configure(yscrollcommand=scrollbar.set)

    self.budget_label = Label(display_frame,text=f"Montly Budget: {self.monthly_budget:.2f}")
    self.budget_label.grid(row=1,column=0,sticky='NEWS',pady=2)

    self.total_expense_label = Label(display_frame,text='Total Expense: 0.00')
    self.total_expense_label.grid(row=2,column=0,sticky='W',pady=2)

    self.remaining_budget_label = Label(display_frame,text=f"Remaining Budget: {self.montthly_budget:.2f}")
    self.remaining_budget_label.grid(row=3,column=0,sticky='W',pady=2)

    Button(display_frame,text='Save Data',command=self.save_data).grid(row=4,column=0,pady=10)

    self.root.columnconfigure(0,weight=1)
    self.root.roeconfigure(0,weight=1)
    main_frame.columnconfigure(1,weight=1)
    main_frame.rowconfigure(0,weight=1)
    display_frame.columnconfigure(0,weight=1)
    display_frame.rowconfigure(0,weight=1)

    




def add_expense(self):
    pass

def add_category(self):
    pass





if __name__ == "__main__":
    root = Tk()
    app = ExpenseTrackerApp(root)
    
    root.mainloop()