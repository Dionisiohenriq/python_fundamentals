string = "Henrique"
nova_string = "*"
tamanho = len(string)
contador = 0


while contador < tamanho:
    print(f"{string[contador]}")
    nova_string += string[contador] + "*"
    contador += 1

print(f"{nova_string}")
