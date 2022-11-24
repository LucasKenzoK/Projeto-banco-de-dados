from Estruturas import *
from Ordem import *
fila_a = Queue()
fila_b = Queue()
pilha_c = Stack()

lista_pessoas = []
emergencia = []
valido = False

while not valido:
    nome = str(input('Qual seu nome:'))
    print("Prioridade: A = Comum, B = Preferencial ou C para emergencia")
    print('(C1,C2,C3 para cada nivel de emergencia)')
    prioridade = str(input('Qual seu nivel de Priordade: ')).upper()

    if prioridade not in 'AB,C1,C2,C3':
        prioridade = str(input('ERRO!!! digite apenas A,B ou C: ')).upper()
    else:
        if prioridade in 'C1C2C3':
            emergencia.append(prioridade + '--' + nome)
        elif prioridade in 'A':
            fila_a.add(prioridade + '--' + nome)
        elif prioridade in 'B':
            fila_b.add(prioridade + '--' + nome)
    
    r = str(input('Quer continuar?(N|S): ')).upper()
    while r not in 'SN':
        r = str(input('E RRO!!! digite apenas S ou N: ')).upper()
    if r in 'N':
        break  

Ordem.emergencia(emergencia,pilha_c)
Ordem.Comum_pref(fila_a,fila_b)