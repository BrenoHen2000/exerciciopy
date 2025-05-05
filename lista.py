bebidas = []
print("digite a sua bebida preferida: ")

n=0

for i in range (5):
    n = n + 1
    bebidas.append(input(f"{n}: "))

for bebida in bebidas:
    bebidas.sort()
    print(bebidas)