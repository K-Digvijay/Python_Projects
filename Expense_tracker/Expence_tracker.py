from tkinter import *
from tkinter import messagebox, ttk, simpledialog,filedialog
import json
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter





class ExpenseTrackerApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Expense Tracker And Budget Planner")
        self.root.geometry("900x600")
        self.expenses = []
        self.categories = ['Rent','Food','Entertainment','Car','CreditCards']
        self.monthly_budget = self.get_initial_budget()
        self.create_widget()
    
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

        ttk.Button(input_frame,text="Add Expense",command=self.add_expense).grid(row=2,column=2)

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

        scrollbar = Scrollbar(display_frame,orient=VERTICAL,command=self.expense_tree.yview)
        scrollbar.grid(row=0,column=1,sticky='NS')
        self.expense_tree.configure(yscrollcommand=scrollbar.set)

        self.budget_label = Label(display_frame,text=f"Montly Budget: {self.monthly_budget:.2f}")
        self.budget_label.grid(row=1,column=0,sticky='NEWS',pady=2)

        self.total_expense_label = Label(display_frame,text='Total Expense: 0.00')
        self.total_expense_label.grid(row=2,column=0,sticky='W',pady=2)

        self.remaining_budget_label = Label(display_frame,text=f"Remaining Budget: {self.monthly_budget:.2f}")
        self.remaining_budget_label.grid(row=3,column=0,sticky='W',pady=2)

        Button(display_frame,text='Save Data',command=self.save_data).grid(row=4,column=0,pady=10)

        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        main_frame.columnconfigure(1,weight=1)
        main_frame.rowconfigure(0,weight=1)
        display_frame.columnconfigure(0,weight=1)
        display_frame.rowconfigure(0,weight=1)
    
    def get_initial_budget(self):
        while True:
            budget = simpledialog.askfloat("Monthly Budget","Enter your monthly budget")
            if budget is not None:
                return budget
            else:
                if messagebox.askyesno("No Budget","You havent Enter your budget Do you want to exit?"):
                    self.root.quit()
                    return 0



    def add_expense(self):
        try:
            date = self.date_entry.get()
            category = self.category_combobox.get()
            amount = float(self.amount_entry.get())

            self.expenses.append({
                'date':date,
                'category':category,
                'amount':amount
            })

            self.update_expense_list()
            self.update_budget_info()
            self.clear_input_fields()
        
        except ValueError:
            messagebox.showerror("Error","Invalid Input. Please check your entries")
        

    def add_category(self):
        new_category = self.new_category_entry.get().strip()
        if new_category and new_category not in self.categories:
            self.categories.append(new_category)
            self.category_combobox['values'] = self.categories
            self.new_category_entry.delete(0,END)
            messagebox.showinfo("Category Added",f"{new_category} Has been added")
        else:
            messagebox.showerror("Error","Invalid category name or category already exists")



    def update_expense_list(self):
        for item in self.expense_tree.get_children():
            self.expense_tree.delete(item)
        for expense in self.expenses:
            self.expense_tree.insert('', 'end', values=(
                expense['date'],
                expense['category'],
                f"Rs {expense['amount']:.2f}"
            ))

    def update_budget_info(self):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        remaining_budget = self.monthly_budget - total_expenses

        self.total_expense_label.config(text=f"Total Expenses: Rs {total_expenses:.2f}")
        self.remaining_budget_label.config(text=f"Remaining Budget: Rs {remaining_budget:.2f}")

    def clear_input_fields(self):
        self.date_entry.delete(0, END)
        self.category_combobox.set('')
        self.amount_entry.delete(0, END)

    def save_data(self):
        data = {
            'budget': self.monthly_budget,
            'categories': self.categories,
            'expenses': self.expenses
        }
        
        # Get the current date to use in the filename
        current_date = datetime.now().strftime("%Y-%m")
        pdf_filename = f"expense_data_{current_date}.pdf"

        c = canvas.Canvas(pdf_filename, pagesize=letter)
        width, height = letter

        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 50, "Expense Tracker Report")
        
        # Budget
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 100, f"Monthly Budget: Rs {data['budget']:.2f}")
        
        # Categories
        y = height - 130
        c.drawString(100, y, "Categories:")
        for category in data['categories']:
            y -= 20
            c.drawString(120, y, f"- {category}")
        
        # Expenses
        y -= 20
        c.drawString(100, y, "Expenses:")
        for expense in data['expenses']:
            y -= 20
            date = expense.get('date', 'N/A')
            category = expense.get('category', 'N/A')
            amount = expense.get('amount', 0)
            c.drawString(120, y, f"Date: {date}, Category: {category}, Amount: Rs {amount:.2f}")
        
        c.save()
        messagebox.showinfo("Save Successful", f"Data saved to {pdf_filename}")
        
        '''file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            initialfile=default_filename
        )
        
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Save Successful", f"Data saved to {file_path}")
'''
if __name__ == "__main__":
    root = Tk()
    app = ExpenseTrackerApp(root)
    
    root.mainloop()