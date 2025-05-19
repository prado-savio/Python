# 10.04

from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Visualização de Dados - Uso de Seaborn - 10.04")
print(f"Biblioteca: Choosing color palettes")
print(f"		https://seaborn.pydata.org/tutorial/color_palettes.html")
print(f"\n------------------------------------------------------------\n\n\n")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes-v3-preparado.csv')
print(f'\nPrimeiras linhas: \n{df.head().to_string()}')

# Gráfico de Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')		#['scatter', 'hist', 'hex', 'kde', 'reg', 'resid']
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.show()

# Gráfico de Regressão
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatterkws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

# Gráfico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', date=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nivel de Educação')
plt.show()


print('\n\n\n----- Fim de execução -----\n')