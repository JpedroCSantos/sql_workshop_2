from models.produto import Produto
from database.session import Session


def consult_products():
    session = Session()
    produtos = session.query(Produto).all()
    session.close()
    return produtos