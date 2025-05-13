# 8.5
from datetime import datetime

for i in range(7):
    print('')
print(f"\n------------------------------------------------------------")
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
print(f"Objetivo: Tratar dados inconsistencias - 08.05")
#print(f"          Corrigir valores bem acima ou bem abaixo da média dos valores recebidos com SCIPY")
#print(f"Biblioteca fundamental em Python para computação científica e técnica. Ela fornece uma vasta coleção de algoritmos e funções matemáticas de alto nível")
#print(f"Instalar SCIPY: pip install scipy")
print(f"\n------------------------------------------------------------\n\n\n")

import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('C:/_ Estudo/Python/Ebac/cliente_remove_outliers.csv')

print(f'Primeras linhas do DataFrame: \n, {df.head()}')

# Mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')

# Corrigir Datas
df['data'] = pd.to_datetime(df['data'], format='%Y--5m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
df['idade_ajustada'] = ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan           # atribuir valor nulo

# Corrigir campo com múltiplas informações
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split(' / ')[-1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')

# Verificando a formatação do endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço inválido' if len(x) > 50 or len(x) < 5 else x)

# Corrigir dados errôneos
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'CPF inválido')

estados_br = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RN', 'TO']
print(f'Dados tratados:\n', df.head())

df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'bairro', 'estado']]
df_salvar.to_csv('C:/_ Estudo/Python/Ebac/clientes_tratados.csv', index = False)


print('\n\n\n----- Fim de execução -----')

