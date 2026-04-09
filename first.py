print("hello")jilohkanzujabxjhmn



import streamlit as st
import requests

st.title("EMS Call Prediction Dashboard")

res = requests.get("http://127.0.0.1:8000/predict-next-hour")
data = res.json()

st.metric("Next Hour Calls", data["predicted_calls"])