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

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")

horario = int(input("Insira uma hora em números inteiros"))
try:
    horario = int(horario)
    if horario >= 0 and horario <= 11:
        print("Bom dia!")
    elif horario >= 12 and horario <= 17:
        print("Boa tarde!")
    elif horario >= 18 and horario <= 23:
        print("Boa noite!")
    else:
        print("Horário não reconhecido!")

except ValueError:
    print(f"Você não digitou um inteiro!")


nome = input("Insira seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) in range(5, 7):
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande!")
