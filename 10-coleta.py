# https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/

import requests                     # importa todo módulo
from bs4 import BeautifulSoup       # importa apenas a classe BeautifulSoup
                                    # não há necessidade de fazer a chamada completa módulo.Classe
import pandas

origem = 'https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/'


print('Três formas de recuperar e armazenar dados de uma url - Web Scraping\n\n\n')


print('\n--- Request - resposta em um linha\n')
response = requests.get(origem)
print(response.text[:1111])


print('\n\n--- BeautifulSoup - resposta como visão de página, ié, quebras de linha\n')
#    Propriedades:      texto     , tipo de entrega
soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:1111])


print('\n\n--- Pandas - resposta em forma de tabela\n')
url_dados = pandas.read_html(origem)
print(url_dados[0].head(15))                            # 0 = sequencial de tabelas. 0 é a tabela principal
                                                        # head é para imprimir um limite de linhas





