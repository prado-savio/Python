# 10.05

from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Visualização de Dados - Uso de Seaborn - 10.05")
#print(f"          Corrigir valores bem acima ou bem abaixo da média dos valores recebidos com SCIPY")
#print(f"Biblioteca fundamental em Python para computação científica e técnica. Ela fornece uma vasta coleção de algoritmos e funções matemáticas de alto nível")
#print(f"Instalar MatPlotLib: pip install matplotlib")
#print(f"         SeaBorn   : pip install seaborn")
#print(f"Biblioteca: Choosing color palettes")
#print(f"		https://seaborn.pydata.org/tutorial/color_palettes.html")
print(f"\n------------------------------------------------------------\n\n\n")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes-v3-preparado.csv')

df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()

# Heatmap de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, fmt='.2f')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

# Countplot
sns.countplot(x='estado_civil', data=df)
plt.title('Distribuição do Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.show()

# Countplot com legenda
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df)
plt.title('Distribuição do Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nivel de Educação')
plt.show()


print('\n\n\n----- Fim de execução -----\n')
