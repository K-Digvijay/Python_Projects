from flask import  Flask,render_template,request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from joblib import dump,load
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly as po
import uuid

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html',href='static/X.svg')
    else:
        text = request.form['text']
        random_str = uuid.uuid4().hex
        path = 'static/'+random_str+'.svg'
        model = load('model.joblib')
        numpy_arry = Float_string_to_numpy_array(text)
        Make_Picture('AgesAndHeights.pkl',model,numpy_arry,path)

        return render_template('index.html',href=path)
        
def Make_Picture(training_data_filemane,Model,New_input_np_arr,Output_file):
    data = pd.read_pickle(training_data_filemane)
    ages = data['Age']
    data = data[ages>0]
    ages = data['Age']
    height = data['Height']
    age_np = ages.to_numpy()
    height_np = data['Height'].to_numpy()
    age_np_reshape = age_np.reshape(len(ages),1)
    # height_np_reshape = height_np.reshape(len(height_np),1)
    model = LinearRegression().fit(age_np_reshape,height_np)

    X_new = np.array(list(range(19))).reshape(19,1)
    pred = model.predict(X_new)
    fig = px.scatter(x=ages,y=data['Height'],title='Height vs age',
                 labels={'x':'age','y':'height'})

    fig.add_trace(go.Scatter(x=X_new.reshape(19),y=pred,mode = 'lines',
                            name='Model'))
    new_pred = model.predict(New_input_np_arr)
    fig.add_trace(go.Scatter(x=New_input_np_arr.reshape(len(New_input_np_arr)),y=new_pred,
                                                        name='New_output',
                                                        mode='markers',
                                                        marker = dict(color='purple',size=20,line=dict(color='purple',width=2))))
    fig.write_image(Output_file,width=800,engine='kaleido')
    
    fig.show()

def Float_string_to_numpy_array(float_str):
    def is_float(s):
        try:
            float(s)
            return True
        except:
            return False
    float_values = [x for x in float_str.split(',') if x.strip() and is_float(x)]
    float_array = np.array([float(x) for x in float_values])
    return float_array.reshape(len(float_array),1)



if __name__ == '__main__':
    app.run(debug=True)
