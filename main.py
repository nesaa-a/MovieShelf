from fastapi import FastAPI, HTTPException
from backend import models, crud, database
from backend.schemas import MovieCreate, MovieUpdate

app= FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/login/")
async def login(username: str, password: str):
    if username =="admin" and password == "password":
        return{"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/movies/")
async def ass_movie(movie: MovieCreate):
    return crud.create_movie(movie)

@app.get("/movies/")
async  def view_movies():
    return crud.get_all_movies()

@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, movie: MovieUpdate):
    return crud.update_movie(movie_id, movie)

@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    return crud.delete_movie(movie_id)
