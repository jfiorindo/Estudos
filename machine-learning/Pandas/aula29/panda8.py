import pandas as pd
import matplotlib.pyplot as plt #biblioteca para Gráficos

tabela = pd.read_csv('C:/Users/João/Desktop/py/athlete_events.csv')

tabela2 = tabela.hist(column = 'Weight', bins = 100)
plt.show()
#faz gráficos!!!!!!!