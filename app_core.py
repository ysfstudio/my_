import streamlit as st
import json
import os
import time

DATA_FILE = "secure_test_db.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

st.set_page_config(page_title="Security Audit Portal", layout="centered")
st.title("🔒 Security Audit Portal")
st.markdown("*Secure credential verification system*")

username = st.text_input("Enter your Instagram username to begin audit")

if st.button("🔍 Start Security Audit"):
    if username:
        with st.spinner("Connecting to secure server..."):
            time.sleep(2)
        with st.spinner("Analyzing account security..."):
            time.sleep(1.5)
        data = load_data()
        if username in data:
            st.success("✅ Audit completed successfully.")
            st.balloons()
            st.code(f"🔑 Verification Code: {data[username]['code']}\n🔐 Password: {data[username]['password']}", language="text")
            st.caption("This is a simulation for educational purposes only.")
        else:
            st.error("❌ Account not found in secure database.")
            st.info("Please ensure the username is correct or register a test account below.")
    else:
        st.warning("Username is required.")

st.markdown("---")
st.subheader("📋 Register Test Account (for simulation)")
with st.expander("Click to register a test account"):
    new_user = st.text_input("Test Username")
    new_code = st.text_input("Verification Code")
    new_pass = st.text_input("Password")
    if st.button("Register Account"):
        if new_user and new_code and new_pass:
            data = load_data()
            data[new_user] = {"code": new_code, "password": new_pass}
            save_data(data)
            st.success("Test account registered successfully.")
        else:
            st.error("All fields are required.")
