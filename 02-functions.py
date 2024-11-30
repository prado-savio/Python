import datetime
#-- Importa apenas uma função
# from datetime import date

print(f"La fecha de hoy es: {datetime.date.today()}")
print(f"El dia {datetime.date.today().day}")


# Criar função

def imprime(recebido):
    print(f"\n{recebido}")

def somaQuadrados(n1, n2):
    somaQ = n1 ** 2 + n2 ** 2
    return somaQ

a = 5
b = 7
somaQuadrados(a, b)
imprime('A soma dos quadrados dos números: ', a, " e ", b, " é: ", somaQuadrados(a, b))
