import tkinter as tk
from tkinter import filedialog,simpledialog
import numpy as np
import pandas as pd
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


process_data = None
raw_data  = None

def open_file():
    global raw_data
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files",".csv")])
    if filepath:
        try:
            if not  filepath:
                raise ValueError("No file selected")

            raw_data = pd.read_csv(filepath,header=None)
            if raw_data.shape[1]<2:
                raise ValueError("The file must have atleast 2 columns")
            
            print("Loaded Data: ")
            print(raw_data.head())

            messagebox.showinfo("Info","File loaded Sucessfully")
            display_data(raw_data)
        except Exception as e:
            messagebox.showerror("Error","Fail to open file{e}")
            raw_data =None

def display_data(data):
    # Clear the previous text
    text_display.delete(1.0, tk.END)
    # Convert DataFrame to string and insert it into the Text widget
    text_display.insert(tk.END, data.to_string())

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

root=tk.Tk()
root.title("classification")

root.geometry("600x600")

button1 = tk.Button(root,text="OpenCSV",
                    width=15,height=2,
                    command=open_file,background="skyblue",
                    pady=20)
button1.pack(padx=10,pady=10)
button3 = tk.Button(root,text="Process Data",
                    width=15,height=2,
                    command=process_file,background="skyblue",
                    pady=20)
button3.pack(padx=10,pady=10)

button2 = tk.Button(root,text="SaveCSV",
                    width=15,height=2,
                    command=save_file,background="skyblue",
                    pady=20)
button2.pack(padx=10,pady=10)

text_display = tk.Text(root, wrap=tk.NONE, width=80, height=20)
text_display.pack(padx=10, pady=10)



root.mainloop()