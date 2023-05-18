OPERADORES = "+-*/"

while True:
    numero_1 = input("Insira o primeiro número: ")
    operador = input(f"Insira o operador{OPERADORES}: ")
    numero_2 = input("Insira o segundo número: ")

    numeros_validos = None
    resultado = ...

    try:
        numero1 = float(numero_1)
        numero2 = float(numero_2)

        if len(operador) > 1:
            print("Digite apenas 1 operador")
            continue

        if operador not in OPERADORES:
            print("Operador inválido")
            continue

        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*":
            resultado = numero1 * numero2
        elif operador == "/":
            resultado = numero1 / numero2

        print(f"Resultado da operação: {resultado}")

    except:
        print("Um ou mais números inválidos.")
        numeros_validos = None

    sair = input("Quer sair? [s]im").lower().startswith("s")

    if sair:
        break
