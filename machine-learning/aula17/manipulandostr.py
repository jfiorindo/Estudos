apresentacao = 'Eu nasci em 1990 e moro em São Paulo'
#letra = apresentacao[3] pega a letra que você colocar o número
#entre = apresentacao[0:10] busca tudo entre os caracteres 0 e 10
#pula = apresentaca0[0:20:2] pula de dois em dois e busca tudo entre 0 e 20

contadordea = apresentacao.count('a')
print(contadordea)

contadordecaracteres = len(apresentacao)
print(contadordecaracteres)

trocar = apresentacao.replace('em São Paulo', 'no Brasil')
print(trocar)