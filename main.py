from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "Аснхроггость в Python",
        "author": "Мэтью",
    },
    {
        "id": 2,
        "title": "Beckend в Python",
        "author": "Алекс",
    },
]

@app.get("/books",
         tags=["Книги"],
         summary="Получить все книги"
         )
def read_books():
    return books

@app.get("/books{book_id}",
         tags=["Книги"],
         summary="Получить конкретную книгу"
         )
def get_book(book_id: int):
        for book in books:
             if book["id"] == book_id:
                  return book           
        raise HTTPException(status_code=404, detail="книга не надена")       

class NewBook(BaseModel):
     title: str
     author: str   

@app.post ("/books",
         tags=["Книги"],
         summary="Добавить книгу"
         )
def create_book(new_book: NewBook):
     books.append({
          "id": len(books) + 1,
          "title": new_book.title,
          "author": new_book.author,
     })
     return{"success": True, "message": "Книга добавлена ок"}





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


# myvenv/scripts/activate    
# pip install fastapi[standart] 
# http://127.0.0.1:8000/docs#
# http://127.0.0.1:8000/redoc#


# git push -u origin master
# git remote add origin https://github.com/tiger-a/fastapi_tutor.git
# git commit -m "Initial commit"
# git add main.py