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


#  python -m venv myvenv       
# myvenv/scripts/activate    

# python3.11 -m venv .venv - где .venv - заданное вами имя создаваемого окружения
# source .venv/bin/activate
# pip install --upgrade pip
#  Возможны 2 случая: 1 - используя командную строку; 2- из ранее созданного файла с версиями пакетов ( requirements.txt)
#      Случай 1:
#     pip install "fastapi[all]"  - после выполнения данной команды установите следующий пакет
#     Случай 2:
#     pip install -r requirements.txt - установит разом все пакеты из указанного txt файла
# Шаг 5. Сохраните версии пакетов если в шаге 4 был случай 1
# pip freeze -> requirements.txt
# Если в процессе работы над проектом потребуется установка каки-либо пакетов, то повторите шаг 4 случай 1, а затем шаг 5. 
# Шаг 6. Выход из вирт. окружения (после завершения работы над проектом) командой
# deactivate

# pip install fastapi[all] 
# pip install uvicorn[standard]
# http://127.0.0.1:8000/docs#
# http://127.0.0.1:8000/redoc#

#  python main.py

# git push -u origin master
# git remote add origin https://github.com/tiger-a/fastapi_tutor.git
# git commit -m "Initial commit"
# git add main.py
