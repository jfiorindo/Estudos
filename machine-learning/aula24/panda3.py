import pandas as pd
import numpy as np

pares = ([2, 4, 6, 8])
pares1 = pd.Series(pares)
print(pares1)

impares = np.array([1, 3, 5, 7])
print(impares)

primos = np.array([(2, 3, 5, 7), (11, 13, 17, 19)])
print(primos)