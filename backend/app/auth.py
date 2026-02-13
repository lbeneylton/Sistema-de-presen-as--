from fastapi import APIRouter, Depends

# importando sessão do banco de dados de database.py
from app.core import get_session

# Schemas e Services da Rota Auth


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/")
def login():
    return {"message": "Rotas de autentificação e login"}
