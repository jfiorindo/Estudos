def multiplicacao(x,y):
    mult = x * y
    return mult
test = multiplicacao(2, 5)
print(test)

multiplicacao2 = lambda x, y: x * y
test2 = multiplicacao2(2, 5)
print(test2)

num10 = lambda a: a*3
test3 = num10(5)

print(test3)