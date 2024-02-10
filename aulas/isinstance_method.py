list = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'name': 'Luiz'}
]

for item in list:
    if isinstance(item, set):
        item.add(5)
        print('Set')
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('Str')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('Num')
        print(item * 2)

    else:
        print('Unknown')
        print(item, type(item))