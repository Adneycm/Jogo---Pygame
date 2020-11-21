'''lista = []
for i in range(5):
    x = float(input("digite um número: "))
    lista.append(x)
    
#usar o truque do maior
soma = 0
#maior = lista[i]
for j in lista:
    soma = soma + j
 

print("Soma = {0}. Maior valor = {1}".format(soma, max(lista)))'''

lista = []
soma = 0
i =1
while i < 4:
    x = float(input("qual a nota? "))
    lista.append(x)
    soma = soma + lista[i]
    media = soma/i

print(lista)
print(media)    



    
