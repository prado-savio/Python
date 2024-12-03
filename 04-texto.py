import Funcoes

Funcoes.inicio()

# texto = "abcdefghijklmnopqrstuvxyz1234567890"
texto = list(range(1,44))

print(f'Imprimir as posições iniciais: {texto[:17]}')
print(f'\nImprimir as últimas posições: {texto[17:]}')
print(f'\nImprimir um intervalo posições: {texto[17:22]}')
print(f'\nImprimir as últimas posições: {texto[-7:]}')
print('\n')


