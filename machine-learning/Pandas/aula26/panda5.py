import pandas as pd
notas = {'Alunos':['Bruno', 'João', 'Ana', 'José',], 
         'Notas':['10', '7', '10', '4'],
         'Situacao':['Aprovado', 'Aprovado', 'Aprovado', 'Reprovado']}

tabela = pd.DataFrame(notas)

#print(tabela['Situacao']) / Busca apenas a coluna 
#print(tabela.loc[[0]]) / busca a linha 
#print(tabela.loc[tabela['Notas'] == '10']) / Busca na tabela notas onde tem o número 10 e retorna as linhas encontradas
#print(tabela.loc[tabela['Situacao'] == 'Aprovado']) / Busca os aprovados na tabela e retorna
print(tabela.loc[tabela['Alunos'] == 'João']) #Busca na tabela todos as pessoas chamadas joão