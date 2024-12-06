import requests
from bs4 import BeautifulSoup

origem = 'https://wiki.python.org.br/AprendaMais'


print(' - Web Scraping\n\n\n')

requisicao = requests.get(origem)
extracao = BeautifulSoup(requisicao.text, features= 'html.parser')

print('\n--- Exibir o texto da página\n\n')
print(extracao.text.strip())                    # strip: remover espaços


print('\n--- Exibir o Título\n\n')
# Filtrar a exibição pela tag
#     find_all: encontrar e mostrar o valor do parâmetro, no caso 'h2'
for linha_texto in extracao.find_all('h2'):
      titulo = linha_texto.text.strip()
      print('Titulo: ', titulo)


print('\n--- Exibir o Título e a Descrição\n\n')
contar_titulo = 0
contar_descricao = 0

for linha_texto in extracao.find_all(['h2', 'p']):
      if linha_texto.name == 'h2':
            contar_titulo += 1
            print(f'Título: {linha_texto.text.strip()}')
      elif linha_texto.name == 'p':
            contar_descricao += 1
            if contar_titulo == 7: print(f'      : {linha_texto.text.strip()}')

print(f'\n\nTotal de Tíulos: {contar_titulo}')
print(f'Total Descrição: {contar_descricao}')


print('\n--- Exibir tags aninhada\n\n')     # isto é, dentro de uma tag até encontrar a tag desejada
for titulo in extracao.find_all('h2'):                                      # para cada 'h2'
      print('\n*** Título: ', titulo.text.strip())
      for link in titulo.find_next_siblings('p'):                           # _siblings: procurar
                                                                            # as tags até encontrar 'p'
            for a in link.find_all('a', href = True):                       # encontrar todos 'a'
                  print(f"Link: {a.text.strip()}, | URL: {a['href']}")
                  #                 texto do link             link



print('\n--- FIM\n\n')
