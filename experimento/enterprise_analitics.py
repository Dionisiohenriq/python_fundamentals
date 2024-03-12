import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando um conjunto de dados fictício de vendas mensais
np.random.seed(0)
meses = pd.date_range(start='2023-01-01', end='2023-12-01', freq='M')
vendas = np.random.randint(10000, 50000, size=len(meses))
produtos = ['Produto A', 'Produto B', 'Produto C']
produto_vendido = np.random.choice(produtos, size=len(meses))

dados_vendas = pd.DataFrame({'Data': meses, 'Vendas': vendas, 'Produto': produto_vendido})

# Visualizando as primeiras linhas do conjunto de dados
print("Conjunto de dados de vendas:")
print(dados_vendas.head())

# Resumo estatístico das vendas
print("\nResumo estatístico das vendas:")
print(dados_vendas['Vendas'].describe())

# Vendas totais por produto
vendas_por_produto = dados_vendas.groupby('Produto')['Vendas'].sum()
print("\nVendas totais por produto:")
print(vendas_por_produto)

# Visualização das vendas ao longo do tempo
dados_vendas.set_index('Data', inplace=True)
dados_vendas.groupby('Produto')['Vendas'].plot(legend=True)
plt.ylabel('Vendas')
plt.title('Vendas mensais por produto')
plt.show()
