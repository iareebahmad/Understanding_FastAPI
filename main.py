from fastapi import FastAPI

app = FastAPI()

books = [
    {'Title': 'Title One', 'Author': 'Author One', 'category': 'science'},
    {'Title': 'Title Two', 'Author': 'Author Two', 'category': 'science'},
    {'Title': 'Title Three', 'Author': 'Author Three', 'category': 'history'},
    {'Title': 'Title Four', 'Author': 'Author Four', 'category': 'math'},
    {'Title': 'Title Five', 'Author': 'Author Five', 'category': 'math'},
    {'Title': 'Title Six', 'Author': 'Author Six', 'category': 'math'}
]
@app.get("/",summary="Index Page Loading", description="Returns the welcome message")
def get_all_books():
    return {'Message':'Hello Hi! Welcome to the API Application'}


@app.get("/books", summary="Get all books", description="Returns the full list of available books.")
def get_all_books():
    return books

@app.get("/books/{dynamic_param}", summary="Get book by dynamic param", description="Returns the value of the dynamic path parameter.")
def get_all_books(dynamic_param: str):
    return {'dynamic_param': dynamic_param}

@app.get("/books/mybook",summary="Get my Fav Book", description="Returns my fav book")
def get_all_books():
    return {'Book Title':'My fav Book'}

