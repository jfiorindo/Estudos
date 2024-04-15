import time
contador=0
while contador < 5:
    print("Vermelho")
    contador = contador+1 #aumentar de 1 em 1
    if contador  == 3: #quebra o while no 3 e continua fora
        break
    time.sleep(1) #contar por segundos
print("verde")