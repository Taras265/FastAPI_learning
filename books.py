from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

BOOKS = []


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of book", min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

    class Config:
        schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "title": "Examples",
                "author": "No name",
                "description": "Interesting description",
                "rating": 75
            }
        }


@app.get("/")
async def read_all_books(books_to_return):
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i += 1
        return new_books
    return BOOKS


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book
