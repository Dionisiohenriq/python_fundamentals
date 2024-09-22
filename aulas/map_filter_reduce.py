from functools import partial, reduce
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55.55},
    {'nome': 'p3', 'preco': 5.59},
    {'nome': 'p4', 'preco': 22},
    {'nome': 'p5', 'preco': 81.23},
    {'nome': 'p6', 'preco': 5.7},
]

print_iter(produtos)

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

novos_produtos = list(map(muda_preco_de_produtos, produtos))

print_iter(produtos)
print_iter(novos_produtos)

print(isinstance(novos_produtos, GeneratorType))

print(list(map(lambda x: x * 2, [1, 2, 3, 4])))

novos_produtos = [
    p for p in produtos if p['preco'] > 0
]

def filtrar_preco(produto):
    return produto['preco'] > 10

novos_produtos = list(filter(filtrar_preco, produtos))

print_iter(novos_produtos)
#reduce

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

print(reduce(funcao_do_reduce, produtos, 0), 'Total')
total = 0
for p in produtos:
    total += p['preco']

print(total)

print(sum([p['preco'] for p in produtos]))
