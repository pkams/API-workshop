
from fastapi import FastAPI
from .schema import ProdutoSchema
from .data import Produtos
from typing import List

app = FastAPI()

lista_de_produtos = Produtos()

@app.get("/")
def home():
    return {'Ola':'Mundao'}

@app.get("/produtos", response_model=list[ProdutoSchema])
def listar_produtos():
    return lista_de_produtos.listar_produtos()

@app.get("/produto/{id}")
def buscar_produto(id: int):
    return lista_de_produtos.buscar_produto(id)

@app.post("/produtos", response_model=ProdutoSchema)
def adicionar_produto(produto: ProdutoSchema):
    return lista_de_produto.adicionar_produto(produto.model_dump())    