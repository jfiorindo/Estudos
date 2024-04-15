def adicao(x,y):
    return x + y
def subtracao(x,y):
    return x - y
def multiplicacao(x,y):
    return x * y
def divisao(x,y):
    return x / y

print("Escolha uma opração: ")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Escolha a sua operação de 1 a 4: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if(escolha == "1"):
    print(num1, '+', num2, '=', adicao(num1,num2))
elif(escolha == "2"):
    print(num1, '-', num2, '=', subtracao(num1,num2))
elif(escolha == "3"):
    print(num1, '*', num2, '=', multiplicacao(num1,num2))
else:
    print(num1, '/', num2, '=', divisao(num1,num2))

input("Pressione a tecla enter para finalizar: ")