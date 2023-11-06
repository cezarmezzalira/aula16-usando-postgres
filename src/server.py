from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.config.database import create_db_and_tables, get_session
from src.models.manutencao_model import Manutencao


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "hello world"}

@app.post("/manutencoes")
def criar_manutencao(manutencao: Manutencao):
    with get_session() as session:
        session.add(manutencao)
        session.commit()
        session.refresh(manutencao)
        return manutencao