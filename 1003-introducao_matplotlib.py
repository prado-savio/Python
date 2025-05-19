# 10.03

from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Visualização de Dados - Uso de Matplotlib - 10.03")
print(f"Biblioteca: pandas.DataFrame.plot")
print(f"		https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas")
print(f"	     Choosing Colormaps in Matplotlib")
print(f"		https://matplotlib.org/stable/users/explain/colors/colormaps.html")
print(f"\n------------------------------------------------------------\n\n\n")

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes-v3-preparado.csv')
print(f'\nPrimeiras 20 linhas: \n{df.head(20).to_string()}')

# Gráfico de Barras
plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisão de Escolariedade - 1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color= '#60aa65')
plt.title('Divisão de Escolariedade - 2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')

# Gráficos de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle= 90)
plt.title('Distribuição de Nível de Educação')
plt.show()

# Gráfio de Dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label = 'Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))



print('\n\n\n----- Fim de execução -----\n')
