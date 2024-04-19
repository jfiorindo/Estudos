import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv('C:/Users/João/Desktop/py/athlete_events.csv')

tabela2 = tabela.boxplot(column = ['Age', 'Height', 'Weight'])
plt.show()
