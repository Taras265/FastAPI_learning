from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()

BOOKS = []


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    rating: int


@app.get("/")
async def read_all_books():
    return BOOKS


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book
