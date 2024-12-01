from datetime import datetime

for i in range(7):
    print('')
print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
#--------------------------------------------------------------
# Lista         []
print(f'------------ LISTA ------------')
lista = [10, 11, 22, 33, 44]

for i in lista:
    print(f'Valores: {i}')


# Adicionar
lista.append(55)

contador = 0
for i in range(len(lista)):
    if not contador:
        print(f'Na posição {i}, temos o valor: {lista[i]}')
        contador = 1
    else:
        print(f'           {i},                {lista[i]}')

#--------------------------------------------------------------
# Tupla         ()
# Não permite alteração na lista
print(f'\n------------ TUPLA ------------')

tupla = [100, 111, 222, 333, 444]

for i in tupla:
    print(f'Valores: {i}')


contador = 0
for i in range(len(tupla)):
    if not contador:
        print(f'Na posição {i}, temos o valor: {tupla[i]}')
        contador = 1
    else:
        print(f'           {i},                {tupla[i]}')


#--------------------------------------------------------------
# Dicionário    {}
print(f'\n------------ DICIONÁRIO ------------')

# Criando uma lista de dicionários
pessoas = [
    {
        "nome": "João",
        "idade": 30,
        "hobbies": ["futebol", "leitura", "viagens"]
    },
    {
        "nome": "Maria",
        "idade": 25,
        "hobbies": ["dança", "cinema"]
    },
    {
        "nome": "Carlos",
        "idade": 35,
        "hobbies": ["caminhadas", "fotografia"]
    }
]

for gente in pessoas:
    print(gente["nome"])

contador = 0
for i in range(len(pessoas)):
    if not contador:
        print(f'Na posição {i}, temos o dicionário: {pessoas[i]}')
        contador = 1
    else:
        print(f'           {i},                     {pessoas[i]}')


