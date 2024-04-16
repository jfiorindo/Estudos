polegadas = [1, 2, 3, 4, 5, 6, 7, 8]
mm = []

for i in polegadas:
    mm.append(i*25.4)
print (mm)

mm2 = list(map(lambda x: x*25.4, polegadas))
print(mm2)

mm3 = [x*25.4 for x in polegadas]
print(mm3)

curso = [i for i in "Python"]
print(curso)