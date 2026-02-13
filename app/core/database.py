"""
Este arquivo utiliza a classe de configuração do settings.py 
para criar a engine do SQLAlchemy e a sessão para o ORM gerenciar a engine.

Engine = gerenciador de conexões com o banco (connection pool)
Session_Local = unidade de trabalho do ORM usada para executar queries e transações
sessionmaker = Fábrica de sessões do banco usada pelo ORM

A função get_session é uma função geradora que fornece uma sessão do banco para cada requisição
(utilizando yield para criar uma sessão do banco de dados para cada operação,
garantindo que a sessão seja fechada após o uso).
"""
from .config import DB_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# o settings é uma instancia da classe de configuraçoes

# Cria o engine do SQLAlchemy para comunicação com o banco
# echo=False para não exibir as consultas SQL no console
engine = create_engine(DB_settings.sqlalchemy_url, echo=False)

# configura a sessão para o ORM gerenciar a engine e retorna
Session_Local = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=True
)

# Função para entre contínua da sessão
# Cada operação precisara de uma sessão propria


def get_session():
    db = Session_Local()

    try:
        yield db
    finally:
        db.close()
