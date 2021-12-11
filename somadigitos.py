#Exercício 3
#Escreva um programa que receba um número inteiro na entrada,
#calcule e imprima a soma dos dígitos deste número na saída

num = int(input("Digite um número inteiro: "))
digito = 0
soma = 0
while num != 0:
    digito = digito + num % 10 #tira o digito e soma com o anterior
    num = num // 10  #condição de loop. diminiu o num de digitos

print(digito)
