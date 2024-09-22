import json


pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Otávio',
    'endereços': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.80,
    'numero': 29,
    'dev': True,
    'nada': None,
}

with open('./module.json', 'w', encoding='utf-8') as file:
    json.dump(pessoa, file, ensure_ascii=False, indent=4)

with open('./module.json', 'r', encoding='utf-8') as file:
    pessoa = json.load(file)
    print(pessoa['nome'])
    print(type(pessoa))
