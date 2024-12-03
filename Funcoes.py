
def inicio():
    from datetime import datetime

    for i in range(7):
        print('')
    print(f'\n        Executado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
    #--------------------------------------------------------------