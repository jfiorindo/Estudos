import pandas 
tabela = pandas.read_csv('C:/Users/João/Desktop/py/athlete_events.csv')
tabela2 = tabela.drop('ID', axis = 1, inplace = True)
tabela2 = tabela.head()

print(tabela2)
