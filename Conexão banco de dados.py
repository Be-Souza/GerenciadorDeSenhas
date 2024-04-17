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
    idade INTEGER
)
''')

# Inserir dados na tabela
cursor.execute('''
INSERT INTO usuarios (nome, idade) VALUES (?, ?)
''', ('Bernardo', 17))

# Salvar as mudanças
conn.commit()

# Consultar dados
cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())

# Fechar a conexão
conn.close()