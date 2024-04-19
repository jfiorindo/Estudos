import pandas as pd
notas = {'Alunos':['Bruno', 'João', 'Ana', 'José',], 
         'Notas':['10', '7', '10', '4'],
         'Situacao':['Aprovado', 'Aprovado', 'Aprovado', 'Reprovado']}

tabela = pd.DataFrame(notas)

print(tabela)