import streamlit as st

def login_form():

    st.title("Login to MovieShelf")
    st.write("Please enter your credentials to access the platform.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid username or password.")
            return False

    return False
