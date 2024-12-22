import os
import base64
import streamlit as st
from login_form import login_form
from streamlit_app import get_all_movies, add_movie, delete_movie, update_movie
from database import create_database, get_connection

create_database()

def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo.png")

    if os.path.exists(logo_path):
        logo_base64 = get_image_as_base64(logo_path)
        logo_html = f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
            <img src="data:image/png;base64,{logo_base64}" style="max-width: 100%; height: auto; width: 300px;">
        </div>
        """
        with st.sidebar:
            st.markdown(logo_html, unsafe_allow_html=True)

    if login_form():
        st.sidebar.title("Menu")
        option = st.sidebar.radio("Select an option", ["Home", "Add Movie", "Delete Movie", "Update Movie", "View Movies"])

        if option == "Home":
            st.title("Welcome to MovieShelf")
            st.write("Navigate through the menu to manage your movies!")

        elif option == "Add Movie":
            st.title("Add a Movie")
            title = st.text_input("Title")
            director = st.text_input("Director")
            year = st.number_input("Year", min_value=1800, max_value=2100, step=1)
            genre = st.text_input("Genre (optional)")

            if st.button("Add Movie"):
                with get_connection():
                    add_movie(title, director, year, genre)
                    st.success("Movie added successfully!")

        elif option == "Delete Movie":
            st.title("Delete a Movie")
            movie_id = st.number_input("Enter the movie ID to delete", min_value=1, step=1)

            if st.button("Delete Movie"):
                with get_connection() as db:
                    if delete_movie(db, movie_id) > 0:
                        st.success("Movie deleted successfully!")
                    else:
                        st.error("Movie not found!")

        elif option == "Update Movie":
            st.title("Update a Movie")
            movie_id = st.number_input("Enter the movie ID to update", min_value=1, step=1)
            title = st.text_input("Title (leave blank to keep current)")
            director = st.text_input("Director (leave blank to keep current)")
            year = st.number_input("Year (enter 0 to keep current)", min_value=0, max_value=2100, step=1)
            genre = st.text_input("Genre (optional)")

            if st.button("Update Movie"):
                with get_connection() as db:
                    updated_fields = {}
                    if title: updated_fields['title'] = title
                    if director: updated_fields['director'] = director
                    if year != 0: updated_fields['year'] = year
                    if genre: updated_fields['genre'] = genre

                    if update_movie(db, movie_id, updated_fields):
                        st.success("Movie updated successfully!")
                    else:
                        st.error("Movie not found!")

        elif option == "View Movies":
            st.title("All Movies")
            with get_connection() as db:
                movies = get_all_movies(db)
                if movies:
                    st.table(movies)
                else:
                    st.write("No movies found!")

if __name__ == "__main__":
    main()
