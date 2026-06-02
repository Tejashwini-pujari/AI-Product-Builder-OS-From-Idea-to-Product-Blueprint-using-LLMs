import streamlit as st
from engine import run_full_pipeline
import json

st.set_page_config(page_title="AI Product Builder OS", layout="wide")

st.title("🚀 AI Product Builder OS")

user_input = st.text_area("Enter your idea")

if st.button("Generate System"):
    if user_input.strip() == "":
        st.warning("Enter an idea")
    else:
        result = run_full_pipeline(user_input)

        st.subheader("📄 PRD")
        st.json(result["PRD"])

        st.subheader("🏗 System Design")
        st.json(result["SYSTEM_DESIGN"])

        st.subheader("⚙ Execution Plan")
        st.json(result["EXECUTION"])

        st.subheader("⚠ Risks")
        st.json(result["RISKS"])

        st.subheader("📊 Evaluation")
        st.json(result["EVALUATION"])