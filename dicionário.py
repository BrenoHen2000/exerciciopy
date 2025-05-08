#Dada uma lista de dicionários com nome e nota, ordene pela nota (maior para menor).

alunos = [
    {"nome":"Ana", "nota":5.5},
     {"nome":"Joao", "nota":8.5},
      {"nome":"DIego", "nota":4.5},
       {"nome":"Olaido", "nota":9.5},
]

#key lambda é usado para funções para especificar uma função de ordenação personalizada. Lambda é utilizado para criar funções anonimas

ordenados = sorted(alunos, key=lambda aluno: aluno["nota"])
#Lista usando o valor de x["nota"] como critério."

for aluno in ordenados:
    print(f"{aluno['nome']}- Nota: {aluno['nota']}")

print("-----------------------------")

#ordem decrescente reverse.true
ordenados = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)

for aluno in ordenados:
    print(f"{aluno['nome']}- Nota: {aluno['nota']}")