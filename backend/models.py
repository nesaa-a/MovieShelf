from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    title: str
    director: str
    year: int
    genre: Optional[str]=None


