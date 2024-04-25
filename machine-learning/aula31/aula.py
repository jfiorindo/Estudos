import matplotlib.pyplot as plt
import numpy as np

valor = [2, 4, 6, 8, 10, 12, 14, 16]
produto = [1, 2, 3, 4, 5, 6, 7, 8]

#plt.scatter(valor, produto)
#plt.show()

x = np.arange(0, 100, 1)
print(x)

plt.plot(x, x**2)
plt.show()