def jogar_forca():

    print("* " * 10)
    print("Bem vindo ao jogo da forca!")
    print("* " * 10)

    palavra_secreta = "banana".lower()
    letras_certas = ["_", "_", "_", "_", "_", "_"]
    erros = 0
    acertou = False
    enforcou = False

    # início dos palpites
    while not enforcou and not acertou:
        
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
        
        # verificação de enforcamento
        enforcou = erros is 6

        # verificação de acerto da palavra
        acertou = "_" not in letras_certas


    if acertou:
        print("Você ganhou!! :D ")
    else:
        print("Você perdeu! :'(")

    print("Fim do jogo!")
    

if __name__ == "__main__":
    jogar_forca()