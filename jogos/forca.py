import random


def jogar_forca():
    # inicia o jogo da forca
    arquivo = digitar_palavras()
    palavra_secreta = gerar_palavra_secreta(arquivo)

    letras_certas = ["_" for letra in palavra_secreta]
    erros = 0
    pontos = 0
    opcao = True

    print("* " * 10)
    print("Bem vindo ao jogo da forca!")
    print("* " * 10)

    # início dos palpites
    while opcao:
        chute = input("Qual a letra?").lower().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    print(f"Letra {chute} encontrada no índice: {index}")
                    letras_certas.__setitem__(index, chute)
                    print(letras_certas)

                index += 1
        else:
            erros += 1

    if "_" not in letras_certas:
        print(f"Você ganhou!! :D\nQtd de erros: {erros}")
        pontos += 1

    else:
        print("Você cometeu 6 erros!\nPerdeu! :'(")
        pontos -= 1

    opcao = input("Jogar novamente? Digite qualquer tecla ou enter para sair ")


print("Fim do jogo!")


def digitar_palavras():
    # insere uma qtd de palavras determinada no arquivo para o jogo da forca

    with open("palavras.txt", "w") as arquivo:
        qtd_palavras = int(input("Digite a qtd de palavras para a forca: "))
        for i in range(0, qtd_palavras):
            arquivo.write(input("Digite uma palavra"))
            arquivo.write("\n")

    return arquivo


def gerar_palavra_secreta(arquivo: str) -> str:
    # recebe um arquivo com palavras e retorna uma palavra selecionada aleatoriamente do arquivo

    palavra_secreta = ""
    with open("palavras.txt", "r") as arquivo:
        palavras = [linha for linha in arquivo]
        palavra_secreta = (
            palavras.__getitem__(random.randint(0, len(palavras) - 1)).strip().lower()
        )

    return palavra_secreta


if __name__ == "__main__":
    jogar_forca()
