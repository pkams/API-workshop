from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone que é inteligente",
        "preco": 15000.0,
    },
    {
        "id": 2,
        "nome": "Smart",
        "descricao": "Um telefone",
        "preco": 25000.0,
    },
    {
        "id": 3,
        "nome": "Sma",
        "descricao": "Um inteligente produto",
        "preco": 46000.0,
    }
]

@app.get("/")
def home():
    return {'Ola':'Mundao'}

@app.get("/produtos")
def listar_produtos():
    return produtos
