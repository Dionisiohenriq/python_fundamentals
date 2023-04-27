import random

def jogar_adivinhacao():
    
    print("*" * 10)
    print("Bem vindo ao jogo de Adivinhação")
    print("*" * 10)

    total_tentativas = 0
    pontos = 1000
    random.seed()
    numero_secreto = random.randint(0, 100)

    # seleção do nível de dificuldade: 
    print("Qual nível de dificuldade? ")

    print ("Nível 1 (Fácil)\nNível 2 (Médio)\nNível 3 (Difícil)")
    nivel = input("Insira o nível desejado")

    if(nivel is 1):
        total_tentativas = 20

    elif(nivel is 2):
        total_tentativas = 10

    else:
        total_tentativas = 5


    # início das tentativas
    for i in range(1, total_tentativas):
        
        print(f"Rodada atual {i} de {total_tentativas}.")
        chute_str = input("Digite o número secreto!")
        
        print(f"Você digitou: {chute_str}")

        chute = int(chute_str)

        if(chute < 1):
            print(f"Digite um número entre 1 e 100, número digitado: {chute}")
            
        # validação do chute
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f"Parabéns! Você acertou o número secreto: {numero_secreto}\nPontos: {pontos}")
            break
        else:
            if(maior):
                print(f"O seu chute foi maior do que o número secreto! {numero_secreto}")
            elif(menor):
                print(f"O seu chute foi menos do que o número secreto! {numero_secreto}")
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - abs(pontos_perdidos)
            print(f"Pontos atuais: {pontos}")
            

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar_adivinhacao()