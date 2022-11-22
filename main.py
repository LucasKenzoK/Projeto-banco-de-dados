from estruturas import *

recepcao = Lista_Encad()
atendimento = Stack()

lista_pessoas = []
emergencia = []

while True:
    nome = str(input('Qual seu nome:'))
    print("Prioridade: A = Comum, B = Preferencial ou C para emergencia")
    print('(C1,C2,C3 para cada nivel de emergencia)')
    prioridade = str(input('Qual seu nivel de Priordade: ')).upper()
    while prioridade not in 'AB,C1,C2,C3':
        prioridade = str(input('ERRO!!! digite apenas A,B ou C: ')).upper()

    lista_pessoas.append(prioridade + '--' + nome)

    r = str(input('Quer continuar?(N|S): ')).upper()
    if r in 'N':
        break
    while r not in 'SN':
        r = str(input('E RRO!!! digite apenas S ou N: ')).upper()

for pessoa in lista_pessoas:
    if pessoa[0:2] == 'C1':
        emergencia.append(pessoa)
    if pessoa[0:2] == 'C2':
        emergencia.append(pessoa)
    if pessoa[0:2] == 'C3':
        emergencia.append(pessoa)

for i in sorted(emergencia):
    atendimento.push(i)

print(atendimento.items)