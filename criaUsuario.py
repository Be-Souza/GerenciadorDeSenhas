import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('userSenhaProd.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')

# Pergunta ao usuário, que usuário ele quer criar

user = input("Insira o nome de usuário à ser criado:")
senha = input("Insira a senha do usuário (Texto):")

# Declaração de um metodo

guardarInfo = 'INSERT INTO usuarios (user, senha) VALUES (?, ?)'

# Inserir dados na tabela
cursor.execute(guardarInfo,(user, senha))


# Salvar as mudanças
conn.commit()

# Consultar dados
cursor.execute('SELECT * FROM usuarios')
print("Usuário e senha cirados com sucesso!", cursor.fetchall())

# Fechar a conexão
conn.close()
