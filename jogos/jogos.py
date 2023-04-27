from jogos import forca
from jogos import adivinhacao

print("* " * 10)
print("Escolha seu jogo!")
print("* " * 10)

print("1 Forca - 2 Adivinhação")
jogo = int(input("Qual o jogo?"))

if(jogo is 1):
    print("Jogar forca!")
    forca.jogar_forca()
    
elif(jogo is 2):
    print("Jogar adivinhação")
    adivinhacao.jogar_adivinhacao()