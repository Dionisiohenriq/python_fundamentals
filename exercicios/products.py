import copy
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'name': 'Product5', 'price': 10.00},
    {'name': 'Product4', 'price': 22.32},
    {'name': 'Product3', 'price': 10.11},
    {'name': 'Product2', 'price': 105.87},
    {'name': 'Product1', 'price': 69.90},
]
# Ordene os produtos por nome decrescente ( do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# new_products = [{'price': round(product['price'] + (product['price'] * 0.1), 2)} for product in produtos]
#new_products = copy.deepcopy([{'name': product['name'], 'price': float(f"{product['price'] + (product['price'] * 0.1):.2f}")} for product in produtos])
new_products = [ {**p, 'price': f'{p['price'] * 1.1:.2f}'}
                 for p in copy.deepcopy(produtos)
                ]



print(*produtos, sep='\n')
print()

ordered_products_by_name = sorted(
        copy.deepcopy(produtos),
        key=lambda k: k['name'], reverse=True
)

ordered_products_by_price = sorted(
    copy.deepcopy(produtos),
    key=lambda k: k['price'], reverse=False
)

print(*new_products, sep='\n')

print()

print(*ordered_products_by_name, sep='\n')

print()

print(*ordered_products_by_price, sep='\n')

