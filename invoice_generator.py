from tkinter import *
from customtkinter import *
from docxtpl import DocxTemplate
from tkinter import ttk
import datetime
from tkinter import messagebox


def clear_item():
    quantity_entry.delete(0,END)
    quantity_entry.insert(0,"1")
    desc_entry.delete(0,END)
    unit_price_entry.delete(0,END)
    unit_price_entry.insert(0,"1.0")

invoice_list=[]
def add_item():
    qty = int(quantity_entry.get())
    desc = desc_entry.get()
    price = float(unit_price_entry.get())
    line_total = qty*price
    invoice_item = [qty,desc,price,line_total]
    
    tree.insert("",0,values=invoice_item)
    clear_item()

    invoice_list.append(invoice_item)


def new_invoice():
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    phone_number_entry.delete(0,END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()


def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = first_name_entry.get()+" "+last_name_entry.get()
    phone = phone_number_entry.get()
    sub_total = sum(item[3] for item in invoice_list)
    sales_tax = 0.1
    total = sub_total*(1-sales_tax)
    doc.render({
        "Name":name,
        "phone":phone,
        "invoice_list":invoice_list,
        "sub_total":sub_total,
        'salestax': str(sales_tax*100)+"%",
        "Total":total
    })
    doc_name = "New_invoice" + name + datetime.datetime.now().strftime('%Y-%m-%d -%H%M%S')+".docx" 
    doc.save(doc_name)
    messagebox.showinfo("Success", f"Invoice {doc_name} has been generated!")
window = CTk()
window.title("Invoice Generator Form")

frame = Frame(window)
frame.pack(padx=20,pady=20)

first_name_label = Label(frame,text="First Name")
first_name_label.grid(row=0,column=0)

last_name_label = Label(frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = Entry(frame)
first_name_entry.grid(row=1,column=0)

last_name_entry = Entry(frame)
last_name_entry.grid(row=1,column=1)

phone_number = Label(frame,text="Phone Number")
phone_number.grid(row=0,column=3)

phone_number_entry = Entry(frame)
phone_number_entry.grid(row=1,column=3)

quantity_label = Label(frame,text="Quantity")
quantity_label.grid(row=3,column=0)

quantity_entry = Spinbox(frame,from_=1,to=100)
quantity_entry.grid(row=4,column=0)

desc_label = Label(frame,text="Description")
desc_label.grid(row=3,column=1)

desc_entry = Entry(frame)
desc_entry.grid(row=4,column=1)

unit_price_label = Label(frame,text="Unit Price")
unit_price_label.grid(row=3,column=3)

unit_price_entry = Spinbox(frame,from_=1,to=500,increment=0.5)
unit_price_entry.grid(row=4,column=3)

add_Item_label = Button(frame,text="Add Item",command=add_item)
add_Item_label.grid(row=5,column=3,pady=10)


columns = ("Quantity","Description","Price","Total")
tree = ttk.Treeview(frame,columns=columns,show='headings')
tree.grid(row=7,column=0,columnspan=4,padx=10,pady=20)

tree.heading("Quantity",text="Quantity")
tree.heading("Description",text="Description")
tree.heading("Price",text="Price")
tree.heading("Total",text="Total")

save_invoice_button = Button(frame,text="Generate Invoice",command=generate_invoice)
save_invoice_button.grid(row=8,column=0,columnspan=4,sticky='news',padx=10,pady=10)

new_invoice_button = Button(frame,text="New Invoice",command=new_invoice)
new_invoice_button.grid(row=9,column=0,columnspan=4,sticky='news',padx=10,pady=10)


window.mainloop()