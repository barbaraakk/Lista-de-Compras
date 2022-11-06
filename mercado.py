from os import remove

arquivo = open("lista.txt", "r")
lista = arquivo.readlines()
arquivo = open ("lista.txt", "a")
for item in range(len(lista)):
    lista[item] = lista[item].rstrip('\n')
print("Esta é sua atual lista de compras: ",lista)

while True:
    x = input("Digite o que você quer adicionar a lista: ").upper()
    arquivo = open("lista.txt", 'r')
    if x == '':
        break
    elif x in lista:
        print("VOCÊ JÁ DIGITOU ESSE PRODUTO!")
    else:
        x = x + '\n'
        lista.append(x)
        arquivo = open("lista.txt", 'a')
arquivo.close()

arquivo = open ('lista.txt', 'r')

for palavras in range (len(lista)):
    lista[palavras] = lista[palavras].rstrip('\n')
    print("Itens adicionados a lista: ".upper(),lista[palavras])
arquivo.close()
lista2 = []
arquivo = open ('lista.txt', 'a')
while True:
    y = input("Digite o que você quer remover da lista: ").upper()
    if y == '':
        break
    else:
        lista2.append(y)
        lista.remove(y)
arquivo = open('lista.txt', 'w')
for item in lista:
    item = item+'\n'
    arquivo.writelines(item)

print("Itens removidos: ",lista2)
print("Sua lista de compras: ",lista)