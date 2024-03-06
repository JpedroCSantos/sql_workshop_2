from database.init_db import init_db
from crud.create import add_product
from crud.read import consult_products
from crud.update import update_product
from crud.delete import delete_product

init_db()

# Adicionar produtos
add_product("Cadeira Gamer", "Cadeira confortável para jogos", 1200.00, True)
add_product("Workshop Python", "Workshop sobre Python", 300.00, False)

# Consultar produtos
produtos = consult_products()
for produto in produtos:
    print(produto.title, produto.price)

# Atualizar produto
update_product(1, price=1500.00)

# Deletar produto
delete_product(2)

# Consultar produtos após atualizações
produtos = consult_products()
for produto in produtos:
    print(produto.title, produto.price)