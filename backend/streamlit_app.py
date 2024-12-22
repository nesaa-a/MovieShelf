import streamlit as st
from login_form import login_form
import os
import base64

def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def main():
    # Merr drejtimin aktual të skedarit
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Rruga e logos
    logo_path = os.path.join(current_dir, "logo.png")  # Ose ndrysho në "assets/MovieShelf.png" nëse ndodhet në një dosje 'assets'

    # Shfaq logon në anën e majtë të faqes
    if os.path.exists(logo_path):
        logo_base64 = get_image_as_base64(logo_path)
        logo_html = f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
            <img src="data:image/png;base64,{logo_base64}" style="max-width: 100%; height: auto; width: 300px;">
        </div>
        """
        with st.sidebar:
            st.markdown(logo_html, unsafe_allow_html=True)

# Thirret funksioni i login-it
is_logged_in = login_form()

# Nëse login është i suksesshëm, shfaq pjesën tjetër të aplikacionit
if is_logged_in:
    st.sidebar.title("Menu")
    menu = ["View Movies", "Add Movie", "Update Movie", "Delete Movie"]
    choice = st.sidebar.selectbox("Choose an action", menu)

    if choice == "View Movies":
        st.subheader("View Movies")
        st.write("Here is the list of all movies...")

    elif choice == "Add Movie":
        st.subheader("Add a New Movie")
        title = st.text_input("Movie Title")
        description = st.text_area("Description")
        year = st.number_input("Release Year", min_value=1800, max_value=2024, step=1)
        if st.button("Add Movie"):
            st.success(f"Movie '{title}' added successfully!")

    elif choice == "Update Movie":
        st.subheader("Update a Movie")
        movie_id = st.number_input("Movie ID", min_value=1, step=1)
        title = st.text_input("New Title")
        description = st.text_area("New Description")
        year = st.number_input("New Release Year", min_value=1800, max_value=2024, step=1)
        if st.button("Update Movie"):
            st.success("Movie updated successfully!")

    elif choice == "Delete Movie":
        st.subheader("Delete a Movie")
        movie_id = st.number_input("Movie ID", min_value=1, step=1)
        if st.button("Delete Movie"):
            st.success("Movie deleted successfully!")
