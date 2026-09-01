import streamlit as st
import json
import os
import time
import random

DATA_FILE = "exploit_db.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

st.set_page_config(page_title="Exploit Framework v2.0", layout="centered")
st.markdown("""
<style>
    body { background-color: #0a0a0a; }
    .main { background-color: #0a0a0a; }
    .stButton button { background-color: #00ff00; color: #000; }
</style>
""", unsafe_allow_html=True)

st.title("💀 Exploit Framework v2.0")
st.markdown("*Advanced security testing interface*")

username = st.text_input("🎯 Target Instagram Username")

if st.button("🚀 Execute Exploit"):
    if username:
        progress = st.progress(0)
        for i in range(10):
            time.sleep(0.3)
            progress.progress((i+1)*10)
        with st.spinner("Bypassing firewall..."):
            time.sleep(1)
        with st.spinner("Injecting payload..."):
            time.sleep(1)
        with st.spinner("Extracting credentials..."):
            time.sleep(1.5)
        
        data = load_data()
        if username in data:
            st.success("✅ Exploit successful!")
            st.balloons()
            st.code(f"🔑 Verification Code: {data[username]['code']}\n🔐 Password: {data[username]['password']}", language="text")
            st.caption("This is a simulation for educational purposes only.")
        else:
            st.error("❌ Exploit failed. Target not found in database.")
            st.info("Add target to database using the section below.")
    else:
        st.warning("Please enter a target username.")

st.markdown("---")
st.subheader("📡 Add Target to Database")
with st.expander("Register target (for simulation)"):
    new_user = st.text_input("Username")
    new_code = st.text_input("Verification Code")
    new_pass = st.text_input("Password")
    if st.button("Add Target"):
        if new_user and new_code and new_pass:
            data = load_data()
            data[new_user] = {"code": new_code, "password": new_pass}
            save_data(data)
            st.success("Target added to database.")
        else:
            st.error("All fields are required.")
