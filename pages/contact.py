import streamlit as st
from sendemail import send_email

st.header("CONTACT ME")
with st.form(key="formmail"):
     useremail = st.text_input("your email address")
     rmessage = st.text_area("your message")
     button = st.form_submit_button("submit")
     message= f"""\
Subject: New email from {useremail}
From: {useremail}
{rmessage}
     
     """
     if button:
        send_email(message)
        st.info("your email was sent successfully")
