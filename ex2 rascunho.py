print('Bem vindo a loja de gelados do Endryus Schmidel\n')
print('-' * 9, 'Cardápio ', '-' * 9)
print('-' * 29)

print(' Tamanho  |   Cupuaçu (CP)  |   Açaí (AC)    ')
print('     P    |   R$9.00        |   R$11.00     ')
print('     M    |   R$14.00       |   R$16.00     ')
print('     G    |   R$18.00       |   R$20.00     ')
pedidoOutro = 'S'
valorTotal = 0
while pedidoOutro == 'S':
    try: 
        pedidoSabor = str(input('Sabor desejado (CP/AC): ')).upper()
        while pedidoSabor != 'CP' and pedidoSabor != 'AC':
            print('Sabor inválido! Tente novamente.')
            pedidoSabor = str(input('Sabor desejado (CP/AC): ')).upper()
        pedidoTamanho = str(input('Tamanho desejado (P/M/G): ')).upper()
        while pedidoTamanho != 'P' and pedidoTamanho != 'M' and pedidoTamanho != 'G':
            print('Tamanho inválido! Tente novamente.')
            pedidoTamanho = str(input('Tamanho desejado (P/M/G): ')).upper()
        if pedidoSabor == 'CP':
            if pedidoTamanho == 'P':
                valorTotal += 9
                print('Você pediu um Cupuaçu tamanho P: R$9,00')
            elif pedidoTamanho == 'M':
                valorTotal += 14
                print('Você pediu um Cupuaçu tamanho M: R$14,00')
            else:
                valorTotal += 18
                print('Você pediu um Cupuaçu tamanho G: R$18,00')
        elif pedidoSabor == 'AC':
            if pedidoTamanho == 'P':
                valorTotal += 11
                print('Você pediu um Açaí tamanho P: R$11,00')
            elif pedidoTamanho == 'M':
                valorTotal += 16
                print('Você pediu um Açaí tamanho M: R$16,00')
            else:
                valorTotal += 20
                print('Você pediu um Açaí tamanho G: R$20,00')
    except:
        print('Erro')
    finally:
        print('Pedido feito com sucesso!')
    pedidoOutro = input('Deseja fazer outro pedido? (S/N): ').upper()
print(f'Valor total a ser pago: R${valorTotal}')
