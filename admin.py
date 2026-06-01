# dashboard/admin.py

import streamlit as st

st.title("Instagram Admin Dashboard")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Account",
        "View Accounts",
        "Delete Account"
    ]
)

username = st.text_input("Username")
token = st.text_input("Access Token")

if st.button("Add Account"):
    pass