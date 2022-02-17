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


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
async def read_all_books():
    return BOOKS


@app.get("/books/mybook")
async def read_book():
    return {"book_title": "My favourite book"}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_title": book_id}


@app.get("/direction/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.south:
        return {"direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.west:
        return {"direction": direction_name, "sub": "Left"}
    return {"direction": direction_name, "sub": "Right"}

