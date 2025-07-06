def descontoProduto(valor): #função para calcular desconto
    if valor >= 10000:
        return valor - (valor * 11 / 100)
    elif valor >= 6000 and valor < 10000:
        return valor - (valor * 7 / 100)
    elif valor >= 2500 and valor < 6000:
        return valor - (valor * 4 / 100)
    else:
        return valor
print('- ' * 30)
print('Bem vindo a loja de Endryus Schmidel') #boas vindas
valorInicial = float(input('Entre com o valor do produto: ')) #receber valor
quantidadeProduto = int(input('Entre com a quatidade do produto: ')) #receber quantidade
valorMaisQuantidade = valorInicial * quantidadeProduto #calculo do valor e quantidade
print(f'O valor sem desconto é R${valorMaisQuantidade:.2f}') #valor sem desconto
print(f'O valor com desconto é R${descontoProduto(valorMaisQuantidade):.2f}') #valor com desconto (se tiver)
print('- ' * 30)
