from flask import  Flask,render_template,request
import pandas as pd
import pickle
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
model = pickle.load('model.pkl','rb')








if __name__ ==('__main__'):
    app.run(debug=True)