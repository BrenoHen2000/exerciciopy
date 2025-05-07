#Remova todos os elementos repetidos de uma lista.

lista = [2,3,5,1,2,3,1,52,4,2,5,6]

# o set é uma lista mas com valores únicos
meu_set = set (list)
print (meu_set)

#transforma lista em set e depois em lista novamente
lista = list(set(lista))
print(lista)

#para os dicionários a ordem importa
meu_dic = list(dict.fromkeys(lista))
print(meu_dic)
#transforma o dicionario em lista
lista = list(dict.fromkeys(lista))
print(lista)