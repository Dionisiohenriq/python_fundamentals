product = {
    'name' : 'Blue Pen',
    'price' : 2.5,
    'category' : 'Office',
}

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
    if key != 'category'
}

list = [
    ('a', 'value a'),
    ('b', 'value b'),
    ('c', 'value c'),
]

dc = {
    key: value
    for key, value in list
}

new_dict = dict(list)

print(dc)
print(new_dict)