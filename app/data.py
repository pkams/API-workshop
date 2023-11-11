from typing import List, Dict

class Produtos:
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

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id: int):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404, "Mensagem":"Produto não encontrado"}

    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        return produto