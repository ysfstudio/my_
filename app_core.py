import streamlit as st
import json
import os

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

st.set_page_config(page_title="Instagram Security Test", layout="centered")
st.title("🔓 Instagram Security Test (Simulation)")

username = st.text_input("Enter Instagram Username")

if st.button("Get Credentials"):
    if username:
        data = load_data()
        if username in data:
            st.success("✅ Access granted (SIMULATION ONLY)")
            st.code(f"Verification Code: {data[username]['code']}\nPassword: {data[username]['password']}")
        else:
            st.error("❌ Username not found in local database.")
    else:
        st.warning("Please enter a username.")

st.markdown("---")
st.subheader("Add New User (for simulation)")
new_user = st.text_input("Username")
new_code = st.text_input("Verification Code")
new_pass = st.text_input("Password")
if st.button("Add User"):
    if new_user and new_code and new_pass:
        data = load_data()
        data[new_user] = {"code": new_code, "password": new_pass}
        save_data(data)
        st.success("User added successfully.")
    else:
        st.error("All fields are required.")
