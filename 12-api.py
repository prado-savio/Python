import requests

print(' -API\n\n\n')

#--- Funções
def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = 'C:/_ Estudo/Python/Ebac/ColetaDados/teste-de-envio.txt'

    # Enviar o arquivo                                                          'r' read ; 'b' binário
    requisicao = requests.post(url= 'https://file.io', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(f'Saída da requisição 1: {saida_requisicao}')
    # saida_requisição = dicionário
    # saida_requisição = {'success': True, 
    #                       'status': 200, 
    #                       'id': 'bbda4120-b5ac-11ef-8ba8-070cbf59b54b', 'key': 'tiz0n3CKxGyt', 'path': '/', 'nodeType': 'file', 'name': 'teste-de-envio.txt', 'title': None, 'description': None, 'size': 0, 'link': 'https://file.io/tiz0n3CKxGyt', 'private': False, 'expires': '2024-12-22T21:38:16.230Z', 'downloads': 0, 'maxDownloads': 1, 'autoDelete': True, 'planId': 0, 'screeningStatus': 'pending', 'mimeType': 'text/plain', 'created': '2024-12-08T21:38:16.230Z', 'modified': '2024-12-08T21:38:16.230Z'}

    url = saida_requisicao['link']
    print(f'Arquivo enviado. Link para acesso: {url}')


def enviar_arquivo_chave():
    # Caminho do arquivo e chave para upload
    caminho = 'C:/_ Estudo/Python/Ebac/ColetaDados/teste-de-envio.txt'
    # Fazer login no site (variável url), no menu "Account", submenu "API Keys", criar uma
    chave_acesso = 'CHAV-OBTID-ANOS-ITE'          # API KEY


    # Enviar arquivo
    requisicao = requests.post(
        url = 'https://file.io',
        files = {'file': open(caminho, 'rb')},
        headers = {'Authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()

    print(f'Saída da requisição 2: {saida_requisicao}')
    url = saida_requisicao['link']
    print(f'Arquivo enviado com chave. Link para acesso: {url}')


def receber_arquivo(file_url):
    # Receber arquivo
    requisicao = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print(f'Arquivo baixado com sucesso.')
    else:
        print(f'Erro ao baixar o arquivo: {requisicao.json()}')


enviar_arquivo()
enviar_arquivo_chave()
receber_arquivo('endereço-recebido-na-função-enviar...-na-variável-saida_requisicao')


