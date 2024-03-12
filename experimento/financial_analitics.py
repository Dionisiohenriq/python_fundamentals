import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Gerando dados de vendas hipotéticos
anos = pd.date_range(start='2020-01-01', end='2023-12-31', freq='M')
vendas = np.random.randint(10000, 50000, size=len(anos))
despesas = np.random.randint(5000, 20000, size=len(anos))

# Criando um DataFrame com os dados
dados = pd.DataFrame({'Ano': anos, 'Vendas': vendas, 'Despesas': despesas})

# Calculando o lucro
dados['Lucro'] = dados['Vendas'] - dados['Despesas']

# Análise descritiva dos dados
print(dados.describe())

# Visualizando as vendas ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(dados['Ano'], dados['Vendas'], marker='o', color='b', label='Vendas')
plt.title('Vendas ao longo do tempo')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.legend()
plt.grid(True)
plt.show()

# Visualizando a distribuição do lucro
plt.figure(figsize=(8, 5))
plt.hist(dados['Lucro'], bins=10, color='g', alpha=0.7)
plt.title('Distribuição do Lucro')
plt.xlabel('Lucro')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Calculando a média móvel das vendas
dados['Media_Movel_Vendas'] = dados['Vendas'].rolling(window=12).mean()

# Visualizando a média móvel das vendas ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(dados['Ano'], dados['Vendas'], marker='o', color='b', label='Vendas')
plt.plot(dados['Ano'], dados['Media_Movel_Vendas'], linestyle='--', color='r', label='Média Móvel (12 meses)')
plt.title('Vendas e Média Móvel ao longo do tempo')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.legend()
plt.grid(True)
plt.show()
