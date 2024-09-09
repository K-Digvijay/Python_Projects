import streamlit as st

st.title("welcome to streamlit")
st.header("This is header")
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png")
    st.title("Streamlit ML")
    choice = st.radio("Navigation",['upload','profiling','ML','Download'])
    st.info("This application allows you to built ML pipelone")