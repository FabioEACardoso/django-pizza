pedidos = []


def criar_pedido(nome, sabor, observacao='sem observacoes'):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor
    pedido['observacao'] = observacao
    return pedido

print(pedidos)
pedidos.append(criar_pedido('Mario', 'pepperoni'))
pedidos.append(criar_pedido('Luigi', 'mozzarela'))
print(pedidos)
