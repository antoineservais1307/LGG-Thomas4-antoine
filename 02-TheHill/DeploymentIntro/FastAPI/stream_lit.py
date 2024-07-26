import streamlit as st
import json 
import requests

st.title("✖️➗➕➖ Basic Calculator App ✖️➗➕➖")

option = st.selectbox("What operation you want to perform", 
                      ("Addition", "Substraction" ,"Multiplication","Division"))
st.write("")
st.write("Select the numbers from slider below")
x = st.slider("X" , 0, 100, 20)
y = st.slider("Y" , 0, 420, 10)

inputs = {"operation" : option, "x":x ,"y":y}

if st.button('Calculate'):
    res = requests.post(url = "http://127.0.0.1:8000/calculate", data= json.dumps(inputs))

    st.subheader(f"Reponse from Api = {res.text}")