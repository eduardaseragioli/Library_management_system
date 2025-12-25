import mysql.connector 
from mysql.connector import Error

class DatabaseManager:# Classe para gerenciar a conexão com o banco de dados MySQL
    def __init__(self, host="localhost", user="root", password="", database="biblioteca"):
        self.host = host 
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self): 
        """Estabelece a conexão com o banco de dados."""
        try:
            # Tenta executar o bloco de código a seguir, que pode gerar um erro se a conexão falhar.
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexão bem-sucedida ao banco de dados!")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def execute_query(self, query, params=None):
        # Define o método 'execute_query', usado para executar comandos SQL que modificam o banco de dados.

        """
        Executa uma consulta SQL (INSERT, UPDATE, DELETE).
        :param query: A string da consulta SQL.
        :param params: Parâmetros opcionais para a consulta.
        """
        if self.connection is None or not self.connection.is_connected():
            print("Conexão não estabelecida. Chame o método connect() primeiro.")
            return

        cursor = self.connection.cursor()# Cria um objeto 'cursor',q permite interagir com o banco de dados,

        try:
            if params is not None:# Se 'params' não for None, executa a consulta com os parâmetros fornecidos.
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()# Confirma as alterações no banco de dados.
            print("Consulta executada com sucesso!")
        except Error as e:
            print(f"Erro ao executar a consulta: {e}")
        finally:
            cursor.close()

    def fetch_query(self, query, params=None): # Define o método 'fetch_query', usado para executar consultas SQL que retornam dados, como SELECT.
        """
        Executa uma consulta SQL (SELECT) e retorna os resultados.
        :param query: A string da consulta SQL.
        :param params: Parâmetros opcionais para a consulta.
        :return: Lista de resultados da consulta.
        """
        if self.connection is None or not self.connection.is_connected():
            print("Conexão não estabelecida. Chame o método connect() primeiro.")
            return

        cursor = self.connection.cursor(dictionary=True)# O parâmetro 'dictionary=True' permite que os resultados sejam retornados como dicionários, facilitando o acesso aos dados por nome de coluna.
        try:
            if params is not None:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()#Pega todos os resultados da consulta e os armazena na variável 'results'.
            return results
        except Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
        finally:
            cursor.close()

    def close_connection(self):# Define o método 'close_connection', usado para fechar a conexão com o banco de dados.
        """Fecha a conexão com o banco de dados."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")

# Exemplo de uso
if __name__ == "__main__":# Verifica se o script está sendo executado diretamente
    db_manager = DatabaseManager()# Cria uma instância da classe DatabaseManager com os parâmetros padrão.
    db_manager.connect()

    # Exemplo de consulta SELECT
    results = db_manager.fetch_query("SELECT * FROM livros")  # Substitua "livros" pelo nome da sua tabela
    # Executa uma consulta SELECT para buscar todos os registros da tabela 'livros'.

    if results:
        for row in results:# Itera sobre os resultados retornados pela consulta e imprime cada linha.
            print(row)

    # Fechar a conexão
    db_manager.close_connection()