pedidos = [
    {
        'nome': 'Mario',
        'sabor': 'Portuguesa'
    },
    {
        'nome': 'Luigi',
        'sabor': 'Presunto'
    }
]

for pedido in pedidos:
    s = 'Nome: {}\nSabor: {}'
    print(s.format(pedido['nome'], pedido['sabor']))


