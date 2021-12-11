#Exercício 1 Adicional
#Escreva um programa que receba um número inteiro positivo na entrada
# e verifique se é primo. Se o número for primo, imprima "primo".
#Caso contrário, imprima "não primo".

n = int(input("Digite um número inteiro: "))
primo = True
i = 2
resto = 0
while i < n and primo:
    resto = n % i  #Verifica se o número é primo pelo resto da divisao
    if resto == 0:
        primo = False
    i += 1
if primo:
    print("primo")
else:
    print("não primo")
