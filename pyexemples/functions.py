pedidos = []


def criar_pedido(nome, sabor, observacao=None):
    pedido = {}
    pedido['nome'] = nome
    pedido['sabor'] = sabor
    pedido['observacao'] = observacao
    return pedido


pedidos.append(criar_pedido('Mario', 'pepperoni'))
pedidos.append(criar_pedido('Luigi', 'mozzarela', 'dobro de queijo'))

for pedido in pedidos:
    template = 'Nome: {nome}\nSabor: {sabor}'
    print(template.format(**pedido))
    if pedido['observacao']:
        print('Observacao = {}'.format(pedido['observacao']))

    print('-'*30)
