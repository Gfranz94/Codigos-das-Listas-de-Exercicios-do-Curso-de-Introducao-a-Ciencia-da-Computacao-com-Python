#Exercício 2 - Invertendo sequência
#Como pedido na primeira video-aula desta semana,
#escreva um programa que recebe uma sequência de números inteiros e
#imprima todos os valores em ordem inversa.
#A sequência sempre termina pelo número 0.
#Note que 0 (ZERO) não deve fazer parte da sequência.

n = 1
lista = []
while n != 0:
     n = int(input("Digite um número: "))
     if n != 0:
          lista.append(n)
i = len(lista) - 1
while i >= 0:
    print(lista[i])
    i -= 1
