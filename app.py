import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="AI Career Predictor", page_icon="🚀")

st.title("🚀 AI Career Predictor Pro")
st.write("AI-powered system that recommends best tech career for you")

model = pickle.load(open("model.pkl", "rb"))

st.subheader("Enter your skills")

col1, col2 = st.columns(2)

with col1:
    python = st.slider("Python", 0, 10)
    java = st.slider("Java", 0, 10)
    web = st.slider("Web", 0, 10)

with col2:
    math = st.slider("Math", 0, 10)
    ai = st.slider("AI Interest", 0, 10)
    cgpa = st.slider("CGPA", 0.0, 10.0)

if st.button("Predict My Career 🔮"):
    data = np.array([[python, java, web, math, ai, cgpa]])
    prediction = model.predict(data)[0]

    st.success(f"🎯 Recommended Career: {prediction}")

    if prediction == "AI Engineer":
        st.info("Focus on Python, ML, Deep Learning, Projects")
    elif prediction == "Web Developer":
        st.info("Focus on React, JS, Full Stack")
    elif prediction == "Data Scientist":
        st.info("Focus on Python, SQL, Statistics")
