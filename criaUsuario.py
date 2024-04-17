import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('databaseTeste.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

# Pergunta ao usuário, que usuário ele quer criar

userCria = input("Insira o nome de usuário à ser criado:")
senhaCria = input("Insira a senha numérica do usuário:")

# Declaração de um metodo

guardarInfo = 'INSERT INTO usuarios (nome, senha) VALUES (?, ?)'

# Inserir dados na tabela
cursor.execute(guardarInfo,(userCria, senhaCria))


# Salvar as mudanças
conn.commit()

# Consultar dados
cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())

# Fechar a conexão
conn.close()