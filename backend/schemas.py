from pydantic import BaseModel
from typing import Optional

class MovieCreate(BaseModel):
    title: str
    director: str
    year: int
    genre: Optional[str]= None

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    director: Optional[str]= None
    year: Optional[str]= None
    genre: Optional[str]= None

class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int
    genre: Optional[str]= None

    class Config:
        orm_mode= True