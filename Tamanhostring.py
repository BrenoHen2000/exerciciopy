#Dada uma lista de strings, crie outra com o tamanho de cada palavra.

nomes = ['breno', 'almocinho', 'aligot', 'amiguinhosinho']

#coloca quantas letras tem cada item da lista
for nome in nomes:
    print (f"{ nome } tem {len(nome)}  letras")

#coloca quantas letras tem cada item da lista em forma de lista
tamanhos = [len(nome) for nome in nomes]
print(tamanhos)

#ordena a lista do menor para o maior
nomes.sort(key=len)
print(nomes)
