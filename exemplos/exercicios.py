nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
if not nome or not idade:
    print("Você deixou campos vazios")
else:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome {'contém' if ' ' in nome else 'não contém'} espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")

numero = input("Informe um número: ")

n = int(numero)

if type(n) is not int:
    print("O número digitado não é um inteiro")
elif n % 2 != 0:
    print("Número ímpar")
else:
    print("Número par")

horario = input("Qual a hora atual? ")

h = int(horario)

if h in range(0, 11 + 1):
    print("Bom dia!")
elif h in range(12, 17 + 1):
    print("Boa tarde!")
else:
    print("Boa noite!")


nome = input("Insira seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) in range(5, 7):
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande!")
