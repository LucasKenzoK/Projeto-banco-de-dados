from estruturas import *
from ordem import *

fila_a = Queue()
fila_b = Queue()
C_pilha = Stack()

lista_pessoas = []
emergencia = []

while True:
    nome = str(input('Qual seu nome:'))
    print("Prioridade: A = Comum, B = Preferencial ou C para emergencia")
    print('(C1,C2,C3 para cada nivel de emergencia)')
    prioridade = str(input('Qual seu nivel de Priordade: ')).upper()
    while prioridade not in 'AB,C1,C2,C3':
        prioridade = str(input('ERRO!!! digite apenas A,B ou C: ')).upper()

    if prioridade in 'C1C2C3':
        emergencia.append(prioridade + '--' + nome)
    elif prioridade in 'A':
        fila_a.add(prioridade + '--' + nome)
    elif prioridade in 'B':
        fila_b.add(prioridade + '--' + nome)

    r = str(input('Quer continuar?(N|S): ')).upper()
    if r in 'N':
        break
    while r not in 'SN':
        r = str(input('E RRO!!! digite apenas S ou N: ')).upper()

for c in sorted(emergencia, reverse= True):
    C_pilha.push(c)

Ordem(fila_a,fila_b)