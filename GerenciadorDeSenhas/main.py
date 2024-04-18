import sqlite3
import os
import time

def criarUsuario():
    
    limparTerminal()
    print("Bem vindo ao menu de criação de usuário!\n")

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
    senha = input("Insira a senha do usuário:")

    # Declaração de um metodo

    guardarInfo = 'INSERT INTO usuarios (user, senha) VALUES (?, ?)'

    # Inserir dados na tabela
    cursor.execute(guardarInfo,(user, senha))


    # Salvar as mudanças
    conn.commit()

    # Consultar dados
    cursor.execute('SELECT user, senha FROM usuarios WHERE user = ?', (user,))
    print("Usuário e senha cirados com sucesso!", cursor.fetchall())

    # Fechar a conexão
    conn.close()

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():

    limparTerminal()
    usuarioEntrou = False

    while not usuarioEntrou:
        
        userGerenciador = input("Usuário: ")
        senhaGerenciador = input("Senha: ")
        usuarioEntrou = verificarCredenciais(userGerenciador, senhaGerenciador)

        if usuarioEntrou:
            print("Inicializando...")
        else:
            print("Por favor, tente novamente!")
    print("Seja bem vindo ao PassWorld!")
    time.sleep(1)
    limparTerminal()

    print(f"Bem vindo {userGerenciador}!")

def verificarCredenciais(usuario, senha):
    
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('userSenhaProd.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Buscar no banco de dados, tal usuário

    cursor.execute('SELECT senha FROM usuarios WHERE user=?', (usuario,))
    deuCerto = cursor.fetchone()

    #Verifica se a senha que veio é igual a senha que foi

    if deuCerto:                     # Esse if, que parece meio sem pé nem cabeça, na verdade, está verificando se       
                                     # o banco de dados retornou de fato alguma coisa. se for "true", retornou normal
        senhaDoBanco = deuCerto[0]   # se for "false", significa que ele recebeu "none" do banco de dados, e não vai rodar
                                     # o código dentro do if       
                                                                  # E o senhaDoBanco = deuCerto[0] é pra atribuir à 
                                                                  #senhaDoBanco, o valor do primeiro item (ID 0)
        
        #Comparar de fato se tá certo

        if senhaDoBanco == senha:
            limparTerminal()
            print("Acesso concedido!")
            return True
        else:
            limparTerminal()
            print("Acesso negado.")
    else:
        limparTerminal()
        print("Usuário não encontrado.")

    #Fecha conexão com banco de dados
    conn.close()    
    return False

def printaTela():
    print("O que você deseja fazer?")
    print("\n")
    print("1. Listar senhas")
    print("2. Inserir nova senha")
    print("3. Excluir uma senha")
    print("4. Gerador de senhas")
    print("5. Sair")

####COMEÇO OFICIAL DO PROGRAMA-------------------------------------------------------------------------------------

logou = False

while not logou:

    print("Bem vindo ao PassWorld!\n")
    print("O que você deseja fazer?\n")
    print("------------------------\n")
    print("1. Entrar no PassWorld")
    print("2. Criar uma conta PassWorld")

    escolhaTelaInicial = input("\nDigite o número referente a opção desejada: ")

    if escolhaTelaInicial == '1':
        login()
        logou = True
    elif escolhaTelaInicial == '2':
        criarUsuario()
        logou = True
    else:
        limparTerminal()
        print("Opção inválida digitada, tente novamente.")


usandoPrograma = True

####DEFINIÇÃO DE ESCOLHAS (cada um é uma função dentro do programa) -----------------------------------------

def insereSenha():
    limparTerminal()
    conn = sqlite3.connect('passworld.db')
    cursor = conn.cursor()
    armazenaSite = input("Digite o SITE ou SERVIÇO para qual você deseja cadastrar uma senha: ")
    armazenaUser = input(f"Digite o USUÁRIO que será usado no site/serviço {armazenaSite}: ")
    armazenaSenha = input(f"Digite a SENHA que será usada no site/serviço")




####DEFINIÇÃO DE ESCOLHAS (cada um é uma função dentro do programa) -----------------------------------------

while usandoPrograma:
    printaTela()
    escolhaTela = input("\nDigite o número referente a opção desejada: ")
    if escolhaTela == '1':
        print("jonasguedes")
    if escolhaTela == '2':
        insereSenha()
    usandoPrograma = False