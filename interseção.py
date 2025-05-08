#Implemente uma função que receba duas listas e retorne a interseção entre elas (valores comuns).

lista1 = [2,1,4,6,42,6,5,8,4,85,74,2]
lista2 = [4,5,8,85,4,2,6,8,5,4,9,14]

intersecao = list(set(lista1)&set(lista2))
print(intersecao)