pedidos = []


def adiciona_pedido(nome, sabor):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor

    pedidos.append(pedido)

print(pedidos)
adiciona_pedido('Mario', 'pepperoni')
adiciona_pedido('Luigi', 'mozzarela')
print(pedidos)
