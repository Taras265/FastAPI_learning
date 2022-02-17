from fastapi import FastAPI
from enum import Enum

app = FastAPI()


BOOKS = {
    'book_1': {'title': 'Title 1', 'author': 'Author 1'},
    'book_2': {'title': 'Title 2', 'author': 'Author 2'},
    'book_3': {'title': 'Title 3', 'author': 'Author 3'},
    'book_4': {'title': 'Title 4', 'author': 'Author 4'},
    'book_5': {'title': 'Title 5', 'author': 'Author 5'},
}


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]

