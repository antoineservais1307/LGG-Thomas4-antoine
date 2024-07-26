import streamlit as st
import json 
import requests

st.title("Salary Calculator")

st.write("")
st.write("Select your salary, bonus and taxes from the box down below")
salary = st.number_input("Salary")
bonus = st.number_input("Bonus")
taxes = st.number_input("Taxes")

inputs = {"salary": salary, "bonus": bonus, "taxes" : taxes}

if st.button("Calculate salary"):
    res = requests.post(url = "http://127.0.0.1:8000/calculate_salary", data =json.dumps(inputs))

    st.subheader(f"Calulated salary  = {res.text}")