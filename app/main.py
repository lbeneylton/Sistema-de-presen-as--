from fastapi import FastAPI
# importando sessão do banco de dados de database.py
from app.core import get_session
from app.auth import auth_router

app = FastAPI()
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Bem-vindo ao sistema de presenças!"}
