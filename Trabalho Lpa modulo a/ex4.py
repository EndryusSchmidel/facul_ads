import time

lista_livro = [] #exigencia 2, lista dos dicionarios
id_global = 0 #exigencia 2, contador 

def cadastrar_livro(id): #Exigencia 3, função de cadastrar livro
    print(f"\nCadastrando livro ID: {id}")
    cadastro_nome = str(input('Digite o nome do livro: '))
    cadastro_autor = str(input('Digite o nome do autor do livro: '))
    cadastro_editora = str(input('Digite o nome da editora do livro: '))
    livro = {
        "id": id,
        "Nome": cadastro_nome,
        "Autor": cadastro_autor,
        "Editora": cadastro_editora
    }
    lista_livro.append(livro)
    print('Livro cadastrado com sucesso! Voltando ao menu principal...')
    time.sleep(.5)
    
def consultar_livro(): #Exigencia 4, função de consultar livro
    while True:    
        try:
            print('\n====== MENU PARA CONSULTAR LIVROS ====== \n1 - Consultar todos\n2 - Consultar por id\n3 - Consultar por autor\n4 - Retornar ao menu principal')
            
            opc_consulta = int(input('Selecione uma opção: '))
            
            if opc_consulta == 1:
                print('Consultando todos os livros...')
                time.sleep(.5)
                for i, dicionario in enumerate(lista_livro, 1):
                    for c, v in dicionario.items():
                        print(f'\n{c}: {v}')
                    print('-' * 30)
                print('Todos os livros consultados! Voltando ao menu de consulta...')
                time.sleep(1)
            elif opc_consulta == 2:
                print('Consultando livros por ID!')
                time.sleep(.5)
                consulta_id = (input('Digite o ID do livro: '))
                encontrado = False
                for livro in lista_livro:
                    if str(livro['id']) == consulta_id:
                        print(f'Consultando livro de ID {consulta_id}...')
                        time.sleep(1)
                        print('\n')
                        print('-' * 30)
                        print(f"ID: {livro['id']}")
                        print(f"Nome: {livro['Nome']}")
                        print(f"Autor: {livro['Autor']}")
                        print(f"Editora: {livro['Editora']}")
                        print('-' * 30)
                        print('Voltando ao menu de consultas...')
                        time.sleep(.5)
                        encontrado = True
                        break
                if not encontrado:
                    print("Não contém livro com esse ID.")
                
            elif opc_consulta == 3:
                print('Consultando livros pelo autor!')
                time.sleep(.5)
                consulta_autor = input("Digite o nome do autor: ")
                print(f'Consultandos livros do autor: {consulta_autor.capitalize()}')
                time.sleep(.5)
                encontrado = False
                for livro in lista_livro:
                    if livro['Autor'].lower() == consulta_autor.lower():
                        print(f"\nID: {livro['id']}")
                        print(f"Nome: {livro['Nome']}")
                        print(f"Editora: {livro['Editora']}")
                        encontrado = True
                print('Voltando ao menu de consultas...')
                time.sleep(.5)
                if not encontrado:
                    print("❌ Nenhum livro encontrado para esse autor.")
                        
            elif opc_consulta == 4:
                print('Retornando ao menu principal...')
                time.sleep(.5)
                break
            
            else:
                print('Erro, você precisa digitar 1, 2, 3 ou 4!')
                
        except ValueError:
            print('Erro, você precisa digitar 1, 2, 3 ou 4!')

def remover_livro(): #Exigencia 5, função de remover livro
    print('Se desejar sair da opção de remoção de livro digite "Sair". ') # caso a pessoa selecione remover livro sem querer ou tenha esquecido de consultar o id do livro ela pode sair da function!
    
    while True:
        remover_id = (str(input('Digite o id do livro que você deseja remover: '))).capitalize()
        if remover_id == "Sair":
            return
        for livro in lista_livro:
            if str(livro['id']) == remover_id:
                lista_livro.remove(livro)
                print(f'\nO livro de ID {remover_id} foi removido!')
                return
        print(f'"{remover_id}" é um ID invalido.\n')
    
#Código Main
print("Bem vindo a Livraria do Endryus Schmidel") #Mensagem de boas vindas com meu nome, exigencia 1
while True:
    print("\n====== MENU PRINCIPAL ======\n")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")

    opcao = input("Escolha uma opção: ") #input menu main
    print('-' * 30)

    if opcao == "1": #Opção de cadastrar livro
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2": #Opção de consultar livro
        consultar_livro()
    elif opcao == "3": #Opção de remover livro
        remover_livro()
    elif opcao == "4": #Opção de encerrar programa
        print('Programa encerrado!')
        print('-' * 30)
        break
    else: #Caso não selecione nenhuma das 4 opções, retornar ao input de 'opcao'
        print('Opção inválida! Digite 1 2 3 ou 4!')