import mysql.connector


def abrir_banco_de_dados(host, user, password, database):
    return mysql.connector.connect(
        host=host, user=user, password=password, database=database)


def encerrar_banco_de_dados(connection):
    return connection.close()


def inserir_no_banco_de_dados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()


def excluir_banco_de_dados(connection, sql, id):
    cursor = connection.cursor()
    dados = (id,)
    cursor.execute(sql, dados)
    connection.commit()


def excluir_banco_total(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


def listar_banco_de_dados(connection, sql_listar):
    cursor = connection.cursor()
    cursor.execute(sql_listar)
    listaOuvidoria=cursor.fetchall()
    for ouvidoria in listaOuvidoria:
        print(ouvidoria[0], ouvidoria[1], ouvidoria[2], ouvidoria[3])
