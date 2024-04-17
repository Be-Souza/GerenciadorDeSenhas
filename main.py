import sqlite3

def verificarCredenciais(usuario, senha):
    
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('userSenhaProd.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Buscar no banco de dados, tal usuário

    cursor.execute('SELECT senha FROM usuarios WHERE user=?', (userGerenciador,))
    deuCerto = cursor.fetchone()

    #Verifica se a senha que veio é igual a senha que foi

    if deuCerto:                     # Esse if, que parece meio sem pé nem cabeça, na verdade, está verificando se       
                                     # o banco de dados retornou de fato alguma coisa, se for "true", retornou normal
        senhaDoBanco = deuCerto[0]   # se for "false", significa que ele recebeu "none" do banco de dados, e não vai rodar
                                     # o código dentro do if       
                                                                  # E o senhaDoBanco = deuCerto[0] é pra atribuir à 
                                                                  #senhaDoBanco, o valor do primeiro item (ID 0)
        
        #Comparar de fato se tá certo

        if senhaDoBanco == senha:
            print("Acesso concedido!")
            return True
        else:
            print("Acesso negado.")
    else:
        print("Usuário não encontrado.")

    #Fecha conexão com banco de dados
    conn.close()    
    return False

#Login

usuarioEntrou = False

while not usuarioEntrou:
    
    userGerenciador = input("Usuário: ")
    senhaGerenciador = input("Senha: ")
    usuarioEntrou = verificarCredenciais(userGerenciador, senhaGerenciador)

    if usuarioEntrou:
        print("Inicializando...")
    else:
        print("Por favor, tente novamente!")

print("Seja bem vindo ao seu mais novo gerenciador de senhas")
