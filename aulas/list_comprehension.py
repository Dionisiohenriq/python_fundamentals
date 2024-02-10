from pprint import pprint

def p(v):
    pprint(v, sort_dicts=False, width=40)

list = []
for number in range(10):
    list.append(number)

list = [number * 2 for number in range(10)]

# print(list)

products = [
    {'name': 'p1', 'price': 20,},
    {'name': 'p2', 'price': 10,},
    {'name': 'p3', 'price': 30,},
]

new_products = [
    {**product, 'price': product['price'] * 1.05} 
    if product['price'] > 20 else {**product} 
    for product in products
    if product['price'] >= 20 and product['price'] * 1.05 > 10
    ]
# print(*new_products, sep='\n')
# p(new_products)

# list = [n for n in range(10) if n < 5]
# print(list)
p(new_products)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list = [number if number != 6 else 600 for number in numbers]

print(list)
