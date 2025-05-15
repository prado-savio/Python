# 9.5
from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Preparação de dados - Engenharia de features - 09.05")
#print(f"          Corrigir valores bem acima ou bem abaixo da média dos valores recebidos com SCIPY")
#print(f"Biblioteca fundamental em Python para computação científica e técnica. Ela fornece uma vasta coleção de algoritmos e funções matemáticas de alto nível")
#print(f"Instalar SCIPY: pip install scipy")
print(f"\n------------------------------------------------------------\n\n\n")

import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes-v2-tratados.csv')

print(f'\nPrimeiras linhas: \n{df.head()}')

# Transformação logarítmica
df['salario_log'] = np.log1p(df['salario'])		# log1p é usado para evitar problemas com valores zero

print(f'\nDataFrame após transformação logarítmica no salario: \n {df.head()}')

# Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)

print(f'\nDataFrame após transformação Box-Cox no salario: \n {df.head()}')

# Codificação de Frequência para 'estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)

print(f'\nDataFrame após codificação de frequência para estado: \n{df.head()}')

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']

print(f'\nDataFrame após criação de interações entre idade e numero_filhos: \n {df.head()}')


print('\n\n\n----- Fim de execução -----\n')