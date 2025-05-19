# 10.02

from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Visualização de Dados - Introdução - 10.02")
print(f"Instalar MatPlotLib: pip install matplotlib")
print(f"         SeaBorn   : pip install seaborn")
print(f"\n------------------------------------------------------------\n\n\n")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes-v3-preparado.csv')
print(f'\nPrimeiras linhas: \n{df.head().to_string()}')

# Histograma
plt.hist(df['salario'])
plt.show()

# Histograma - Parâmetros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição de Salário')
plt.xlabel('Salario')
plt.xticks(ticks=range(0, int(df['salario'].max() + 2000), 2000))
plt.ylabel('Frequencia')
plt.grid(True)
plt.show()

# Múltiplos gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)		# Linha, Coluna, Gráfico

# Gráfico de Dispersão
plt.scatter(df['salario'], df['salario'])
plt.ttle('Dispersão - Salario e Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')
plt.subplot(1, 2, 2)		# Linha, Coluna, Gráfico
plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha=0.6, s=30)		# cor hexadecimal online
plt.title('Dispersão - Idade e Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

# Mapa de Calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3)		# Linha, Coluna, Gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Idade')

plt.tight_layout()			# Ajustar espaçamentos
plt.show()



print('\n\n\n----- Fim de execução -----\n')