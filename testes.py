from estruturas import *

lista = Lista_Encad()

pessoas = [['cleber', 'B'], ['ana', ' A'], ['Joao', 'A']]

lista.add_final(pessoas[0])
lista.add_final(pessoas[1])
lista.add_final(pessoas[2])

print(lista[0])