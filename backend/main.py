from fastapi import  FastAPI, HTTPException
from database import get_connection, create_database
from streamlit_app import create_movie, get_all_movies, update_movie, delete_movie
from schemas import MovieCreate, MovieUpdate

app = FastAPI()

create_database()

@app.post("/movies/")
def add_movie(movie: MovieCreate):
    with get_connection() as db:
        return create_movie(db, movie)

@app.get("/movies/")
def list_movies():
    with get_connection() as db:
        return get_all_movies(db)

@app.put("/movies/{movie_id}")
def edit_movie(movie_id: int, movie: MovieUpdate):
    with get_connection() as db:
        if update_movie(db, movie_id, movie) == 0:
            raise HTTPException(status_code=404, detail="Movie not found")
        return {"message": "Movie updated successfully"}

@app.delete("/movies/{movie_id}")
def remove_movie(movie_id: int):
    with get_connection() as db:
        if delete_movie(db, movie_id) == 0:
            raise HTTPException(status_code=404, detail="Movie not found")
        return {"message": "Movie deleted successfully"}
