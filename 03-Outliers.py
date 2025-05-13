# 8.4
from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Outliers - 08.04")
print(f"          Corrigir valores bem acima ou bem abaixo da média dos valores recebidos com SCIPY")
print(f"Biblioteca fundamental em Python para computação científica e técnica. Ela fornece uma vasta coleção de algoritmos e funções matemáticas de alto nível")
print(f"Instalar SCIPY: pip install scipy")
print(f"\n------------------------------------------------------------\n\n\n")

import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes_posLimpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print(f'Filtro básico \n', df_filtro_basico[['nome', 'idade']])

# Identificar outliers com Z-score                      # desvio padrão
z_scores = stats.zscore(df['idade'].dropna())           # dropna: remover valores nulos
outliers_z = df[z_scores >= 3]
print(f'\nOutliers pelo Z-score:\n', outliers_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)]

# Identifica outliers com IQR
Q1 = df['idade'].quantile(0.25)                         # percentual
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print(f'\nLimites IQR: ')
print(f'Limite Baixo: {limite_baixo}')
print(f'Limite Alto : {limite_alto}')

#                                               OR
outliers_iqr = df[((df['idade'] < limite_baixo) | (df['idade'] > limite_alto))]
print(f'\nOutliers pelo IQR: \n', outliers_iqr)

# ou esta forma de filtro
#Filtrar outliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# ou define os valores
limite_baixo = 1
limite_alto = 100
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# Filtrar endereços inválidos
df['endereco'] = df['endereco'].astype(str)                 # Converter o campo caso não esteja no formato 'string'
#                                                                           dividir em campos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)
print(f'\nQtd registros com Endereços inválidos: ', (df['endereco'] == 'Endereço inválido').sum())

# Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print(f'\nQtd registros com nomes grandes: ', (df['nome'] == 'Nome inválido').sum())

print(f'\nDados com Outliers tratados: \n', df)

# Salvar dataframe
df.to_csv('C:/_ Estudo/Python/Ebac/cliente_remove_outliers.csv', index = False)


print('----- Fim de execução -----')





