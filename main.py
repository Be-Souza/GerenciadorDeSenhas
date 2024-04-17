import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('userPassword.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()



userGerenciador = input("Usuário: ")
senhaGerenciador = input("Senha: ")

print("Você digitou o usuário",userGerenciador,"e a senha",senhaGerenciador,)

