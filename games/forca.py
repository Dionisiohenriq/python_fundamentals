
import random
import sqlite3

def jogar_forca():

    imprime_abertura()
    # inicia o jogo da forca
    arquivo = digitar_palavras()
    palavra_secreta = gerar_palavra_secreta(arquivo)

    letras_certas = ["_" for letra in palavra_secreta]

    erros = 0
    pontos = 0
    opcao = True
    
    imprime_abertura()

    jogador = input("Qual o nome do jogador? ")

    # início dos palpites
    while opcao:
        
        chute = input("Qual a letra?").lower().strip()

        if chute in palavra_secreta:

            index = 0
            indices_encontrados=[]

            # faz a substituição dos caracteres na lista da palavra secreta
            for letra in palavra_secreta:

                if chute == letra:
                    letras_certas.__setitem__(index, chute)
                    indices_encontrados.append(index)

                index += 1

            # exibe a situação atual da forca após um acerto
            print(f"Letra {chute} encontrada no(s) índice(s): {indices_encontrados}")
            print(letras_certas)

        # desenha a forca em caso de erro
        elif chute not in palavra_secreta:
            erros += 1
            desenha_forca(erros)
        
        if "_" not in letras_certas:
            print(f"Você ganhou!! :D\nQtd de erros: {erros}")
            imprime_mensagem_vencedor()
            pontos += 1
            opcao = input("Jogar novamente? Digite qualquer tecla ou enter para sair ")
            palavra_secreta = gerar_palavra_secreta(arquivo)
            letras_certas = ["_" for letra in palavra_secreta]
            salvar_dados(jogador, pontos, criar_banco())

        elif erros is 7:
            imprime_mensagem_perdedor(palavra_secreta)
            pontos -= 1
            opcao = input("Jogar novamente? Digite qualquer tecla ou enter para sair ")
            palavra_secreta = gerar_palavra_secreta(arquivo)
            letras_certas = ["_" for letra in palavra_secreta]
            salvar_dados(jogador, pontos, criar_banco())       
    print("Fim de jogo!")


def imprime_abertura():

    print("* " * 10)
    print("Bem vindo ao jogo da forca!")
    print("* " * 10)


def digitar_palavras():
    
    ### insere uma qtd de palavras determinada no arquivo para o jogo da forca ###

    with open("palavras.txt", "w") as arquivo:
        
        qtd_palavras = int(input("Digite a qtd de palavras para a forca: "))
        for i in range(0, qtd_palavras):
            arquivo.write(input("Digite uma palavra: "))
            arquivo.write("\n")

    return arquivo


def gerar_palavra_secreta(arquivo: str) -> str:
    
    ### recebe um arquivo com palavras e retorna uma palavra selecionada aleatoriamente do arquivo ###
    
    palavra_secreta = ""
    with open("palavras.txt", "r") as arquivo:

        palavras = [ linha for linha in arquivo ]
        palavra_secreta = palavras.__getitem__(random.randint(0, len(palavras)-1)).strip().lower()

    return palavra_secreta


def desenha_forca(erros):
    

    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print() #desenho da forca.


def imprime_mensagem_vencedor():

    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ") #desenho do troféu


def imprime_mensagem_perdedor(palavra_secreta):

    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")  #desenho da caveira


def salvar_dados(jogador, pontos, conexao: sqlite3.Connection) -> sqlite3.Connection:
    
    with conexao as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO forca_pontos(jogador, pontos)" +
                     "VALUES(?, ?)", [jogador, pontos])
        cursor.execute("UPDATE forca_pontos SET pontos = ? WHERE jogador = ?" , [+pontos, jogador])
        
        return cursor.fetchone()


def criar_banco():

    with sqlite3.connect("forca.db") as conn:
        
        cursor = conn.cursor()

        result = cursor.execute("CREATE TABLE IF NOT EXISTS forca_pontos( " +
                              "id INTEGER PRIMARY KEY AUTOINCREMENT, jogador TEXT, pontos INT)")

        return conn


if __name__ == "__main__":
    jogar_forca()

