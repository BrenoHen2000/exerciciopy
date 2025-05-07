# Crie uma lista de 10 números aleatórios entre 1 e 100 e exiba apenas os pares.]

import random

for i in range (10):
    n = random.randint (1, 100)
   
    if n%2==0:
        print (f"{n} é par")
    else:
        print (f"{n} é impar")
    
