from flask import  Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    try:
        int_features = [int(x) for x in request.form.values()]
        final = [np.array(int_features)]
        print(int_features)
        print(final)
        predict = model.predict_proba(final)
        output= round(predict[0][1],2)

        if output> 0.5:
            return render_template('index.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
        else:
            return render_template('index.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")
    except ValueError as e:
        # Handle ValueError if conversion to int fails
        return render_template('index.html', pred="Invalid input. Please enter valid numbers.", bhai=str(e))

if __name__ ==('__main__'):
    app.run(debug=True)