import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.linear_model import LinearRegression

df = pd.read_csv('D:\TinkerForm\ML Flask_first app\hiring.csv')
df['experience'] = df['experience'].fillna(0,inplace=True)

df['test_score'] = df['test_score'].fillna(df['test_score'].mean(),inplace=True)

X = df.iloc[:,:3]
def convert_word_to_int(word):
    word_dict = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'ten':10,
        'eleven':11,
        'twelve':12,
        'zero':0,0:0
    }
    return word_dict.get(word)

X['experience'] = X['experience'].apply(lambda x:convert_word_to_int(x))

y = df.iloc[:,-1]

linear = LinearRegression()

linear.fit(X,y)

pickle.dump(linear,open('model.pkl','wb'))