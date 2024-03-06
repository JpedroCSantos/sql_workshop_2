from models.produto import Produto
from database.session import Session


def delete_product(id):
    session = Session()
    produto = session.query(Produto).filter(Produto.id == id).first()
    if not(produto):
        print(f"Product with  {id} not found")
        session.close()
        return
    session.delete(produto)
    session.commit()
    session.close()