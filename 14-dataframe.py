import pandas as pd

# Lista: Uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ['Ana', 'Maria', 'João']
print(f'Lista de nomes: {lista_nomes}')
print(f'Primeiro item da lista: {lista_nomes[0]}')


# Dicionário: Estrutura composta de pares: chave-valor
dicionario_pessoa = {
    'nome': 'Maria',
    'idade': 22,
    'cidade': 'Porto'
}
print(f'\nDicionário de uma pessoa: {dicionario_pessoa}')
print(f"\nAtributo do Dicionário: {dicionario_pessoa.get('nome')}")


# Lista de dicionários: Estrutura de dados que combina listas e dicionários
dados = [
    {'nome': 'Ana', 'idade': 22, 'cidade': 'Porto'},
    {'nome': 'Maria', 'idade': 17, 'cidade': 'Guimarães'},
    {'nome': 'João', 'idade': 44, 'cidade': 'Braga'}
]


# Dataframe: Estrutura de dados bidimensional
df = pd.DataFrame(dados)
print(f'\n\nDataframe: \n{df}')

# Selecionar coluna
print(f'\n\nSeleção de uma coluna específica: \n{df["nome"]}')

# Selecionar várias colunas
print(f'\n\nSeleção de várias colunas: \n{df[["nome", "idade"]]}')

# Selecionar linhas pelo índice
print(f'\n\nPrimeira linha: \n{df.iloc[0]}')

# Adicionar uma nova coluna
df['salario'] = [4100, 3600, 5200]

# Adicionar um novo registo
df.loc[len(df)] = {
    'nome': 'SaSu',
    'idade': 2,
    'cidade': 'Três Corações',
    'salario': 2200
}
print(f'\n\nDataframe atual: \n{df}')

# Remover uma coluna
#          o que quer,  coluna (1) ou linha (0)
df.drop(labels= "salario", axis = 1, inplace = True)

# Filtrando pessoas com mais de 22 anos
filtro_idade = df[df["idade"] >= 22]
print(f'\n\nFiltro: \n{filtro_idade}')

# Salvando o Dataframe em um arquivo CSV - gera fisicamente
df.to_csv(path_or_buf = 'dados.csv', index = False)

# Lendo um arquivo CSV em um Dataframe
df_lido = pd.read_csv('dados.csv')
print(f'\n\nLeitura do CSV: \n{df_lido}')

