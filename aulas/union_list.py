from itertools import zip_longest


def ziper(list1, list2):
    max_interval = min(len(l1), len(l2))
    return [
        (list1[i], list2[i]) for i in range(max_interval)
    ]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(ziper(l1, l2))
print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='Sem cidade')))
