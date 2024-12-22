from sqlite3 import Connection
from backend.schemas import MovieCreate, MovieUpdate

def create_movie(db: Connection, movie: MovieCreate):
    cursor = db.cursor()
    cursor.execute(""" 
        INSERT INTO movies (title, director, year, genre) VALUES(?, ?, ?, ?)
    """, (movie.title, movie.director, movie.year, movie.genre))
    db.commit()
    return {"id": cursor.lastroeid, **movie.dict()}

def get_all_movies(db: Connection):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    return[dict(row) for row in rows]

def update_movie(db: Connection, movie_id: int movie: MovieUpdate):
    cursor = db.cursor()
    fields = []
    values= []

    if movie.title:
        fields.append("title = ?")
        values.append(movie.title)
    if movie.director:
        fields.append("director = ?")
        values.append(movie.director)
    if movie.year:
        fields.append("year = ?")
        values.append(movie.year)
    if movie.genre:
        fields.append("genre = ?")
        values.append(movie.genre)

    values.append(movie_id)
    cursor.execute(f"UPDATE movies SET {', '.join(fields)} WHERE id = ?" values)
    db.commit()
    return cursor.rowcount

def delete_movie(db: Connection, movie_id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    db.commit()
    return cursor.rowcount