import streamlit as st
import pandas as pd
import os
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score
from sklearn.linear_model import LogisticRegression



with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png")
    st.title("Streamlit ML")
    choice = st.radio("Navigation",['upload','profiling','ML','Download'])
    st.info("This application allows you to built ML pipelone")

st.write("Hello World new edit")

if os.path.exists("submission.csv"):
    df= pd.read_csv('submission.csv',index_col=None)

if choice == "upload":
    st.title("Ulpoad your data for ML")
    file = st.file_uploader("upload you dataset")
    if file:
        df = pd.read_csv(file,index_col=None)
        df.to_csv("submission.csv",index=None)
        st.dataframe(df)

if choice =='profiling':
    st.title("Explotatry Data Analysis")
    profile_report = ProfileReport(df)
    st_profile_report(profile_report)
else:
    st.warning("Please upload a dataset first.")

if choice == "ML":
    st.title("machine Learning")
    target = st.select_box("Train Model",df.columns)
    if target:
        X = df.drop(columns=[target])
        y = df[target]
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state = 42)
        model = LogisticRegression()
        model.fit(X_train,y_train)
        y_pred = model.predict(X_test)

        st.info("Model Metrics")
        st.write("Mean square error",mean_squared_error(y_test,y_pred))
        st.write("R-square",r2_score(y_test,y_pred))
        st.write("Accuracy",accuracy_score(y_test,y_pred))

        st.info("feature Importance")
        feature_importances = pd.DataFrame(model.feature_importances_, index=X.columns, columns=['Importance']).sort_values('Importance', ascending=False)

if choice == 'download':
    with open('best_model.pkl', 'rb') as f: 
    st.download_button('Download Model', f, file_name="best_model.pkl")


