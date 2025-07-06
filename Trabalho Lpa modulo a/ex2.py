print('Bem vindo a loja de gelados do Endryus Schmidel\n') #Mensagem de boas vindas
print('-' * 9, 'Cardápio ', '-' * 9) #cardapio
print('-' * 29)

print(' Tamanho  |   Cupuaçu (CP)  |   Açaí (AC)    ')
print('     P    |   R$9.00        |   R$11.00     ')
print('     M    |   R$14.00       |   R$16.00     ')
print('     G    |   R$18.00       |   R$20.00     ') 
valorTotal = 0 #acumulador
while True: #while infinito até usuario não querer fazer mais pedido
    pedidoSabor = str(input('Sabor desejado (CP/AC): ')).upper() #input do sabor
    if pedidoSabor != 'CP' and pedidoSabor != 'AC': #se usuario digitar sabor errado
        print('Sabor inválido! Tente novamente.')
        continue
    pedidoTamanho = str(input('Tamanho desejado (P/M/G): ')).upper() #input do tamanho
    if pedidoTamanho != 'P' and pedidoTamanho != 'M' and pedidoTamanho != 'G': #se usuario digitar tamanho errado
        print('Tamanho inválido! Tente novamente.')
        continue
    if pedidoSabor == 'CP': #aninhamento
        if pedidoTamanho == 'P':
            valorTotal += 9
            print('Você pediu um Cupuaçu tamanho P: R$9.00')
        elif pedidoTamanho == 'M':
            valorTotal += 14
            print('Você pediu um Cupuaçu tamanho M: R$14.00')
        else:
            valorTotal += 18
            print('Você pediu um Cupuaçu tamanho G: R$18.00')
    elif pedidoSabor == 'AC':
        if pedidoTamanho == 'P':
            valorTotal += 11
            print('Você pediu um Açaí tamanho P: R$11.00')
        elif pedidoTamanho == 'M':
            valorTotal += 16
            print('Você pediu um Açaí tamanho M: R$16.00')
        else:
            valorTotal += 20
            print('Você pediu um Açaí tamanho G: R$20.00')
    pedidoOutro = input('Deseja fazer outro pedido? (S/N): ').upper() #input se desejar pedir mais alguma coisa
    if pedidoOutro == 'N':
        break #break fim do programa
print(f'Valor total a ser pago: R${valorTotal:.2f}') #print do total usando variavel