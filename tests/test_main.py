import pytest

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get('/')
    assert response.status_code == 200

def test_ola_mundo_json():
    response = client.get('/')
    print(response)
    assert response.json() == {'Ola':'Mundao'}

def test_listar_Produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_tamanho_lista_de_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3

def test_pega_um_produto():
    response = client.get("/produto/1")
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um telefone que é inteligente",
        "preco": 15000.0,
    }
