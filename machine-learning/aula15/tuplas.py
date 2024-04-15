lista = [1, 3, 5, 7]



tupla = (2, 4, 6, 8)
tipo1 = type(tupla)
print(tipo1)

lista.append(9)
print(lista)

'''tupla.append(10)
print(tupla)
não funciona pois tupla é imutável'''

tupla2 = tuple(lista)
print(tupla2)

tipo = type(tupla2)
print(tipo)
