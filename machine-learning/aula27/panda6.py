import pandas as pd
tabela = pd.read_csv('C:/Users/João/Desktop/py/athlete_events.csv')

tabela = tabela.rename(columns={'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade'})

tabela2 = tabela.head(5)
#print(tabela2)

jogos = tabela['Games']
#print(jogos)
tabela3 = tabela['Idade']
#print(tabela3)

tabela4 = tabela['Medal'].value_counts()
#print(tabela4)

tabela5 = tabela['Games'].value_counts()
#print(tabela5)

tabela6 = tabela.describe()
print(tabela6)

