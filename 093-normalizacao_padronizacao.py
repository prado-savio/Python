# 9.3
from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Preparação de dados - Normalização Padronização - 09.03")
#print(f"          Corrigir valores bem acima ou bem abaixo da média dos valores recebidos com SCIPY")
#print(f"Biblioteca fundamental em Python para computação científica e técnica. Ela fornece uma vasta coleção de algoritmos e funções matemáticas de alto nível")
print(f"Instalar Sklearn: pip install scikit-learn")
print(f"\n------------------------------------------------------------\n\n\n")

import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes-v2-tratados.csv')

print(f'\nPrimeiras linhas: \n{df.head()}')

df = df.drop(labels=['data', 'estado', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao'], axis=1)

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))

df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(f'\nPrimeiras quinze linhas: \n {df.head(15)}')

print(f'\n\nMinMaxScaler (De 0 a 1):')
print(f'\nIdade - Min {df["idadeMinMaxScaler"].min():.4f} Max: {df["idadeMinMaxScaler"].max():.4f} Mean: {df["idadeMinMaxScaler"].mean():.4f} Std: {df["idadeMinMaxScaler"].std():.4f}')
print(f'\nSalario - Min {df["salarioMinMaxScaler"].min():.4f} Max: {df["salarioMinMaxScaler"].max():.4f} Mean: {df["salarioMinMaxScaler"].mean():.4f} Std: {df["salarioMinMaxScaler"].std():.4f}')

print(f'\n\nMinMaxScaler (De -1 a 1):')
print(f'\nIdade - Min {df["idadeMinMaxScaler_mm"].min():.4f} Max: {df["idadeMinMaxScaler_mm"].max():.4f} Mean: {df["idadeMinMaxScaler"].mean():.4f} Std: {df["idadeMinMaxScaler_mm"].std():.4f}')
print(f'\nSalario - Min {df["salarioMinMaxScaler_mm"].min():.4f} Max: {df["salarioMinMaxScaler_mm"].max():.4f} Mean: {df["salarioMinMaxScaler"].mean():.4f} Std: {df["salarioMinMaxScaler_mm"].std():.4f}')

print(f'\n\nStandardScaler (Ajuste a média a 0 e desvio padrão a 1):')
print(f'\nIdade - Min {df["idadeStandardScaler"].min():.4f} Max: {df["idadeStandardScaler"].max():.4f} Mean: {df["idadeStandardScaler"].mean():.4f} Std: {df["idadeStandardScaler"].std():.4f}')
print(f'\nSalario - Min {df["salarioStandardScaler"].min():.4f} Max: {df["salarioStandardScaler"].max():.4f} Mean: {df["salarioStandardScaler"].mean():.4f} Std: {df["salarioStandardScaler"].std():.4f}')

print(f'\n\nRobustScaler (Ajuste a média a 0 e desvio padrão a 1):')
print(f'\nIdade - Min {df["idadeRobustScaler"].min():.4f} Max: {df["idadeRobustScaler"].max():.4f} Mean: {df["idadeRobustScaler"].mean():.4f} Std: {df["idadeRobustScaler"].std():.4f}')
print(f'\nSalario - Min {df["salarioRobustScaler"].min():.4f} Max: {df["salarioRobustScaler"].max():.4f} Mean: {df["salarioRobustScaler"].mean():.4f} Std: {df["salarioRobustScaler"].std():.4f}')

print('\n\n\n----- Fim de execução -----\n')