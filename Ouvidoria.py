import testebd as bd
import os
import time

conexao = bd.abrir_banco_de_dados('localhost', 'root', 'root', 'ouvidoria')

class Ouvidoria:

    def cadastrar_ocorrencia(self, conexao, nome, tipo, descricao):
        aux = 1

        while aux != 2:
            # cadastrando no banco...
            sql = "INSERT INTO ouvidoria(nome, tipo, descricao) VALUES (%s, %s, %s)"
            dados = (nome, tipo, descricao)
            bd.inserir_no_banco_de_dados(conexao, sql, dados)
            print('Registrada com sucesso!\n')
            time.sleep(2)
            os.system('clear')
            break

    def pagina_principal(self):
        print('-' * 30)
        print(
            'Ouvidoria:\n1) Cadastrar Ocorrências'
            '\n2) Listar Ocorrências '
            '\n3) Apagar Ocorrências '
            '\n4) Sair'
        )
        print('-' * 30)

    def listar_ocorrencias(self, conexao):
        # Capturando Ocorrências no Banco...
        sql_listar = "SELECT * FROM ouvidoria"
        bd.listar_banco_de_dados(conexao, sql_listar)
        
    def apagar_todas(self, conexao):
        sql = "DELETE FROM ouvidoria"
        bd.excluir_banco_total(conexao, sql)
        print('-removido com sucesso-')
        time.sleep(3)

    def apagar_especifica(self, conexao, id):
        sql_listar = "SELECT * FROM ouvidoria"
        sql = "DELETE FROM ouvidoria WHERE idOuvidoria = %s"
        bd.listar_banco_de_dados(conexao, sql_listar)
        bd.excluir_banco_de_dados(conexao, sql, id)
        print('-removido com sucesso-')
        time.sleep(3)
        
    def encerrando_ouvidoria(self, conexao):
        bd.encerrar_banco_de_dados(conexao)
        print('-' * 30)
        print('Saindo do programa.....')
        print('-' * 30)
        time.sleep(2)
        os.system('clear')
        print('-' * 30)
        print('Obrigado pela preferência ')
        print('-' * 30)