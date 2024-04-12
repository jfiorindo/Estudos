#calculador fatorial
numero = int(input('informe um valor: '))
fatorial = numero 
contador = 1 

while (numero - contador)>1:
    fatorial = fatorial*(numero - contador)
    contador += contador
print('{0}!={1}'.format(numero, fatorial))