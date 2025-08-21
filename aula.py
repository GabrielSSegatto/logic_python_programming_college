#atividade a
lista_vazia = []

#atividade b
lista = input("Crie sua lista: ").split(' ')
print(lista)

#atividade c
lista = input("Crie sua lista: ").split(' ')
print(lista)

#ativade d
lista = input("Crie sua lista: ").split(' ')
for num in lista:
    print(num)

#ativiade e
lista = input("Crie sua lista: ").split(' ')
quantidade = len(lista)
print("A lista tem", quantidade, "elementos")

#atividade f
entrada = input("Crie sua lista: ")
lista = list(map(int, entrada.split()))
soma = sum(lista)
print(f"A soma é {soma}")

#atividade g
lista = input("Crie sua lista: ").split(' ')
list = [None] * len(lista)
i = 0
for num in lista:
    list[i] = int(num)
    i += 1
maior = float('-inf')
for num in list:
    if maior < num:
        maior = num
print(maior)

#atividade h
lista = input("Crie sua lista: ").split(' ')
list = [None] * len(lista)
i = 0
for num in lista:
    list[i] = int(num)
    i += 1
menor = float('inf')
for num in list:
    if maior > num:
        maior = num
print(maior)

#atividade i
tem = False 
entrada = input("Crie sua lista: ").split(' ')
lista = [int(num) for num in entrada] 

x = int(input("Digite o número a verificar: "))  
if x in lista:
    print("Tem")
else:
    print("Tem n")

#atividade j
tem = False 
entrada = input("Crie sua lista: ").split(' ')
lista = [int(num) for num in entrada] 

x = int(input("Digite o número a verificar: "))  
cont = 0
for num in lista:
    cont +=1
    if x == num:
        pos = cont
        tem = True
if tem == True:
    print("Tem")
    print("posição", pos-1)