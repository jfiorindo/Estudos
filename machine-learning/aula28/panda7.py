import pandas 
tabela = pandas.read_csv('C:/Users/João/Desktop/py/athlete_events.csv')
tabela = tabela.drop('ID', axis = 1, inplace = True)
