# Faker = 

import pandas as pd
import random
from faker import Faker

feiqui = Faker('pt_BR')

dados_pessoas = []

# _ é uma variável descartável. Não vai ser utilizada dentro do loop
for _ in range(10):
    #var = pacote.atributos
    nome = feiqui.name()
    cpf = feiqui.cpf()
    idade = random.randint(a = 18, b = 60)
    data = feiqui.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    endereco = feiqui.address()
    estado = feiqui.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }

    dados_pessoas.append(pessoa)


df_pessoas = pd.DataFrame(dados_pessoas)
print(f'\n\nDataframe em Display \n{df_pessoas}')

# Opções para não fazer o corte de linhas
pd.set_option('display.max_columns', None)      # Poderia limitar o número de colunas
pd.set_option('display.max_rows', None)         # Poderia limitar o número de linhas
pd.set_option('display.max_colwidth', None)     # largura de colunas
pd.set_option('display.width', None)            # largura de display

# Ou através do display ou através do string
print(f'\n\nDataframe - String: \n{df_pessoas.to_string()}')

# Salvar em ficheiro
df_pessoas.to_csv('dadosGerados.csv')