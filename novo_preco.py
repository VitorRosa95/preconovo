preco_antigo = int(input('digite o preço antigo.\n'))


#até 50 preço antigo
if preco_antigo <= 50:
    preco_novo = preco_antigo+(5*preco_antigo)/100
    if preco_novo <= 80:
        print('Barato\n')
    if preco_novo > 80 and preco_novo <= 120:
        print('Normal\n')
    if preco_novo > 120 and preco_novo <= 200:
        print('Caro\n')
    if preco_novo > 200:
        print('Muito caro\n')

#entre 50 e 100 preço antigo
if preco_antigo > 50 and preco_antigo <= 100:
    preco_novo = preco_antigo+(10 * preco_antigo) / 100
    if preco_novo <= 80:
        print('Barato\n')
    if preco_novo > 80 and preco_novo <= 120:
        print('Normal\n')
    if preco_novo > 120 and preco_novo <= 200:
        print('Caro\n')
    if preco_novo > 200:
        print('Muito caro\n')

# acima de 100 preço antigo
if preco_antigo > 100:
    preco_novo = preco_antigo+(15*preco_antigo)/100
    if preco_novo <= 80:
        print('Barato\n')
    if preco_novo > 80 and preco_novo <= 120:
        print('Normal\n')
    if preco_novo > 120 and preco_novo <= 200:
        print('Caro\n')
    if preco_novo > 200:
        print('Muito caro\n')
