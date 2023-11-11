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
        "nome": "TV",
        "descricao": "Uma TV 4K",
        "preco": 25000.0,
    },
    {
        "id": 3,
        "nome": "Livro",
        "descricao": "Um livro maneiro",
        "preco": 40.0,
    }
]

@app.get("/")
def home():
    return {'Ola':'Mundao'}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produto/{id}")
def buscar_produto(id: int):
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return {"Status": 404, "Mensagem":"Produto não encontrado"}