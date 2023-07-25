def multiplicador(multiplicador):
    def numero(numero):
        return multiplicador * numero

    return numero


num = int(input("Insira um número:"))
multiplicar = int(input("Insira um multiplicador:"))


duplicar = multiplicador(multiplicar)
print(duplicar(num))
teste   