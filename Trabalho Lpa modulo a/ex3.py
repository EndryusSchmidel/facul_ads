print('Boas vindas a copiadora do Endryus Schmidel') #EXIGÊNCIA DE CÓDIGO 1 de 7;

def escolha_servico(): #EXIGÊNCIA DE CÓDIGO 2 de 7
    print('Nossos serviços \nDIG - Digitalização \nICO - Impressão colorida\nIPB - Impressão preto e branco\nFOT - Fotocópia') #Tabela de serviços
    while True:
        servicoEscolhido = str(input('Escolha o serviço desejado: ')).upper()
        if servicoEscolhido == 'DIG':
            return 1.10
        elif servicoEscolhido == 'ICO':
            return 1
        elif servicoEscolhido == 'IPB':
            return 0.40
        elif servicoEscolhido == 'FOT':
            return 0.20
        else:
            print('Escolha inválida, escolha um tipo de serviço novamente!')
def num_paginas(): #EXIGÊNCIA DE CÓDIGO 3 de 7
    while True:
        try:    
            paginas = int(input('Digite a quantidade de páginas que você deseja fazer a impressão: '))
            if paginas >= 20000:
                print('Quantidade de páginas não permitida, deve ser menor que 20.000!') #Limite de páginas
                continue
            elif paginas < 20:
                return paginas
            elif 20 <= paginas < 200:
                return paginas * 0.85
            elif 200 <= paginas < 2000:
                return paginas * 0.80
            elif 2000 <= paginas < 20000:
                return paginas * 0.75
        except ValueError:
            print("Por favor, digite um número válido de páginas.")
def servico_extra(): #EXIGÊNCIA DE CÓDIGO 4 de 7
    print('----- Serviços Extras -----\n( 1 ) Encadernação simples - R$15.00\n( 2 ) Encadernação de capa dura - R$40.00 \nDigite 0 se não quiser adicional!') #Tabela de serviços extras
    while True:
        adicional = input('Deseja algum serviço extra? ')
        if adicional == "1":
            return 15.00
        elif adicional == "2":
            return 40.00
        elif adicional == "0":
            return 0.00
        else:
            print('Opção inválida! Digite 0, 1 ou 2')
            
try: #EXIGÊNCIA DE CÓDIGO 6 de 7
    servico = escolha_servico()
    paginas = num_paginas()
    extra = servico_extra()
    total = (servico * paginas) + extra #Soma do valor total incluindo descontos e extras
    print(f'Valor total a ser pago: R${total:.2f} (Serviço: {servico} * Páginas: {paginas:.2f} + extra: {extra:.2f})') #EXIGÊNCIA DE CÓDIGO 5 de 7
except Exception as x: #Tratamento de erro genérico 
    print('Ocorreu um erro inesperado: ',x)