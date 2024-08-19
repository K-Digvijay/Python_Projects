import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import *
from tkinter import messagebox, filedialog, simpledialog

root = Tk()
root.title("Data Viewer and Plotter")
root.geometry("800x600")

process_data = None
raw_data = None

def open_file():
    global raw_data
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", ".csv")])
    if file_path:
        try:
            raw_data = pd.read_csv(file_path)
            
            if raw_data.shape[1] < 2:
                raise ValueError("The file must contain at least 2 columns.")
            
            messagebox.showinfo("CSV File", "File loaded successfully!")
            display(raw_data)
            update_listbox_options()  # Update listbox options
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")
            raw_data = None

def display(data):
    text_display.delete(1.0, END)
    text_display.insert(END, data.to_string())

def update_listbox_options():
    # Populate the listboxes with column names
    x_column_listbox.delete(0, END)
    y_column_listbox.delete(0, END)
    
    for col in raw_data.columns:
        x_column_listbox.insert(END, col)
        y_column_listbox.insert(END, col)

def display_plot():
    if raw_data is None:
        messagebox.showerror("Error", "No data loaded!")
        return

    try:
        # Get the selected columns
        x_selection = x_column_listbox.curselection()
        y_selection = y_column_listbox.curselection()
        
        if not x_selection or not y_selection:
            messagebox.showerror("Error", "Please select both X and Y columns.")
            return
        
        x_column = x_column_listbox.get(x_selection)
        y_column = y_column_listbox.get(y_selection)

        # Convert the Y column to numeric values
        y = pd.to_numeric(raw_data[y_column], errors='coerce')

        # Check if X column is categorical or numeric
        if raw_data[x_column].dtype == 'object':
            # Handle categorical vs numeric
            x = raw_data[x_column]
            valid_data = pd.DataFrame({x_column: x, y_column: y}).dropna()

            if valid_data.empty:
                raise ValueError("The selected columns contain only missing data.")

            # Aggregate data for bar plot
            plot_data = valid_data.groupby(x_column)[y_column].mean().reset_index()

            # Create the bar plot
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.barplot(x=x_column, y=y_column, data=plot_data, ax=ax)
            ax.set_title(f"Bar Plot of {x_column} vs {y_column}")
            ax.set_xlabel(x_column)
            ax.set_ylabel(f"Average {y_column}")
        
        else:
            # Handle numeric vs numeric
            x = pd.to_numeric(raw_data[x_column], errors='coerce')
            valid_data = pd.DataFrame({x_column: x, y_column: y}).dropna()

            if valid_data.empty:
                raise ValueError("The selected columns contain only missing data.")

            # Create the scatter plot
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.scatter(valid_data[x_column], valid_data[y_column], marker='o')
            ax.set_title(f"Scatter Plot of {x_column} vs {y_column}")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)

        # Create a new window for the plot
        plot_window = Toplevel(root)
        plot_window.title("Plot Window")
        plot_window.geometry("800x600")

        # Embed plot in the new window
        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        
        # Optionally, add a button to close the plot window
        btn_close = Button(plot_window, text="Close", command=plot_window.destroy)
        btn_close.pack(pady=10)
       
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create plot: {e}")

def process_file():
    global process_data,raw_data
    if raw_data is None:
        messagebox.showerror('Error','File not loaded')
        return
    try:
        columns = list(raw_data.columns)
        column_names = [f"Column {i}" for i in columns]
        column_names_str = "\n".join(f"{i}: {name}" for i, name in enumerate(column_names))
        
        target_col_index = simpledialog.askinteger("Input", f"Enter target column index:\n{column_names_str}")
        target_col_index = simpledialog.askinteger("Input",'Enter target column Index')

        if target_col_index is None or target_col_index<0 or target_col_index >= raw_data.shape[1]:
            raise ValueError("Target column index out of range")



        X = raw_data.drop(columns=[raw_data.columns[target_col_index]])
        y = pd.to_numeric(raw_data.iloc[:,target_col_index],errors='coerce')
        X = X[y.notna()]
        y= y.dropna()

        X = X.reset_index(drop=True)
        y = y.reset_index(drop=True)


        categorical_col = X.select_dtypes(include='object').columns
        numerical_col = X.select_dtypes(include=np.number).columns
        
        
        preprocessor = ColumnTransformer(
            transformers = [
                ("category",OneHotEncoder(handle_unknown='ignore'),categorical_col),
                ('numerical',SimpleImputer(strategy='mean'),numerical_col)
            ],
            remainder = 'passthrough'
        )

        pipeline = Pipeline(steps=[
            ('prepressor',preprocessor),
            ('regressor',LinearRegression())
        ])

        pipeline.fit(X,y)
        y_pred = pipeline.predict(X)
        y_pred_df = pd.DataFrame(y_pred,columns=['predicted_target'])

        process_data = pd.concat([raw_data,y_pred_df],axis=1)

        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        model = pipeline.named_steps['regressor']
        coef = model.coef_
        intercept = model.intercept_
        rmse = np.sqrt(mse)

        messagebox.showinfo("Model Performance",
                            f"Mean Squared Error: {mse:.2f}\n"
                            f"R-squared: {r2:.2f}\n"
                            f"Coefficients: {coef}\n"
                            f"Intercept: {intercept:.2f}\n"
                            f"RMSE: {rmse}")
        

    except Exception as e:
        print(f"Error: {str(e)}")
        messagebox.showerror("Error",f"Failed to process{str(e)}")

    

def save_file():
    global process_data
    if process_data is not None:
        savepath = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[('CSV File','.csv')])
        if savepath:
            try:
                process_data.to_csv(savepath,index=False)
                messagebox.showinfo("Success","File save successfully")
            except Exception as e:
                messagebox.showerror(f'Error File not Saved{str(e)}')
    else:
        messagebox.showerror("Error","No data to save. Please process the data first")



# GUI Elements
frame = Frame(root)
frame.pack(pady=10)

btn_open = Button(frame, text="Open CSV File",width=15,height=2, command=open_file,background='skyblue')
btn_open.grid(row=0, column=0, padx=10)

Label(frame, text="X Column:Categorical Value ").grid(row=1, column=0, padx=10)
x_column_listbox = Listbox(frame, selectmode=SINGLE, height=5, exportselection=False)
x_column_listbox.grid(row=1, column=1, padx=10)

Label(frame, text="Y Column:Numerical Value").grid(row=2, column=0, padx=10)
y_column_listbox = Listbox(frame, selectmode=SINGLE, height=5, exportselection=False)
y_column_listbox.grid(row=2, column=1, padx=10)

btn_plot = Button(frame, text="Display Plot",width=15,height=2, command=display_plot,background='skyblue')
btn_plot.grid(row=0, column=2, columnspan=2, pady=10)



button_process = Button(root,text="Process Data",
                    width=15,height=2,
                    command=process_file,background="skyblue",
                    pady=20)
button_process.pack(padx=10,pady=10)

button_save = Button(root,text="SaveCSV",
                    width=15,height=2,
                    command=save_file,background="skyblue",
                    pady=20)
button_save.pack(padx=10,pady=10)

text_display = Text(root, wrap=NONE, width=80, height=20)
text_display.pack(padx=10, pady=10, fill=BOTH, expand=True)



root.mainloop()
