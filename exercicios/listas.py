OPCOES = 'ial'

while True:
    print("Selecione uma opção")
    
    opcao = input('[i]nserir, [a]pagar, [l]istar')

    if opcao.lower() not in OPCOES:
        print("Insira uma opção válida!")


    