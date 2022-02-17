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


@app.post("/")
async def create_book(title, author):
    current_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if current_id < x:
                current_id = x
    BOOKS[f'book_{current_id+1}'] = {'title': title, 'author': author}
    return BOOKS[f'book_{current_id+1}']


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_info = {"title": book_title, "author": book_author}
    BOOKS[book_name] = book_info
    return book_info


@app.delete("/{book_name}")
async def delete_book(book_name: str):
    del BOOKS[book_name]
    return f'Book {book_name} was deleted.'
