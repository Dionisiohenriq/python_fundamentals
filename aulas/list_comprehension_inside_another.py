list = []
for x in range(3):
    for y in range(3):
        list.append((x, y))

list = [(x, y)
        for x in range(3)
        for y in range(3)
        ]


list = [
        [(x, letra for letra in 'Henrique')]
        for x in range(3)
        for y in range(3)
        ]


print(list)