from models.produto import Produto
from database.session import Session
from typing import Dict
import json


def update_product(id, **kwargs):
    session = Session()
    produto = session.query(Produto).filter(Produto.id == id).first()
    if not(produto):
        print(f"Product with  {id} not found")
        session.close()
        return
    for chave, valor in kwargs.items():
        if hasattr(produto, chave): # Usamos hasattr(produto, chave) para verificar se o atributo com o nome da chave existe no objeto Produto
            setattr(produto, chave, valor) #usamos setattr(produto, chave, valor) para definir dinamicamente o valor do atributo no objeto Produto.
        else:
            print(f"Atributo '{chave}' não existe em Produto.")
    session.commit()
    session.close()