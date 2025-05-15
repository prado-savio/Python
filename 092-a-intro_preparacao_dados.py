# 9.2
from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Preparação de dados - Análise Exploratória de Dados (AED) - 09.02")
print(f"\n------------------------------------------------------------\n\n\n")

import pandas as pd

df = pd.read_csv('C:/_ Estudo/Python/Ebac/clientes-v2.csv')

print(f'Primeiras linhas: \n{df.head().to_string()}')
print(f'Últimas linhas: \n{df.tail().to_string()}')
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Verificar os tipos de dados
print(f'Verificação inicial: \n{df.info()}')

print(f'\nAnálise de dados nulos: \n {df.isnull().sum()}')      # Percentual com a média
print(f'\n% de dados nulos: \n {df.isnull().mean()} * 100')
df.dropna(inplace=True)
print(f'\n\nConfirmar remoção de dados nulos: \n {df.isnull().sum().sum()}')    # Primeiro sum(): Contar o número de valores nulos em cada coluna individualmente;
                                                                                # Segundo sum() : Somar os resultados da contagem de nulos por coluna para obter o total de valores nulos em todo o DataFrame.
print(f'\n\nAnálise de dados duplicados: \n {df.duplicated().sum()}')
print(f'\n\nAnálise de dados únicos: \n {df.nunique()}')
print(f'\n\nEstatísticas dos dados: \n {df.describe()}')        # Estatísticas padrões

df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]

print(f'\n\nPrimeiras linhas: \n{df.head().to_string()}')

df.to_csv('C:/_ Estudo/Python/Ebac/clientes-v2-tratados.csv', index=False)



print('\n\n\n----- Fim de execução -----')



