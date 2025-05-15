# 9.4
from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Preparação de dados - Codificação de Variáveis Categóricas - 09.04")
#print(f"          Corrigir valores bem acima ou bem abaixo da média dos valores recebidos com SCIPY")
#print(f"Biblioteca fundamental em Python para computação científica e técnica. Ela fornece uma vasta coleção de algoritmos e funções matemáticas de alto nível")
#print(f"Instalar SCIPY: pip install scipy")
print(f"\n------------------------------------------------------------\n\n\n")

import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes-v2-tratados.csv')

print(df.head())

# Codificação one-hot para 'estado_civil'
df = pd.concat(objs=[df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print(f'\nDataFrame após codificação one-hot para estado_civil \n, {df.head()}')

# Codificação ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print(f'\nDataFrame após codificação ordinal para nivel_educacao: \n {df.head()}')

# Transformar 'area_atuacao' em categorias codificadas usando o método .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes

print(f'\nDataFrame após transformar area_atuacao em códigos numéricos: \n {df.head()}')

# LabelEncoder para 'estado'
# LabelEncoder converte cada valor único em números de ' a n_classes-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])

print(f'\nDataFrame após aplicar LabelEncoder em estado: \n {df.head()}')


print('\n\n\n----- Fim de execução -----\n')
