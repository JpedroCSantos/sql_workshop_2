from models.produto import Produto
from database.session import Session


def add_product(titulo, descricao, preco, available):
    session = Session()
    novo_produto = Produto(title=titulo, description=descricao, price=preco, available=available)
    session.add(novo_produto)
    session.commit()
    session.close()