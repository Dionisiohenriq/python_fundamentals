
import os
caminho_arquivo = 'C:/Users/menuu/Desktop/New folder (2)/aula116.txt'

with open(caminho_arquivo, 'a+', encoding='utf-8') as file:
    file.write('Alguma coisa, atenção\n')
    file.write('Alguma outra coisa\n')
    file.writelines(
        [
            'Alguma coisa\n',
            'Alguma outra coisa\n'
        ]
    )
    file.seek(0, 0)
    print(file.read())
    print('Lendo')
    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline().strip())
    print(file.readline())
    print(file.readline())
    print('READLINES')
    for linha in file.readlines():
        print(linha.strip())
    

with open(caminho_arquivo, 'r') as file:
    print(file.read())


os.unlink(caminho_arquivo)
os.remove(caminho_arquivo)
os.rename(caminho_arquivo, 'aula116.txt')


pessoa = {
    
}