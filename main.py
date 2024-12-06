from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/", summary="Главная ручка", tags=["Основные ручки"])
def main():
    return "Hello world"



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


# myvenv/scripts/activate    
# pip install fastapi[standart] 