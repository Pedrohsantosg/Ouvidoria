import Ouvidoria as ouv
import testebd as bd
import os
import time


tipo = ''
conexao = bd.abrir_banco_de_dados('localhost', 'root', 'root', 'ouvidoria')
option = '0'
n = ouv.Ouvidoria()

print('Bem vindo a ouvidoria, em que podemos lhe ajudar ?')
while True:
    n.pagina_principal()
    option = input('\nDigite sua opção: ')
    os.system('clear')

    if option == '1':
        nome = input('Digite o seu nome: ').strip().title()
        while tipo != 'Sugestão' and tipo != 'Reclamação' and tipo != 'Elogio':
            tipo = input('Digite o tipo da manifestação (Sugestão, Reclamação ou Elogio): ').strip().title()
        descricao = input('Digite a descrição da manifestação: ').strip().capitalize()
        n.cadastrar_ocorrencia(conexao, nome, tipo, descricao)
    elif option == '2':
        list_ocorrencia = int(input('Deseja ver seu histórico de ocorrência ?:\n1:SIM\n2:NÃO \n---> : '))
        if list_ocorrencia == 1:
            n.listar_ocorrencias(conexao)
        volta_menu = int(input('Deseja voltar para o menu ?:\n1:SIM\n---> : '))
        os.system('clear')
    elif option == '3':
        remover = int(input('Deseja apagar: \n1)Todas as ocorrências \n2)Ocorrência especifíca \n---> : '))
        if remover ==1:
            n.apagar_todas(conexao)
        else:
            n.listar_ocorrencias(conexao)
            id = int(input('Digite o ID que você deseja remover: \n'))
            n.apagar_especifica(conexao, id)
        os.system('clear')
    elif option == '4':
        n.encerrando_ouvidoria(conexao)
        break
    elif option >= '5':
        print('ERROR')
        time.sleep(2)
    os.system('clear')
