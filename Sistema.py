import mysql.connector
from mysql.connector import Error

class Gestao:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.conn = None
        self.verificar_ou_criar_banco_de_dados()
        self.conectar_ao_banco()
        self.criar_tabela_estoque()

    def verificar_ou_criar_banco_de_dados(self):
        try:
            # Conecta sem especificar o banco de dados para verificar sua existência
            conn = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha
            )
            cursor = conn.cursor()
            cursor.execute(f"SHOW DATABASES LIKE '{self.banco}'")
            resultado = cursor.fetchone()
            if not resultado:
                cursor.execute(f"CREATE DATABASE {self.banco}")
                print(f"Banco de dados '{self.banco}' criado com sucesso.")
            else:
                print(f"Banco de dados '{self.banco}' já existe.")
            cursor.close()
            conn.close()
        except Error as e:
            print(f"Erro ao verificar ou criar o banco de dados: {e}")

    def conectar_ao_banco(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )
            if self.conn.is_connected():
                print(f"Conectado ao banco de dados '{self.banco}' com sucesso.")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabela_estoque(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estoque (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    produto VARCHAR(255),
                    quantidade INT
                )
            ''')
            self.conn.commit()
            cursor.close()
            print("Tabela 'estoque' verificada/criada com sucesso.")
        except Error as e:
            print(f"Erro ao criar a tabela 'estoque': {e}")

    # Demais métodos (adicionar_produto, remover_produto, etc.) permanecem os mesmos

# Exemplo de uso
sistema = Gestao(host="localhost", usuario="root", senha="1234", banco="estoqueatd")
