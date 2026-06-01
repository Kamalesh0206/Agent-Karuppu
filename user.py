# dashboard/user.py

import streamlit as st

st.title("Instagram Publisher")


media = st.file_uploader(
    "Upload Media",
    type=["jpg", "png", "mp4"]
)

caption = st.text_area("Caption")

hashtags = st.text_area("Hashtags")

accounts = st.multiselect(
    "Select Accounts",
    [
        "account1",
        "account2"
    ]
)

if st.button("Publish"):
    pass